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

# download latest file, saved with the saved filename
f = con.getLatestFile('1710', 'gbXML File')
print(f['name'])

# or give a third parameter to define the filename yourself
#f = con.getLatestFile('1710', 'gbXML File', 'newfile.xml')



