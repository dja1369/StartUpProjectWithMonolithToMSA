import base64
from random import Random

import uvicorn
from fastapi import FastAPI, File, UploadFile
from fastapi.responses import HTMLResponse

# 모델 선언
model = Random()
model.object_name = ["사과", "바나나", "포도", "딸기"]
model.param = [i for i in range(2000)]
app = FastAPI()

css = """
body {
    font-family: Arial, sans-serif;
    background-color: #F4F4F4;
    margin: 0;
    padding: 0;
}

h1 {
    color: #333;
}

.container {
    width: 80%;
    margin: 0 auto;
    padding: 20px;
    background-color: #fff;
    box-shadow: 0 0 20px rgba(0, 0, 0, 0.1);
}
"""


# 이미지 업로드를 위한 서비스 선언
@app.get("/", response_class=HTMLResponse)
def serve():
    return HTMLResponse(
        content=f"""
            <html>
                <head>
                    <title>태정 노이드 이미지 처리 서비스</title>
                    <style>{css}</style>
                </head>
                <body>
                    <div class="container">
                        <h1>태정 노이드 이미지 처리 서비스</h1>
                        <p>이미지를 업로드 해주세요.</p>
                        <form action="/upload" method="post" enctype="multipart/form-data">
                            <input type="file" name="files", multiple>
                            <button type="submit">!슛!</button>
                        </form>
                    </div>
                </body>
            </html>
            """
    )


@app.post("/upload", response_class=HTMLResponse)
async def upload(files: list[UploadFile] = File(...)):
    results = []
    for file in files:
        contents = await file.read()
        result = process_image(img=contents)
        encoding_image = base64.b64encode(result['image']).decode('utf-8')
        results.append(f"""
        <div>
            <h1> 이미지 처리 결과 </h1>
            <img src="data:image/jpeg;base64,{encoding_image}" alt="업로드된 이미지">
            <p> 객체: {result['object']} </p>
            <p> 좌표: {result['coordinate']} </p>
        </div>
        """)
    return HTMLResponse(
        content=f"""
        <html>
            <head>
                <title> 이미지 처리 결과 </title>
                <style>{css}</style>
            </head>
            <body>
                {"".join(results)}
            </body>
        </html>
        """
    )


# 이미지를 받아서 처리하는 함수
def process_image(img):
    print("이미지 처리 시작")

    name = model.sample(model.object_name, 1)
    coordinate = model.sample(model.param, 4)

    print("이미지 처리 중")

    result = {"image": img, "object": name, "coordinate": coordinate}

    print("이미지 처리 완료")
    return result


if __name__ == '__main__':
    uvicorn.run(
        app, host="0.0.0.0", port=8000
    )
