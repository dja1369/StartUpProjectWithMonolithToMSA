from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from domain.ai_model import AIModel


def get_container():
    """
    FastAPI 컨테이너를 반환합니다.
    :return app:
    """
    app = FastAPI()
    app.mount("/static", StaticFiles(directory="static"), name="static")
    return app


def inject_route(app, route):
    """
    FastAPI 라우터를 주입합니다.
    :param app:
    :param route:
    """
    app.include_router(route)
    return app


def get_service(bean: str):
    """
    서비스를 반환합니다.
    :param bean:
    :return prototype_service => Jinja2Templates | AIModel:
    """
    match bean:
        case "template":
            return Jinja2Templates(directory="templates")
        case "model":
            return AIModel()
