import requests

def address_getter(zip_code):
    zip_code_pad = str(zip_code).zfill(5)
    url = "http://maps.googleapis.com/maps/api/geocode/json?address="+zip_code_pad+"&&components=country:DE"
    response = requests.get(url)
    data = response.json()
    components = data["results"][0]["address_components"]
    city, country = None, None
    for component in components:
        if "country" in component["types"]:
            country = component["long_name"]
        if "locality" in component["types"]:
            city = component["long_name"]
    return city, country