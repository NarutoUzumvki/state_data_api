import requests

URL = "https://apis.travelrealindia.in/ut/PY/delete"

# delete ut
auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdC0xNSIsImlkIjoyNSwicm9sZSI6Imd1ZXN0IiwiZXhwIjoxNzA3MTE3NDgyfQ.jCI4tLJBYqAAIFH_bx-ExbTCNGeNlhGRmoknuvXiGS8"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.delete(url=URL, headers=headers)
print(resp.text)

#Response
"""
{
    "message": "UT with code 'PY' deleted"
}
"""