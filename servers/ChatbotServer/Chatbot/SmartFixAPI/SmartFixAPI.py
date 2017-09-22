import json
import os
from urllib import request, error

from MultiPartForm import MultiPartForm


class SmartFixAPI:
    base_host = "poc-api-test.insiders.cloud/1/rest/"
    request_token_endpoint = 'https://' + base_host + 'accounts/authentication/requesttoken'
    analyse_endpoint = 'https://' + base_host + 'tasks/analyse'

    def __init__(self, config_file):
        with open(config_file) as f:
            config = json.loads(f.read())

        username = config['username']
        password = config['password']
        token_data = config['token_data'] if 'token_data' in config else None

        self.token, self.token_valid_until = self.request_token(username, password) if not token_data else \
            (token_data['token'], token_data['validUntil'])

    def request_token(self, username, password):
        data = {'username': username, 'password': password}
        req = request.Request(self.request_token_endpoint)
        req.add_header('Content-Type', 'application/json')

        with request.urlopen(req, json.dumps(data).encode('utf-8')) as response:
            answer = json.loads(response.read().decode("utf-8"))

        return answer['token'], answer['validUntil']

    def analyse(self, image_paths, subsystem, category):
        form = MultiPartForm()
        files = []
        for image_path in image_paths:
            with open(image_path, 'rb') as f:
                filename = os.path.basename(f.name)
                filename_without_ext = os.path.splitext(filename)[0]
                files.append({'fileData': filename, 'id': filename_without_ext})  # need only fileData
                form.add_file(fieldname=filename, filename=f.name, fileHandle=f)

        parameters = dict()
        parameters['files'] = files
        parameters['subsystem'] = subsystem
        parameters['category'] = category
        form.add_field('task-meta-data', repr(parameters))
        data = bytes(form)  # Build the request, including the byte-string for the data to be posted.

        bearerToken = 'Bearer ' + self.token
        req = request.Request(self.analyse_endpoint, data=data)

        req.add_header('Content-Type', form.get_content_type())
        req.add_header('Content-length', len(data))
        req.add_header('Authorization', bearerToken)

        try:
            answer = request.urlopen(req).read().decode('utf-8')
        except error.HTTPError as e:
            print(e.code)
            print(e.read().decode("utf-8"))
            raise e

        return json.loads(answer)

    def analyse_images(self, image_paths):
        response = sfAPI.analyse(image_paths, 'ChatBotDemo', 'RentalContract')

        results = dict()
        for document in response['data']['processes'][0]['documents']:
            doc_id = document['id']
            fields = {field['name']: field['value'] for field in document['fields']}

            street, city_with_zip = fields['Address'].split(',')
            zip_code, city = city_with_zip.split()
            del fields['Address']
            fields['Street'] = street
            fields['ZipCode'] = zip_code
            fields['City'] = city

            results[doc_id] = fields

        return results


if __name__ == "__main__":
    sfAPI = SmartFixAPI('sf_api_config.json')
    image_paths = [r'../../Demo/Example Contracts/Example1.jpg']
    results = sfAPI.analyse_images(image_paths)
    print(results)
