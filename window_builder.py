from tkinter import *
 
class BuildWindow:
	def __init__(self, master, name):
		self.root = master
		if name == 'main':
			self.build_main_window(master, name)
		if name == 'confirm':
			self.build_confirm_window(master)

	def build_main_window(self, master, name):
		self.build_frame(master, name)
		self.build_label(labels={'mainLabel': ['center', 'black', 'white', 40, [0, 10]]})
		self.build_buttons(buttons={'Save': ['right', None], 'Load': ['right', self.func]})
		
	def build_confirm_window(self, master):
		conf_msg = 'Вы уверены, что хотите загрузить сохранённую игру?'
		self.build_frame(master, 'Confirm')
		self.build_label({'confirmlabel': ['center', None, None, 10, [0, 20]]}, conf_msg)
		self.build_buttons(buttons = {'Ok': ['center', self.ok], 'Cancel': ['center', self.neok]})
	
	def build_frame(self, master, name):
		master.title(name)
		#master.geometry("300x150")
		self.centerframe = Frame(master)
		self.rightframe = Frame(master)
		self.leftframe = Frame(master)
		self.centerframe.pack()

		self.rightframe.pack(side='right')
		self.leftframe.pack(side='left')

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
				button = Button(self.rightframe, text=i, command = buttons[i][1])
			if buttons[i][0] == 'left':
				b_save = Button(self.leftframe, text=i, command = buttons[i][1])
			if buttons[i][0] == 'center':
				button = Button(self.centerframe, text = i, command = buttons[i][1])
			button.pack(padx = 5, pady = 5)


	def func(self):
		w = Tk()
		BuildWindow(w, 'confirm')

	def ok(self):
		print("ok")
		self.root.destroy()

	def neok(self):
		print("neok")
		self.root.destroy()

class Test(BuildWindow):
	def check_saves(self, path):
		print(path)
		if os.path.exists(path):
			return True
		else:
			window.to_label('Не могу найти папку Ноиты')

	def test(self):
		print('Gotcha')

	def to_label(self, text):
		self.label['text'] = text

#a = Tk()

#block = BuildWindow(a, 'main')
path = 'C:\\Users\\{0}\\AppData\\LocalLow\\Nolla_Games_Noita\\save00'.format(uname)

w = Tk()
x = Test(w, 'main')
x.to_label("Banana")
w.mainloop()
#a.mainloop()