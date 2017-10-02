import requests

class EntityExtractor:
    def extractFromText(self, message, entities, currentEntity):
        pass

    def extractFromImage(self, attachment, emptyEntities, currentEntity):
        extractedEntities = dict()
        extractedEntities["name"] = (Match("name", "Marc"))
        extractedEntities["street"] = (Match("street", "Burggrafenstr.", 1))
        extractedEntities["streetnumber"] = (Match("streetnumber", "61", 1))
        extractedEntities["zip"] = (Match("zip", "10787", 1))
        extractedEntities["city"] = (Match("city", "Berlin", 1))
        extractedEntities["country"] = (Match("country", "Deutschland", 1))
        extractedEntities["date"] = (Match("date", None, 1))
        extractedEntities["area"] = (Match("area", "67", 1))
        extractedEntities["price"] = (Match("price", "499.99€", 1))
        extractedEntities["invoiceDate"] = (Match("invoiceDate", "499.99€", 1))
        return self.postExtract(extractedEntities, emptyEntities)

    def postExtract(self, extractedEntities, emptyEntities):
        if "zip" in extractedEntities:
            if "city" not in extractedEntities or "country" not in extractedEntities:
                city, country = self.address_getter(extractedEntities["zip"].value)
                if "city" not in extractedEntities and city:
                    extractedEntities["city"] = Match("city", city)
                if "country" not in extractedEntities and country:
                    extractedEntities["country"] = Match("country", country)
        return [match for match in extractedEntities.values() if match.name in emptyEntities]

    def address_getter(self, zip_code):
        print("zip code extractor")
        zip_code_pad = str(zip_code).zfill(5)
        url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + zip_code_pad + "&&components=country:DE"
        response = requests.get(url)
        data = response.json()
        if len(data["results"]) == 0:
            return None, None
        components = data["results"][0]["address_components"]
        city, country = None, None
        for component in components:
            if "country" in component["types"]:
                country = component["long_name"]
            if "locality" in component["types"]:
                city = component["long_name"]
        return city, country


class Match():
    def __init__(self, name, value, confidence=None):
        self.name = name
        self.value = value
        self.confidence = confidence