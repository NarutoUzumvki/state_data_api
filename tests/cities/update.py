import requests

URL = "https://apis.travelrealindia.in/cities/WB020/update"

# update city
payload = {
    "name": "Siliguri",
    "state_code": "WB",
    "code": "WB020"
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
    "name": "Siliguri",
    "state_code": "WB",
    "code": "WB020"
}
"""