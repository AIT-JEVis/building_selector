from __future__ import print_function

import requests
from requests.exceptions import ConnectionError
from requests.auth import HTTPBasicAuth

auth=HTTPBasicAuth("Sys Admin", "jevis")
SERVER = "http://localhost:8080/JEWebService/v1"
filename = 'content.txt'
files = {'file': (filename, open(filename, 'rb'))}
just_file = {'file': open(filename, 'rb')}

url = SERVER + '/objects/1602/attributes/gbXML File/samples/Files'

r = requests.post(url, files=just_file, auth=auth)
print(r.status_code)
print(r.text)
print(r.headers)