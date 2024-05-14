# State Data API:  [https://apis.travelrealindia.in](https://apis.travelrealindia.in)
The StateDataAPI is a set of robust APIs built on
the Flask framework that serves as a centralized platform to
access information related to States, Union Territories and
Cities of India.


## Usage

### Create New User
#### Endpoint: https://apis.travelrealindia.in/users/create
```python
import requests

URL = "https://apis.travelrealindia.in/users/create"

# creating a user
payload = {
    "username": "new-user-156",
    "password": "notX@443",
    "confirm_password": "notX@443"
}

resp = requests.post(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "api_key": <api_key>",
    "role": "user",
    "username": "maxc-1560"
}
"""
```

### Get Auth Token
#### Endpoint: https://apis.travelrealindia.in/auth/token
```python
import requests

URL = "https://apis.travelrealindia.in/auth/token"

# get auth token
payload = {
    "username": "new-user-156",
    "password": "notX@443"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "access_token": <auth_token>,
    "token_type": "Bearer"
}
"""
```

### Change Password
#### Endpoint: https://apis.travelrealindia.in/users/change/password
```python
import requests

URL = "https://apis.travelrealindia.in/users/change/password"

# change password
payload = {
    "username":"new-user-156",
    "old_password":"notX@443",
    "new_password":"notA@443",
    "confirm_password":"notA@443"
}

auth_token = "--------auth_token--------"

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
```

### Add State
#### Endpoint: https://apis.travelrealindia.in/states/create
```python
import requests

URL = "https://apis.travelrealindia.in/states/create"

# add state
payload = {
    "name": "Karnataka",
    "code": "KA",
    "capital": "Bengaluru",
    "description": "Karnataka, located in southwest India, is renowned for its rich cultural heritage, historic landmarks, and economic dynamism. With Bengaluru as its bustling capital, the state boasts a diverse landscape, encompassing the Western Ghats and a vibrant coastline. Karnataka is a key player in India's IT and biotechnology sectors, driving economic growth",
    "chief_minister": "Basavaraj Bommai",
    "area": "191,791",
    "population": "67,738,363"
}

auth_token = "--------auth_token--------"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.post(url=URL, json=payload, headers=headers)
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
    "population": "67,738,363"
}
"""
```

### Update State
#### Endpoint: https://apis.travelrealindia.in/states/<state_code>/update
```python
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

auth_token = "--------auth_token--------"

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
```

### Retrieve State
#### Endpoint: https://apis.travelrealindia.in/states/<state_code>/retrieve
```python
import requests

URL = "https://apis.travelrealindia.in/states/KA/retrieve"

# retrieve state
payload = {
    "api_key": "--------api_key--------"
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
```

