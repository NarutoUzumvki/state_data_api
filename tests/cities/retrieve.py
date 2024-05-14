import requests

URL = "https://apis.travelrealindia.in/city/WB020/retrieve"

# retrieve city
payload = {
    "api_key":"I2s-BSNKKLFlE5TTtJUXew8epF-Clhvx"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "name": "Siliguri",
    "state_code": "WB",
    "code": "WB020"
}
"""