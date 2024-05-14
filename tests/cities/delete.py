import requests

URL = "https://apis.travelrealindia.in/cities/WB020/delete"

# delete City
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtYXgtMTU2IiwiaWQiOjEsInJvbGUiOiJhZG1pbiJ9.N8ss1Jlmo5Z-rflXo33ChRn4iHIcMEn7FUVmWRtCSBA"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.delete(url=URL, headers=headers)
print(resp.text)

#Response
"""
{
    "message": "City with code 'WB020' deleted"
}
"""