import requests

URL = "https://apis.travelrealindia.in/users/create"

# creating a user
payload = {
    "username": "Richard",
    "password": "R1chie12",
    "confirm_password": "R1chie12"
}

resp = requests.post(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "api_key": "I2s-BSNKKLFlE5TTtJUXew8epF-Clhvx",
    "role": "user",
    "username": "R1chie12"
}
"""