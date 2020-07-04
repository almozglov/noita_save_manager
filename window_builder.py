import os, shutil
from tkinter import *
 
version = 'NoitaSavesManager v4.07.20'

class BuildWindow:
	def __init__(self, master, name, path=None, deskpath = None):
		self.root = master
		self.path = path
		self.deskpath = deskpath
		self.name = name
		if name == 'main':
			self.build_main_window(master, version)
		if name == 'confirm':
			self.build_confirm_window(master)
		if name == 'save':
			self.build_save_window(master)

	def __str__(self):
		return self.name

	def build_main_window(self, master, name):
		msg_main = 'Список сохранений'
		self.build_frame(master, name)
		self.build_label(labels={'mainLabel': ['center',None, None, 40, [0, 10]]}, text = msg_main)
		#self.build_label(labels={'mainLabel': ['left',None, None, 40, [0, 10]]}, text = msg_info)
		self.build_list()
		
	def build_frame(self, master, name):
		master.title(name)
		if self.name == 'main':
			master.geometry("500x300")
		self.centerframe = Frame(master)
		self.rightframe = Frame(master)
		self.leftframe = Frame(master)
		self.centerframe.pack()

		self.rightframe.pack(side='right')
		self.leftframe.pack(side='left')

	def build_list(self):
		self.listbox = Listbox(self.centerframe, width = 80)
		self.listbox.pack()

	def build_label(self, labels, text=None):
		for i in labels:
			if labels[i][0] == 'right':
				self.label = Label(self.rightframe, bg=labels[i][1] , fg=labels[i][2], width=40, pady=10, )
			if labels[i][0] == 'left':
				self.label = Label(self.leftframe, bg=labels[i][1], fg=labels[i][2], width=40, pady=10, )
			if labels[i][0] == 'center':
				self.label = Label(self.centerframe,bg=labels[i][1], fg=labels[i][2], width=40, pady=10, )
			self.label['text'] = text
			self.label.pack()

	def build_buttons(self, buttons):
		for i in buttons:
			if buttons[i][0] == 'right':
				button = Button(self.rightframe, text=i, command = buttons[i][1], width=10)
			if buttons[i][0] == 'left':
				b_save = Button(self.leftframe, text=i, command = buttons[i][1], width=10)
			if buttons[i][0] == 'center':
				button = Button(self.centerframe, text = i, command = buttons[i][1], width=10)
			button.pack(padx = 5, pady = 2)
		return button

	def add_to_list(self, item_name, num=0):
		if num==0:
			num = len(self.listbox.get(0 , END))+1
		self.listbox.insert(num, item_name)

	def build_entry(self, text=None):
		self.entry = Entry(self.centerframe, width=20)
		self.entry.pack()
