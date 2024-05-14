import requests

URL = "https://apis.travelrealindia.in/states/KA/retrieve/all/cities"

# retrieve all cities from state
payload = {
    "api_key": "I2s-BSNKKLFlE5TTtJUXew8epF-Clhvx"
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