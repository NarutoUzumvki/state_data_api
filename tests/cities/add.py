import requests

URL = "https://apis.travelrealindia.in/cities/create"

# add city
payload = {
    "name": "Siligudi",
    "state_code": "WB"
}

auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdC0xNSIsImlkIjoyNSwicm9sZSI6Imd1ZXN0IiwiZXhwIjoxNzA3MTE3NDgyfQ.jCI4tLJBYqAAIFH_bx-ExbTCNGeNlhGRmoknuvXiGS8"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.post(url=URL, json=payload, headers=headers)
print(resp.text)

#Response
"""
{
    "name": "Siligudi",
    "state_code": "WB",
    "code": "WB020"
}
"""