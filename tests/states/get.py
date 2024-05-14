import requests

URL = "https://apis.travelrealindia.in/states/KA/retrieve"

# retrieve state
payload = {
    "api_key": "I2s-BSNKKLFlE5TTtJUXew8epF-Clhvx"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "code": "KA",
    "name": "Karnataka",
    "capital": "Bengaluru",
    "description": "Karnataka, located in southwest India, is renowned for its rich cultural heritage, historic landmarks, and economic dynamism. With Bengaluru as its bustling capital, the state boasts a diverse landscape, encompassing the Western Ghats and a vibrant coastline. Karnataka is a key player in India's IT and biotechnology sectors, driving economic growth",
    "chief_minister": "Basavaraj Bommai",
    "area": "191,791",
    "population": "67,738,364"
}
"""