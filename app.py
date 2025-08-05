import requests

url = "http://localhost:8000/analyze/"
files = {"file": open("41918_song.wav", "rb")}
response = requests.post(url, files=files)

print(response.json())
