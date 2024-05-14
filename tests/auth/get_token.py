import requests

URL = "https://apis.travelrealindia.in/auth/token"

# get auth token
payload = {
    "username": "Richard",
    "password": "R1chie12"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYXgtMTU2IiwiaWQiOjEsInJvbGUiOiJhZG1pbiJ9.N8ss1Jlmo5Z-rflXo33ChRn4iHIcMEn7FUVmWRtCSBA",
    "token_type": "Bearer"
}
"""