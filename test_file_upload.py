from __future__ import print_function
from __future__ import unicode_literals

from jevis_api import JEVisConnector

SERVER = "http://localhost:8080/JEWebService/v1"
USER = 'AIT'
PASSWORD = 'jevis'

con = JEVisConnector(SERVER, USER, PASSWORD)
if not con.isConnected():
	print("Cannot connect to JEVis WebService. status: ", con.getStatusCode())
	exit(1)

filename = "OfficeBuilding.xml"

# upload the file given by filepath
r = con.uploadFile('1710', 'gbXML File', filename)
# or give a third parameter to define the filename yourself
#r = con.uploadFile('1710', 'gbXML File', filename, 'newfile.xml')
print(r.status_code)
print(r.text)
print(r.headers)

