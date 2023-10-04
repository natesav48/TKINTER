from tkinter import *
master = Tk()


#these are my labels
w = Label(master, text='Label 1')
w.pack()
w2 = Label(master, text='Label 2')
w2.pack()
w3 = Label(master, text='label 3')
w3.pack()
w4 = Label(master, text='Label 4')
w4.pack()



#these are my check boxes
var1 = IntVar()
Checkbutton(master, text='male', variable=var1).pack()
var2 = IntVar()
Checkbutton(master, text='female', variable=var2).pack()

var3 = IntVar()
Checkbutton(master, text='attack helicopter', variable=var3).pack()
var4 = IntVar()
Checkbutton(master, text='knucklehead', variable=var4).pack()


#buttons
#r = tk.Tk()
master.title('Buttons')
button = Button(master, text='button 1', width=50)
button.pack()
button = Button(master, text='button 2', width=50)
button.pack()
button = Button(master, text='button 3', width=50)
button.pack()
button = Button(master, text='button 4', width=50)
button.pack()



#these are my text boxes
Label(master, text='First Name').pack()
Label(master, text='Last Name').pack()
e1 = Entry(master)
e2 = Entry(master)
e1.pack()
e2.pack()



#these are my sliders

w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()
w = Scale(master, from_=0, to=42)
w.pack()
w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
w.pack()



#Message box
ourMessage ='MESSAGE BOX LETS GO'
messageVar = Message( text = ourMessage)
messageVar.config(bg='black')
messageVar.pack( )



#radio buttons

v = IntVar()
Radiobutton(master, text='A', variable=v, value=1).pack(anchor=W)
Radiobutton(master, text='B', variable=v, value=2).pack(anchor=W)
Radiobutton(master, text='C', variable=v, value=3).pack(anchor=W)
Radiobutton(master, text='D', variable=v, value=4).pack(anchor=W)
Radiobutton(master, text='E', variable=v, value=5).pack(anchor=W)



#Spin Box
w = Spinbox(master, from_ = 90, to = 100)
w.pack()



#drop down menu
mb =  Menubutton (text = "Menu")
mb.menu  =  Menu ( mb, tearoff = 0 )
mb["menu"]  =  mb.menu
cVar  = IntVar()
aVar = IntVar()
mb.menu.add_checkbutton ( label ='Contact', variable = cVar )
mb.menu.add_checkbutton ( label = 'About', variable = aVar )
mb.pack()

mainloop()