### Retrieve all Cities from State
#### Endpoint: https://apis.travelrealindia.in/states/<state_code>/retrieve/all/cities
```python
import requests

URL = "https://apis.travelrealindia.in/states/KA/retrieve/all/cities"

# retrieve all cities from state
payload = {
    "api_key": "--------api_key--------"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
[
    {
        "code": "KA001",
        "name": "Bidar"
    },
    {
        "code": "KA002",
        "name": "Belgaum"
    },
    {
        "code": "KA003",
        "name": "Bijapur"
    },
    {
        "code": "KA004",
        "name": "Bagalkot"
    },
    {
        "code": "KA005",
        "name": "Bellary"
    },
    {
        "code": "KA006",
        "name": "Bangalore Rural District"
    },
    {
        "code": "KA007",
        "name": "Bangalore Urban District"
    },
    {
        "code": "KA008",
        "name": "Chamarajnagar"
    },
    {
        "code": "KA009",
        "name": "Chikmagalur"
    },
    {
        "code": "KA010",
        "name": "Chitradurga"
    },
    {
        "code": "KA011",
        "name": "Davanagere"
    },
    {
        "code": "KA012",
        "name": "Dharwad"
    },
    {
        "code": "KA013",
        "name": "Dakshina Kannada"
    },
    {
        "code": "KA014",
        "name": "Gadag"
    },
    {
        "code": "KA015",
        "name": "Gulbarga"
    },
    {
        "code": "KA016",
        "name": "Hassan"
    },
    {
        "code": "KA017",
        "name": "Haveri District"
    },
    {
        "code": "KA018",
        "name": "Kodagu"
    },
    {
        "code": "KA019",
        "name": "Kolar"
    },
    {
        "code": "KA020",
        "name": "Koppal"
    },
    {
        "code": "KA021",
        "name": "Mandya"
    },
    {
        "code": "KA022",
        "name": "Mysore"
    },
    {
        "code": "KA023",
        "name": "Raichur"
    },
    {
        "code": "KA024",
        "name": "Shimoga"
    },
    {
        "code": "KA025",
        "name": "Tumkur"
    },
    {
        "code": "KA026",
        "name": "Udupi"
    },
    {
        "code": "KA027",
        "name": "Uttara Kannada"
    },
    {
        "code": "KA028",
        "name": "Ramanagara"
    },
    {
        "code": "KA029",
        "name": "Chikballapur"
    },
    {
        "code": "KA030",
        "name": "Yadagiri"
    }
]
"""
```

### Delete State
#### Endpoint: https://apis.travelrealindia.in/states/<state_code>/delete
```python
import requests

URL = "https://apis.travelrealindia.in/states/KA/delete"

# delete state
auth_token = "--------auth_token--------"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.delete(url=URL, headers=headers)
print(resp.text)

#Response
"""
{
    "message": "State with code 'KA' deleted"
}
"""
```

### Add UT
#### Endpoint: https://apis.travelrealindia.in/ut/create
```python
import requests

URL = "https://apis.travelrealindia.in/ut/create"

# add ut
payload = {
    "area": "479",
    "capital": "Pondicherry",
    "chief_minister": "N.Rangaswamy",
    "code": "PY",
    "description": "Pondicherry (or Puducherry), a French colonial settlement in India until 1954, is now a Union Territory town bounded by the southeastern Tamil Nadu state. Its French legacy is preserved in its French Quarter, with tree-lined streets, mustard-colored colonial villas and chic boutiques. A seaside promenade runs along the Bay of Bengal and passes several statues, including a 4m-high Gandhi Memorial.",
    "name": "Puducherry",
    "population": "1,247,953"
}

auth_token = "--------auth_token--------"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.post(url=URL, json=payload, headers=headers)
print(resp.text)

#Response
"""
{
    "area": "479",
    "capital": "Pondicherry",
    "chief_minister": "N.Rangaswamy",
    "code": "PY",
    "description": "Pondicherry (or Puducherry), a French colonial settlement in India until 1954, is now a Union Territory town bounded by the southeastern Tamil Nadu state. Its French legacy is preserved in its French Quarter, with tree-lined streets, mustard-colored colonial villas and chic boutiques. A seaside promenade runs along the Bay of Bengal and passes several statues, including a 4m-high Gandhi Memorial.",
    "name": "Puducherry",
    "population": "1,247,953"
}
"""
```

