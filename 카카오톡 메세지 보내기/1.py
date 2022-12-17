import requests
import json

# 카카오톡 메시지 API
url = "https://kauth.kakao.com/oauth/token"
data = {
    "grant_type" : "authorization_code",
    "client_id" : "e42eeafab393c128853e35ad7993dfd3",
    "redirect_url" : "https://localhost:3000",
    "code" : "gTuHO0EHyiIFR-eRtkspxkabbQbKbX5AoPbZX5eVaRbHVOKUYkldzLJ-JXoPEaODUkd-4worDR8AAAGFHjjQIw"
}
response = requests.post(url, data=data)
tokens = response.json()
print(tokens)

# kakao_code.json 파일 저장
with open("kakao_code.json", "w") as fp:
    json.dump(tokens, fp)