from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from auth import process_auth 
import uvicorn


class App:
    def __init__(self):
        self.app = FastAPI() 
        self.templates = Jinja2Templates(directory="../") # Папка с html шаблонами
        self.app.mount("/assets", StaticFiles(directory="../assets"), name="assets") # Подключаем статику для стилей и картинок
        self._setup_routes() # Инициирование путей

    def _setup_routes(self):
        # Тут у нас роуты
        # Пример с get запросом 
        @self.app.get("/", response_class=HTMLResponse)
        async def root_route(request: Request):
            return self.templates.TemplateResponse("index.html", {
                "request": request
            })

        @self.app.get("/auth", response_class=HTMLResponse)
        async def auth_page(request: Request):
            return self.templates.TemplateResponse("front/auth/auth.html", {"request": request})

        @self.app.get("/account", response_class=HTMLResponse)
        async def about_me_page(request: Request):
            from auth import sessions  # Импорт из auth.py

            uid = request.cookies.get("user_uid")
            if not uid or uid not in sessions:
                return RedirectResponse(url="/auth", status_code=303)

            email = sessions[uid]

            db = UserDatabaseManager()
            users = db.read_all_users()

            user_data = next((u._mapping for u in users if u._mapping['email'] == email), None)
            if not user_data:
                return self.templates.TemplateResponse("front/account/account.html", {
                    "request": request,
                    "error": "Пользователь не найден"
                })

            return self.templates.TemplateResponse("front/account/account.html", {
                "request": request,
                "full_name": user_data['full_name'],
                "email": user_data['email'],
                "inn": user_data['inn'],
                "number": user_data['phone'],
                "born": user_data['birth_date'],
                "raiting": user_data.get('achievements', '–'),
                "bonus": "42 очка доверия"  # можно заменить на реальное поле
            })

        @self.app.get("/account", response_class=HTMLResponse)
        async def account_page(request: Request):
            return self.templates.TemplateResponse("front/account/account.html", {"request": request})


if __name__ == "__main__":
    # Запуск сервера через uvicorn
    server = App()
    uvicorn.run(server.app, host="10.254.198.144", port=8080, workers=True)