from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
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
        
        # Рендеринг страницы
        @self.app.get("/auth", response_class=HTMLResponse)
        async def about_me_page(request: Request):
            return self.templates.TemplateResponse("front/auth/auth.html", {"request": request})

        # Рендеринг страницы
        @self.app.get("/account", response_class=HTMLResponse)
        async def about_me_page(request: Request):
            return self.templates.TemplateResponse("front/account/account.html", {"request": request})
        
        # Пример с post запросом
        #@self.app.post("/aboutme", response_class=HTMLResponse)
        #async def post_exemple(request: Request, name: str =  Form(...)):
        #    message = f"Я, {name}"
        #    return self.templates.TemplateResponse("../front/auth/auth.html", {
        #        "request": request,
        #        "message": message
        #    })


if __name__ == "__main__":
    # Запуск сервера через uvicorn
    server = App()
    uvicorn.run(server.app, host="localhost", port=8080, workers=True)