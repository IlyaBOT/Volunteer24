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

        @self.app.get("/zakzak", response_class=HTMLResponse)
        async def zakaz_page(request: Request):
            return self.templates.TemplateResponse("front/indexaccount/index.html", {"request": request})

        @self.app.post("/auth", response_class=HTMLResponse)
        async def handle_auth(request: Request, part_name: str = Form(None), email: str = Form(...), password: str = Form(...)):
            from auth import process_auth
            result = process_auth(part_name=part_name, email=email, password=password)

            print("Результат process_auth:", result)

            if result.get("error"):
                print("Ошибка авторизации:", result["error"])
                return self.templates.TemplateResponse("front/auth/auth.html", {
                    "request": request,
                    "error_message": result["error"]
                })


            # Перенаправление на /account
            from fastapi.responses import RedirectResponse
            return RedirectResponse(url="/account", status_code=303)

        @self.app.get("/account", response_class=HTMLResponse)
        async def account_page(request: Request):
            return self.templates.TemplateResponse("front/account/account.html", {"request": request})


if __name__ == "__main__":
    # Запуск сервера через uvicorn
    server = App()
    uvicorn.run(server.app, host="10.254.198.144", port=8080, workers=True)