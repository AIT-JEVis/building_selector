from __future__ import print_function
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

class Selector:

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

	def __init__(self):
		self.root = Tk()
		self.root.title("Select Building")

		self.con = JEVisConnector("http://localhost:8080/JEWebService/v1", "Sys Admin", "jevis")
		if self.con.isConnected() == FALSE:
			print("Cannot connect to JEVis WebService. status: ", self.con.getStatusCode())
			print(self.con.getLastRequest().json())
			exit(1)

		# setup GUI
		self.l = Listbox(self.root, height=5)
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
			self.l.insert('end', "{} | {}".format(b['id'], unicodedata.normalize('NFKD', b['name']).encode('ascii','ignore')) )
			self.ids.append(b['id'])
			print(b['id'])

		print(self.ids)
		self.b = ttk.Button(self.root, text="OK", command=self.btn_ok_click)
		self.b.grid(column=0,row=2)
		self.root.mainloop()

BuildingSelector = Selector()
print("Finished")
