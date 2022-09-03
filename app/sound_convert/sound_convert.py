#음성데이터 텍스트 변환
from fastapi import FastAPI

app = FastAPI()


@app.get("/sound")
async def sound_convert(name: str):
    return {"message": f"Hello {name}"}
