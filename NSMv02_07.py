import os, shutil
from tkinter import *

version = 'NoitaSavesManager v2.07.20'


class Window:
	def __init__(self, master):
		build_window(self, master, version)
		check_saves(self, path)

	def to_label(self, text):
		self.text_label['text'] = text
	
	def savegame(self, event):
		global path, deskpath
		if check_saves(self, path):
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
					self.to_label('Game Saved')
			else:		
				os.mkdir(deskpath, mode=0o777)

	def loadgame(self, event):
		global path, deskpath
		if check_saves(self, deskpath):
			os.chdir(deskpath)
			save = os.listdir()
			filenames = []
			for n in save:
				if '.salakieli' in n:
					filenames.append(n)
			if len(filenames) < 3:
				self.to_label("Ошибка. Файлы повреждены или утеряны")
				return None
			if os.path.exists(path):
				for i in filenames:
					fpath = deskpath+'\\' + i
					dpath = path + '\\' + i
					shutil.copyfile(fpath, dpath)
					self.to_label('Game loaded')

	def confirm(self):
		con_win = Window(root)

def build_window(window, root, name):
	root.title(name)
	#master.geometry("300x150")
	centerframe = Frame(root)
	rightframe = Frame(root)
	leftframe = Frame(root)
	centerframe.pack()

	rightframe.pack(side=RIGHT)
	leftframe.pack(side=LEFT)

	window.b_save = Button(rightframe, text='Save')
	window.b_load = Button(rightframe, text='Load')
	window.text_label = Label(centerframe, bg='black', fg='white', width=40, pady=10, relief='sunken')

	window.b_save.bind('<Button-1>', window.savegame)
	window.b_load.bind('<Button-1>', window.loadgame)

	window.text_label.pack()
	window.b_save.pack(padx = 5, pady = 5)
	window.b_load.pack(padx = 5, pady = 5)


def check_saves(window, path):
	if os.path.exists(path):
		return True
	else:
		window.to_label('Не могу найти папку Ноиты')


#uname = os.getlogin()
uname = 'alexander'
path = 'C:\\Users\\{0}\\AppData\\LocalLow\\Nolla_Games_Noita\\save00'.format(uname)
deskpath = 'C:\\Users\\{0}\\Desktop\\noitasaves'.format(uname)

root = Tk()

main_block = Window(root)

root.mainloop()