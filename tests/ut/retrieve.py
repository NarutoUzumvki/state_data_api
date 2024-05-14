import requests

URL = "https://apis.travelrealindia.in/ut/PY/retrieve"

# retrieve ut
payload = {
    "api_key": "I2s-BSNKKLFlE5TTtJUXew8epF-Clhvx"
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