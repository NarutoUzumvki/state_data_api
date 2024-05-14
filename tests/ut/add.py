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

auth_token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJtdC0xNSIsImlkIjoyNSwicm9sZSI6Imd1ZXN0IiwiZXhwIjoxNzA3MTE3NDgyfQ.jCI4tLJBYqAAIFH_bx-ExbTCNGeNlhGRmoknuvXiGS8"

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