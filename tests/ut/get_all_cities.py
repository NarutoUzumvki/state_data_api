import requests

URL = "https://apis.travelrealindia.in/ut/PY/retrieve/all/cities"

# retrieve all cities from ut
payload = {
    "api_key": "I2s-BSNKKLFlE5TTtJUXew8epF-Clhvx"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
[
    {
        "code": "PY001",
        "name": "Karaikal"
    },
    {
        "code": "PY002",
        "name": "Mahe"
    },
    {
        "code": "PY003",
        "name": "Puducherry"
    },
    {
        "code": "PY004",
        "name": "Yanam"
    }
]"""