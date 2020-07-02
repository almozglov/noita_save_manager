import os, shutil
from window_builder import *

version = 'NoitaSavesManager v2.07.20'

#Сохранения (выбор что сохранить) на папки и имена для сейвов


class Window:
	
	def to_label(self, text):
		print(type(self))
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


def check_saves(window, path):
	print(path)
	if os.path.exists(path):
		return True
	else:
		window.to_label('Не могу найти папку Ноиты')


uname = os.getlogin()
#uname = 'alexander'
path = 'C:\\Users\\{0}\\AppData\\LocalLow\\Nolla_Games_Noita\\save00'.format(uname)
deskpath = 'C:\\Users\\{0}\\Desktop\\noitasaves'.format(uname)

root = Tk()

main_block = Window(root)

root.mainloop()