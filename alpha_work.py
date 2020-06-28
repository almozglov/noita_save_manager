import os, shutil
from tkinter import *


class Block:
	def __init__(self, master):
		self.b_save = Button(master, text='Save')
		self.b_load = Button(master, text='loadgame')
		self.text_label = Label(master, bg='black', fg='white', width=40)

		self.b_save.bind('<Button-1>', self.savegame)
		self.b_load.bind('<Button-1>', self.loadgame)

		self.text_label.pack()
		self.b_save.pack()
		self.b_load.pack()

	def to_label(self, text):
		main_block.text_label['text'] = text
	
	def savegame(self, event):
		global path, deskpath

		if os.path.exists(path):
			os.chdir(path)
			save = os.listdir()
			filenames = []
			for n in save:
				if '.salakieli' in n:
					filenames.append(n)
			if os.path.exists(deskpath):
				for i in filenames:
					fpath = path+'\\' + i
					dpath = deskpath + '\\' + i
					shutil.copyfile(fpath, dpath)
					self.to_label('Save OK')
			else:		
				os.mkdir(deskpath, mode=0o777)
		else:
			self.to_label("Can't find Noita directory")

	def loadgame(self, event):
		global path, deskpath
		if os.path.exists(deskpath):
			os.chdir(deskpath)
			save = os.listdir()
			filenames = []
			for n in save:
				if '.salakieli' in n:
					filenames.append(n)
			if len(filenames) < 3:
				self.to_label("Error, some files are missing!")
				return None
			if os.path.exists(path):
				for i in filenames:
					fpath = deskpath+'\\' + i
					dpath = path + '\\' + i
					shutil.copyfile(fpath, dpath)
					self.to_label('Load OK')
		else:
			self.to_label("Error, can't find save's folder")




uname = os.getlogin()
path = 'C:\\Users\\{0}\\AppData\\LocalLow\\Nolla_Games_Noita\\save00'.format(uname)
deskpath = 'C:\\Users\\{0}\\Desktop\\noitasaves'.format(uname)

root = Tk()

main_block = Block(root)
'''
text_label = Label(bg='black', fg='white', width=40)
b_save = Button(text='Сохранить')
b_load = Button(text='Загрузить')

b_save.bind('<Button-1>', savegame)
b_load.bind('<Button-1>', loadgame)

text_label.pack()
b_save.pack()
b_load.pack()
'''
root.mainloop()