from __future__ import print_function
# use cross tkinter cross python versions
try:
	import tkinter as tk
	from tkinter import ttk
except ImportError:
	import Tkinter as tk # for python version < 3.0
	import ttk

import os
try:
	import configparser
except ImportError:
	import ConfigParser as configparser


class JEVisWebServiceLogin:
	login_file = "login.conf"
	section_name = "JEVis"
	server = ("")
	username = ("")
	password = ("")
	
	def __init__(self):
		self.init_GUI()
		self.read_from_config(self.login_file)
		self.window.mainloop()
		
	def grid_config(self, entry, column, row):
		entry.grid(column=column, row=row, padx=10, pady=10, sticky='nsew')
		
	def read_from_config(self, login_file):
		if not os.path.isfile(login_file):
			print("No login-file named: ", self.login_file)
			return
		
		config = configparser.ConfigParser()
		config.read(login_file)
		if not config.has_section(self.section_name):
			print("Login-file has no section named: ", self.section_name)
			return
		
		# read items into variables
		self.server = config.get(self.section_name, 'server')
		self.username = config.get(self.section_name, 'username')
		self.password = config.get(self.section_name, 'password')
		
		self.update_entries()
		
	def write_to_config(self, login_file):
		config = configparser.ConfigParser()
		config.add_section(self.section_name)
		config.set(self.section_name, 'server', self.server)
		config.set(self.section_name, 'username', self.username)
		config.set(self.section_name, 'password', self.password)
	
		config.write(open(login_file, 'w'))
	
	def btn_OK_click(self):
		self.read_from_config(self.login_file)
		import sys
		sys.stdout.flush()
		self.update_entries()
	
	def btn_write_click(self):
		self.update_vars()
		self.write_to_config(self.login_file)
		import sys
		sys.stdout.flush()
		
	def init_GUI(self):
		self.window = tk.Tk()
		self.window.title("JEVis Webservice Login")
		
		# row counter
		row = 0
		
		# create labels and entry fields
		server_text = ttk.Label(self.window, text="Server:")
		server_info = ttk.Label(self.window,
						  text="for example 'http://localhost:8080/JEWebService/v1'")
		self.server_entry = ttk.Entry(self.window, width=50)
		
		self.grid_config(server_text, column=0, row=row)
		self.grid_config(self.server_entry, column=1, row=row)
		row +=1
		self.grid_config(server_info, column=1, row=row)
		row +=1
		
		username_text = ttk.Label(self.window, text="Username:")
		self.username_entry = ttk.Entry(self.window)
		self.grid_config(username_text,       column=0, row=row)
		self.grid_config(self.username_entry, column=1, row=row)
		row +=1
		
		password_text = ttk.Label(self.window, text="Password:")
		self.password_entry = ttk.Entry(self.window, show="*")
		self.grid_config(password_text,       column=0, row=row)
		self.grid_config(self.password_entry, column=1, row=row)
		row +=1
		
		# create buttons
		btn_OK = ttk.Button(self.window, text="OK", command=self.btn_OK_click)
		btn_OK.grid(column=1,row=row, padx=10, pady=10, sticky='nw')
		btn_OK = ttk.Button(self.window, text="Write", command=self.btn_write_click)
		btn_OK.grid(column=0,row=row, padx=10, pady=10, sticky='nw')
		
		self.password_entry.bind('<Return>', self.btn_OK_click)
		
		# properly resize window
		ttk.Sizegrip().grid(column=1, row=row, sticky='se')
		self.window.columnconfigure(1, weight=1)
		self.window.rowconfigure(row, weight=1)

	def update_vars(self):
		self.server = self.server_entry.get()
		self.username = self.username_entry.get()
		self.password = self.password_entry.get()
	
	def update_entries(self):
		self.server_entry.delete(0, last=tk.END)
		self.username_entry.delete(0, last=tk.END)
		self.password_entry.delete(0, last=tk.END)
	
		self.server_entry.insert(0, self.server)
		self.username_entry.insert(0, self.username)
		self.password_entry.insert(0, self.password)

if __name__ == '__main__':
	login = JEVisWebServiceLogin()