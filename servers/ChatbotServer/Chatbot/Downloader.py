import urllib.request


def download(attachment):
    url, filename, mimetype = attachment["url"], attachment["fileName"], attachment["mimeType"]
    data = None
    try:
        response = urllib.request.urlopen(url)
        data = response.read()
    except:
        print("Could not download attachment")
    return data