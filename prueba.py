
from tkinter import *
from tkinter import ttk

import socket
import codecs


class App():
	def __init__(self):
	
		self.root = Tk()  			
		self.root.title('HS100')		
		self.root.geometry('350x350')

		# mainframe

		self.mainframe = Frame(self.root)
		self.mainframe.config(bd = 15)
		self.mainframe.pack()

		# label
		
		self.labeltitle = Label(self.mainframe, text = "HS100")
		self.labeltitle.config(fg = "white", bg = "black",font = ("Verdana",24))
		self.labeltitle.pack(anchor = CENTER)	

		#input frame

		self.inputframe = Frame(self.mainframe)
		self.inputframe.config(bd = 10)
		self.inputframe.pack()

		# input ip

		ip = StringVar()

		self.label_ip = Label(self.inputframe, text = "IP")
		self.label_ip.grid(row = 0, column = 0, padx = 3, pady = 3)

		self.entry_ip = Entry(self.inputframe, textvariable = ip)	
		self.entry_ip.grid(row = 0, column = 1)

		# input port

		self.label_port = Label(self.inputframe, text="Port")
		self.label_port.grid(row = 1, column = 0,padx = 3, pady = 3)

		self.entry_port = Entry(self.inputframe)	
		self.entry_port.grid(row = 1, column = 1)

		# input functions

		self.functionsframe = Frame(self.mainframe)
		self.functionsframe.pack()

        # button info
		self.bconect = ttk.Button(self.functionsframe,text="conect",command=self.connect).pack(side = LEFT)
		self.bon = ttk.Button(self.functionsframe,text="on",command=self.on).pack(side = LEFT)
		self.boff = ttk.Button(self.functionsframe,text="off",command=self.off).pack(side = LEFT)

		# input button
		self.buttonframe = Frame(self.mainframe)
		self.buttonframe.pack()

		# button info
		self.binfo = ttk.Button(self.buttonframe,text="info",command=self.get_info).pack(side = LEFT)
		
		# button exit
		self.bclick = ttk.Button(self.buttonframe,text="exit",command=self.exit).pack(side = LEFT)
		
		# errors
		self.errorsframe = Frame(self.mainframe)
		self.errorsframe.config(bd = 10)
		self.errorsframe.pack()

		self.root.mainloop()


	def connect(self):

		#ip = str(self.entry_ip.get())
		if(bool(self.entry_ip.get()) == True and bool(self.entry_port.get()) == True):	# Validacion caso que no ingreso Ip o puerto

			ip = "216.58.222.46" #str(self.entry_ip.get()
			port =  int(self.entry_port.get())			

			self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			self.socket.settimeout(1)
			
			try:
				self.socket.connect((ip, port))		
				print (self.socket)
			except socket.error as msg:
	   			print ("Caught exception socket.error : %socket" %msg)
	   			self.label_error = Label(self.errorsframe,bg = "red", font=("Verdana", 10),text="no conect").pack()
			print ("Conect")
			#print (self.socket)
		else:
			print ("noo bool")


	def on(self):
		
		print ("on")
	
		IP = str(self.entry_ip.get())
		Puerto = int(self.entry_port.get())
		
		Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		Socket.connect((IP, Puerto))
		data = codecs.decode("0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedfa2dfa2","hex")
		Socket.send(data)
		data = codecs.decode("00000025d0f281e28aef8bfe92f7d5ef94b6d1b4c09ff194ec98c7a6c5b1d8b7d9fbc1afdab6daa7da","hex")
		Socket.send(data)
		Socket.close()


	def off(self):
	
		print ("off")

		IP = str(self.entry_ip.get())
		print(type(IP))
		Puerto = int(self.entry_port.get())
		
		Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		Socket.connect((IP,Puerto))
		data = codecs.decode("0000002ad0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381f286e793f6d4eedea3dea3","hex")
		Socket.send(data)
		data = codecs.decode("0000002dd0f281f88bff9af7d5ef94b6c5a0d48bf99cf091e8b7c4b0d1a5c0e2d8a381e496e4bbd8b7d3b694ae9ee39ee3","hex")
		Socket.send(data)
		Socket.close


	def get_info(self):
		print ("Mostrar Info")

	def exit(self):
		self.root.destroy()


app = App()
