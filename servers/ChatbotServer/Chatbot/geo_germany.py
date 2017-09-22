
import urllib2,json


def adress_getter(zip_code):
    data_dic ={}
    zip_code_pad = str(zip_code).zfill(5)
    url = "http://maps.googleapis.com/maps/api/geocode/json?address="+zip_code_pad+"&&components=country:DE"
    response = urllib2.urlopen(url)
    data = json.loads(response.read())

    data_polished = data[u'results'][0][u'formatted_address'].split()
    data_dic["zip_code"] = zip_code
    data_dic["city"] = data_polished[1]
    data_dic["country"] = data_polished[2]
    return data_dic

print adress_getter(67663)

