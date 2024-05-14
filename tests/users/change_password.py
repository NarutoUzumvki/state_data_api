import requests

URL = "https://apis.travelrealindia.in/users/change/password"

# change password
payload = {
    "username":"Richard",
    "old_password":"Richie12",
    "new_password":"Richie13",
    "confirm_password":"Richie13"
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
    "message": "Password updated successfully"
}
"""
