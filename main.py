from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}


#사운드 파일을 업로드 받는 페이지 호출
@app.get("sound/fileupload/")
async def fileupload():
    return ""

#엘라스틱에게 쿼리를 전달하는 페이지
#엘라스티긍로 부터 결과를 넘겨 받아서 리스트화