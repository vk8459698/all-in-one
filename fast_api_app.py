from fastapi import FastAPI, File, UploadFile
from allin1 import analyze
import tempfile
import os
import json

app = FastAPI()


@app.post("/analyze/")
async def analyze_audio(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav:
        temp_wav.write(await file.read())
        temp_wav_path = temp_wav.name

    result = analyze(temp_wav_path)

    os.remove(temp_wav_path)
    return result
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("fast_api_app:app", host="0.0.0.0", port=8000, reload=True)
