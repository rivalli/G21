import tkinter as tk
from tkinter import ttk
from tkinter import *
import tkinter.font as tkFont

class Window(tk.Frame):

	def __init__(self):
		tk.Frame.__init__(self)
		self.grid()
		self.create_widgets()
		
	def create_widgets(self):
		f = tkFont.Font(size = 20, family = "Courier New")

		self.dict = {'泰國': ['芭達雅', '普吉島', '曼谷'],
                     '日本': ['東京', '沖繩', '大阪', '京都'],
                     '韓國': ['釜山', '首爾'],
					 '香港': ['香港'],
					 '新加坡': ['新加坡']}
		self.variable1 = tk.StringVar(self)
		self.variable2 = tk.StringVar(self)
		self.variable1.set('選擇國家')
		self.variable2.set('選擇城市')
		self.variable1.trace('w', self.updateoptions)
		self.droplist1 = tk.OptionMenu(self, self.variable1, *self.dict.keys(), command=self.getValue)
		self.droplist2 = tk.OptionMenu(self, self.variable2, '', command=self.getValue)

		default1 = "要的行程"
		self.txt1 = tk.Entry(self, bd=1)
		self.txt1.insert(0, default1)
		self.txt1.bind('<FocusIn>', self.on_entry_click(self.txt1, default1))
		self.txt1.bind('<FocusOut>', self.on_focusout(self.txt1, default1))
		self.txt1.config(fg='grey')
		default2 = "不要的行程"
		self.txt2 = tk.Entry(self, bd=1)
		self.txt2.insert(0, default2)
		self.txt2.bind('<FocusIn>', self.on_entry_click(self.txt2, default2))
		self.txt2.bind('<FocusOut>', self.on_focusout(self.txt2, default2))
		self.txt2.config(fg='grey')

		self.btn1 = tk.Button(self, height=2, width=8, text="Search", command=self.clickBtn, font=f)
		self.cvsMain = tk.Canvas(self, width = 800, height = 600, bg = "white")
		
		
		self.droplist1.grid(row=0, column=0, columnspan=2,sticky=tk.E+tk.W)
		self.droplist2.grid(row=0, column=2, columnspan=2,sticky=tk.E+tk.W)
		self.txt1.grid(row=1, column=0, columnspan=4,sticky=tk.E+tk.W)
		self.txt2.grid(row=2, column=0, columnspan=4,sticky=tk.E+tk.W)
		self.btn1.grid(row=1, column=4, rowspan=2, sticky=tk.E+tk.W)
		self.cvsMain.grid(row=3, column=0, columnspan=4, sticky= tk.NE + tk.SW)

	def clickBtn(self): 
		country_to_use = self.variable1.get()
		city_to_use = self.variable2.get()
		return country_to_use, city_to_use

	def getValue(self):

		pass		


	def on_entry_click(self, entry, text):  # function that gets called whenever entry is clicked
		if entry.cget('fg') == 'grey':
			entry.delete(0, "end") # delete all the text in the entry
			entry.insert(0, '') #Insert blank for user input
			entry.config(fg = 'black')

	def on_focusout(self, entry, text):
		if entry.get() == '':
			entry.insert(0, text)
			entry.config(fg = 'grey')	

	def updateoptions(self, *args):
		countries = self.dict[self.variable1.get()]
		self.variable2.set(countries[0])
		menu = self.droplist2['menu']
		menu.delete(0, 'end')
		for country in countries:
			menu.add_command(label=country, command=lambda country=country: self.variable2.set(country))
	
	
mywindow = Window()
mywindow.master.title("KKDay+")
mywindow.mainloop()