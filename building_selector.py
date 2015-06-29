from __future__ import print_function
from __future__ import unicode_literals

# use cross tkinter cross python versions
try:
    from tkinter import *
    from tkinter import ttk
except ImportError:
    from Tkinter import * # for python version < 3.0
    import ttk
import base64
import unicodedata
from jevis_api import JEVisConnector
from login_gui import JEVisWebServiceLogin

class Selector:

	list_height=15
	
	def btn_ok_click(self):
		items = self.l.curselection()
		if len(items) == 0:
			print("Nothing selected")
		elif len(items) == 1:
			sel = int(items[0])
			id = self.ids[int(sel)]
			print("Selected: ", sel, "=", id)
			self.getgbXML(id)
		else:
			print("More than one selected")

	def getgbXML(self, id):
		f = self.con.getLatestFile(id, 'gbXML File')
		
	def get_login_credentials(self):
		self.login_gui = JEVisWebServiceLogin()
		if not self.login_gui.is_connected():
			print("Error: No valid login provided.")
			exit(1)
		
		self.credentials = self.login_gui.get_login_credentials()

	def __init__(self):
		self.get_login_credentials()
		
		self.root = Tk()
		self.root.title("Select Building")

		self.con = JEVisConnector(self.credentials['server'],
							self.credentials['username'], self.credentials['password'])
		if not self.con.isConnected():
			print("Cannot connect to JEVis WebService. status: ", self.con.getStatusCode())
			exit(1)

		# setup GUI
		self.l = Listbox(self.root, height=self.list_height)
		self.l.grid(column=0, row=0, sticky=(N,W,E,S))
		self.s = ttk.Scrollbar(self.root, orient=VERTICAL, command=self.l.yview)
		self.s.grid(column=1, row=0, sticky=(N,S))
		self.l['yscrollcommand'] = self.s.set
		ttk.Sizegrip().grid(column=1, row=2, sticky=(S,E))
		self.root.grid_columnconfigure(0, weight=1)
		self.root.grid_rowconfigure(0, weight=1)

		buildings = self.con.getClassObjects("Green Building")

		# workaround if only one green building
		if 'id' in buildings['Object']:
			buildings['Object'] = [buildings['Object']]
			print("Workaround!")

		self.ids = []
		for b in buildings['Object']:
			id = b['id']
			from builtins import str
			val_cleaned = unicodedata.normalize('NFKD', b['name']).encode('ascii','ignore')
			val = val_cleaned.decode()
			print(id,"|", val_cleaned, "|", val)
			self.l.insert('end', "{} | {}".format(id, val) )
			self.ids.append(id)

		print(self.ids)
		self.b = ttk.Button(self.root, text="OK", command=self.btn_ok_click)
		self.b.grid(column=0,row=2)
		self.root.mainloop()

BuildingSelector = Selector()
print("Finished")
