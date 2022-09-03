#음성데이터 텍스트 변환
from fastapi import FastAPI
import requests
import speech_recognition as sr

app = FastAPI()


@app.get("/sound")
async def sound_convert(name: str):
    return {"message": f"Hello {name}"}





def get_sound(cookies: list[dict]) -> None:
    # https://safind.scourt.go.kr/sf/captchaImg?t=audio
    session = requests.Session()

    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])

    wav_file = session.get('https://safind.scourt.go.kr/sf/captchaImg?t=audio')
    with open('/Users/hwang-eunseog/PycharmProjects/casesCrawler/resource/captchaImg.wav', 'wb') as f:
        f.write(wav_file.content)


def convert_sound() -> str:
    r = sr.Recognizer()
    try:
        with sr.AudioFile('/Users/hwang-eunseog/PycharmProjects/casesCrawler/resource/captchaImg.wav') as f:
            audio_data = r.record(f)
            text = r.recognize_google(audio_data, language='ko-KR')
    except Exception as e:
        print(f'wav 파일을 변환하는 데 이슈가 발생하였습니다.\n{e}')
    return text.replace(' ', '')