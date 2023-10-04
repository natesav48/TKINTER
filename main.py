from tkinter import *
master = Tk()

def labels():
    #these are my labels
    root = Tk()
    w = Label(root, text='Shout out my label thats me')
    w.pack()
    w2 = Label(root, text='im in this b w tb')
    w2.pack()
    w3 = Label(root, text='im in this b w 4 trey')
    w3.pack()
    w4 = Label(root, text='I just poured up me a 8')
    w4.pack()
labels()

def checkboxes():
    #these are my check boxes
    var1 = IntVar()
    Checkbutton(master, text='male', variable=var1).grid(row=0, sticky=W)
    var2 = IntVar()
    Checkbutton(master, text='female', variable=var2).grid(row=1, sticky=W)

    var3 = IntVar()
    Checkbutton(master, text='attack helicopter', variable=var3).grid(row=2, sticky=W)
    var4 = IntVar()
    Checkbutton(master, text='knucklehead', variable=var4).grid(row=3, sticky=W)
checkboxes()

def buttons():
    #buttons
    import tkinter as tk
    r = tk.Tk()
    r.title('whats your favorite kendrick album?')
    button = tk.Button(r, text='To pimp a butterfly', width=50, command=r.destroy)
    button.pack()
    button = tk.Button(r, text='good kid mad city', width=50, command=r.destroy)
    button.pack()
    button = tk.Button(r, text='pride', width=50, command=r.destroy)
    button.pack()
    button = tk.Button(r, text='mr morale and the big steppers', width=50, command=r.destroy)
    button.pack()
buttons()

def text_boxes():
    #these are my text boxes
    Label(master, text='First Name').grid(row=4)
    Label(master, text='Last Name').grid(row=5)
    e1 = Entry(master)
    e2 = Entry(master)
    e1.grid(row=4, column=1)
    e2.grid(row=5, column=1)
text_boxes()

def sliders():
    #these are my sliders
    master = Tk()
    w = Scale(master, from_=0, to=42)
    w.pack()
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()
    w = Scale(master, from_=0, to=42)
    w.pack()
    w = Scale(master, from_=0, to=200, orient=HORIZONTAL)
    w.pack()
sliders()

def message_box():
#Message box
    main = Tk()
    ourMessage ='MESSAGE BOX LETS GO'
    messageVar = Message(main, text = ourMessage)
    messageVar.config(bg='black')
    messageVar.pack( )
message_box()

def radio_buttons():
    #radio buttons
    root = Tk()
    v = IntVar()
    Radiobutton(root, text='A', variable=v, value=1).pack(anchor=W)
    Radiobutton(root, text='B', variable=v, value=2).pack(anchor=W)
    Radiobutton(root, text='C', variable=v, value=3).pack(anchor=W)
    Radiobutton(root, text='D', variable=v, value=4).pack(anchor=W)
    Radiobutton(root, text='E', variable=v, value=5).pack(anchor=W)
radio_buttons()

def spin_box():
    #Spin Box
    master = Tk()
    w = Spinbox(master, from_ = 90, to = 100)
    w.pack()
spin_box()

def drop_down_menu():
    #drop down menu
    root = Tk()
    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu)
    menu.add_cascade(label='File', menu=filemenu)
    filemenu.add_command(label='New')
    filemenu.add_command(label='Open...')
    filemenu.add_separator()
    filemenu.add_command(label='Exit', command=root.quit)
    helpmenu = Menu(menu)
    menu.add_cascade(label='Help', menu=helpmenu)
    helpmenu.add_command(label='About')
drop_down_menu()


mainloop()