import base64

from fastapi import File, UploadFile, APIRouter
from fastapi.requests import Request
from fastapi.responses import HTMLResponse

from domain.entity import InferenceEntity, InferenceResultEntity
from service.container import get_service

route = APIRouter()


@route.get("/", response_class=HTMLResponse)
def serve(request: Request):
    """
    이미지 업로드 페이지를 렌더링합니다.
    :param request:
    :return html:
    """
    templates = get_service("template")
    return templates.TemplateResponse("index.html", {"request": request})


@route.post("/upload", response_class=HTMLResponse)
async def upload(request: Request, files: list[UploadFile] = File(...)):
    """
    이미지를 업로드하고 결과를 렌더링합니다.
    :param request:
    :param files:
    :return html:
    """
    templates = get_service("template")
    model = get_service("model")
    results = []
    for file in files:
        contents = await file.read()
        result: InferenceEntity = model.process_image(img=contents)
        encoding_image = base64.b64encode(result.image).decode('utf-8')
        results.append(
            InferenceResultEntity(
                encoded_image=encoding_image,
                object=result.object,
                coordinate=result.coordinate
            )
        )

    return templates.TemplateResponse("result.html", {"request": request, "results": results})
