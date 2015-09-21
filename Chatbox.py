from Tkinter import *

class Application:

    def hello(self):
        msg = tkinter.messagebox.askquestion('title','question')

    def __init__(self, form):
        form.resizable(0,0)
        form.minsize(200, 200)
        form.title('Top Level')

        # Global Padding pady and padx
        pad_x = 5
        pad_y = 5

        # create a toplevel menu
        menubar = Menu(form)
        #command= parameter missing.
        menubar.add_command(label="Menu1")
        #command= parameter missing.
        menubar.add_command(label="Menu2")
        #command= parameter missing.
        menubar.add_command(label="Menu3")

        # display the menu
        form.config(menu=menubar)

        # Create controls

        label1 = Label(form, text="Label1")
        textbox1 = Entry(form)
        #command= parameter missing.
        button1 = Button(form, text='Button1')

        scrollbar1 = Scrollbar(form)
        textarea1 = Text(form, width=20, height=10)

        textarea1.config(yscrollcommand=scrollbar1.set)
        scrollbar1.config(command=textarea1.yview)

        textarea1.grid(row=0, column=1, padx=pad_x, pady=pad_y, sticky=W)
        scrollbar1.grid(row=0, column=2, padx=pad_x, pady=pad_y, sticky=W)
        textbox1.grid(row=1, column=1, padx=pad_x, pady=pad_y, sticky=W)
        button1.grid(row=1, column=2, padx=pad_x, pady=pad_y, sticky=W)
	button1 = Button(form, text='Button1', command = self.addchat)
	self.textbox = textbox1
    	self.textarea = textarea1 # see above
    	form.bind("<Return>", lambda x: self.addchat())
    # this is the magic that makes your enter key do something
        form.mainloop()

    def addchat(self):
    	txt = self.textbox.get()
    	# gets everything in your textbox
    	self.textarea.insert(END,"\n"+txt)
    	# tosses txt into textarea on a new line after the end
    	self.textbox.delete(0,END) # deletes your textbox text

root = Tk()
Application(root)


