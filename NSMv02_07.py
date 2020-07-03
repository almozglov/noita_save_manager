import os, shutil
from tkinter import *
from window_builder import BuildWindow

version = 'NoitaSavesManager v3.07.20'

#Сохранения (выбор что сохранить) на папки и имена для сейвов

class Window(BuildWindow):

	def raise_confirm(self):
		w = Tk()
		Window(w, 'confirm')

	def raise_confirm_save(self):
		w = Tk()
		Window(w, 'save',)

	def finish_build(self):
		self.check_saves()
		self.b_save = self.build_buttons(buttons={'Save': ['right', self.raise_confirm_save]})
		self.b_load = self.build_buttons(buttons = {'Load': ['right', self.raise_confirm]})
		for i in os.listdir(self.deskpath):
			self.add_to_list(i)


	def build_confirm_window(self, master):
		conf_msg = 'Вы уверены, что хотите загрузить\n сохранённую игру?'
		self.build_frame(master, 'Confirm')
		self.build_label({'confirmlabel': ['center', None, None, 10, [0, 20]]}, conf_msg)
		self.build_buttons(buttons = {'Ok': ['center', self.load_confirm_ok], 'Cancel': ['center', self.confirm_cancel]})
	
	def build_save_window(self, master):
		conf_msg = 'Введите имя сохранения'
		self.build_frame(master, 'Confirm')
		self.build_label({'confirmlabel': ['center', None, None, 10, [0, 20]]}, conf_msg)
		self.build_entry()
		#self.build_buttons(buttons = {'Ok': ['center', self.load_confirm_ok], 'Cancel': ['center', self.load_confirm_cancel]})
		self.build_buttons(buttons = {'Ok': ['center', self.save_confirm_ok], 'Cancel': ['center', self.confirm_cancel]})

	def to_label(self, text):
		self.label['text'] = text
	
	def savegame(self, name):
		self.add_to_list(name)
		if self.check_saves():
			os.chdir(self.path)
			save = os.listdir()
			filenames = []
			for n in save:
				if '.salakieli' in n:
					filenames.append(n)
			if os.path.exists(self.deskpath +  '\\' + name):
				for i in filenames:
					fpath = self.path+'\\' + i
					dpath = self.deskpath + '\\' + name +  '\\' + i
					shutil.copyfile(fpath, dpath)
					self.to_label('Game Saved')
			else:		
				os.mkdir(self.deskpath +  '\\' + name, mode=0o777)

	def loadgame(self):
		savename = self.listbox.get(self.listbox.curselection()[0])
		print(savename)
		if self.check_saves():
			os.chdir(self.deskpath)
			save = os.listdir()
			filenames = []
			for n in save:
				if '.salakieli' in n:
					filenames.append(n)
			if len(filenames) < 3:
				self.to_label("Ошибка. Файлы повреждены или утеряны")
				return None
			#if os.path.exists(self.path):
			for i in filenames:
				fpath = self.deskpath+'\\' + i
				dpath = self.path + '\\' + i
				shutil.copyfile(fpath, dpath)
				self.to_label('Game loaded')

	def save_confirm_ok(self):
		main_block.savegame(self.entry.get())
		self.root.destroy()

	def load_confirm_ok(self):
		print("ok")
		self.root.destroy()
		main_block.loadgame()

	def confirm_cancel(self):
		self.root.destroy()

	def check_saves(self):
		if os.path.exists(self.path):
			return True
		else:
			self.to_label('Не могу найти папку Ноиты')


#uname = os.getlogin()
uname = 'alexander'
path = 'C:\\Users\\{0}\\AppData\\LocalLow\\Nolla_Games_Noita\\save00'.format(uname)
deskpath = 'C:\\Users\\{0}\\Desktop\\noitasaves'.format(uname)

root = Tk()

main_block = Window(root, 'main', path, deskpath)
main_block.finish_build()
root.mainloop()