import requests

URL = "https://apis.travelrealindia.in/states/KA/update"

# update state
payload = {
    "name": "Karnataka",
    "code": "KA",
    "capital": "Bengaluru",
    "description": "Karnataka, located in southwest India, is renowned for its rich cultural heritage, historic landmarks, and economic dynamism. With Bengaluru as its bustling capital, the state boasts a diverse landscape, encompassing the Western Ghats and a vibrant coastline. Karnataka is a key player in India's IT and biotechnology sectors, driving economic growth",
    "chief_minister": "Basavaraj Bommai",
    "area": "191,791",
    "population": "67,738,364"
}

auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdC0xNSIsImlkIjoyNSwicm9sZSI6Imd1ZXN0IiwiZXhwIjoxNzA3MTE3NDgyfQ.jCI4tLJBYqAAIFH_bx-ExbTCNGeNlhGRmoknuvXiGS8"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.put(url=URL, json=payload, headers=headers)
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