### Update UT
#### Endpoint: https://apis.travelrealindia.in/ut/<ut_code>/update
```python
import requests

URL = "https://apis.travelrealindia.in/ut/PY/update"

# update ut
payload = {
    "area": "479",
    "capital": "Pondicherry",
    "chief_minister": "N.Rangaswamy",
    "code": "PY",
    "description": "Pondicherry (or Puducherry), a French colonial settlement in India until 1954, is now a Union Territory town bounded by the southeastern Tamil Nadu state. Its French legacy is preserved in its French Quarter, with tree-lined streets, mustard-colored colonial villas and chic boutiques. A seaside promenade runs along the Bay of Bengal and passes several statues, including a 4m-high Gandhi Memorial.",
    "name": "Puducherry",
    "population": "1,247,955"
}

auth_token = "--------auth_token--------"

headers = {
    "Authorization": f'Bearer {auth_token}'
}

resp = requests.put(url=URL, json=payload, headers=headers)
print(resp.text)

#Response
"""
{
    "area": "479",
    "capital": "Pondicherry",
    "chief_minister": "N.Rangaswamy",
    "code": "PY",
    "description": "Pondicherry (or Puducherry), a French colonial settlement in India until 1954, is now a Union Territory town bounded by the southeastern Tamil Nadu state. Its French legacy is preserved in its French Quarter, with tree-lined streets, mustard-colored colonial villas and chic boutiques. A seaside promenade runs along the Bay of Bengal and passes several statues, including a 4m-high Gandhi Memorial.",
    "name": "Puducherry",
    "population": "1,247,955"
}
"""
```

### Retrieve UT
#### Endpoint: https://apis.travelrealindia.in/ut/PY/retrieve
```python
import requests

URL = "https://apis.travelrealindia.in/ut/PY/retrieve"

# retrieve ut
payload = {
    "api_key": "--------api_key--------"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "area": "479",
    "capital": "Pondicherry",
    "chief_minister": "N.Rangaswamy",
    "code": "PY",
    "description": "Pondicherry (or Puducherry), a French colonial settlement in India until 1954, is now a Union Territory town bounded by the southeastern Tamil Nadu state. Its French legacy is preserved in its French Quarter, with tree-lined streets, mustard-colored colonial villas and chic boutiques. A seaside promenade runs along the Bay of Bengal and passes several statues, including a 4m-high Gandhi Memorial.",
    "name": "Puducherry",
    "population": "1,247,955"
}
"""
```

### Retrieve all Cities from UT
#### Endpoint: https://apis.travelrealindia.in/ut/PY/retrieve/all/cities
```python
import requests

URL = "https://apis.travelrealindia.in/ut/PY/retrieve/all/cities"

# retrieve all cities from ut
payload = {
    "api_key": "--------api_key--------"
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
```

### Delete UT
#### Endpoint: https://apis.travelrealindia.in/ut/PY/delete
```python
import requests

URL = "https://apis.travelrealindia.in/ut/PY/delete"

# delete ut
auth_token = "--------auth_token--------"

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
```

### Add City
#### Endpoint: https://apis.travelrealindia.in/cities/create
```python
import requests

URL = "https://apis.travelrealindia.in/cities/create"

# add city
payload = {
    "name": "Siligudi",
    "state_code": "WB"
}

auth_token = "--------auth_token--------"

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
```

### Update City
#### Endpoint: https://apis.travelrealindia.in/cities/WB019/update
```python
import requests

URL = "https://apis.travelrealindia.in/cities/WB020/update"

# update city
payload = {
    "name": "Siliguri",
    "state_code": "WB"
}

auth_token = "--------auth_token--------"

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
```

### Retrieve City
#### Endpoint: https://apis.travelrealindia.in/city/WB019/retrieve
```python
import requests

URL = "https://apis.travelrealindia.in/city/WB020/retrieve"

# retrieve city
payload = {
    "api_key": "--------api_key--------"
}

resp = requests.get(url=URL, json=payload)
print(resp.text)

#Response
"""
{
    "code": "WB019",
    "map_link": "https://www.google.com/maps/search/?api=1&query=Siliguri,+WB",
    "name": "Siliguri",
    "state_code": "WB",
    "weather_forecast": "24.3°C, Feels Like 24.43°C, Clear Sky"
}
"""
```

### Delete City
#### Endpoint: https://apis.travelrealindia.in/cities/WB019/delete
```python
import requests

URL = "https://apis.travelrealindia.in/cities/WB020/delete"

# delete City
auth_token = "--------auth_token--------"

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
```

## Contributing

Pull requests are welcome. For major changes, please open an issue first
to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License

[MIT](https://choosealicense.com/licenses/mit/)
