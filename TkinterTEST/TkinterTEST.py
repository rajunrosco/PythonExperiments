from tkinter import *
import TkPassword

BuildsList = [
    ("development","win64development"),
    ("debug","win64debug"),
    ("test","win64test")
    ]


class MyApp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.counter = 0
        self.geometry("500x500")
        self.RadioFrame = Frame(self, bg='green', height=200, width=100)
        self.RadioFrame.grid(row=0, column=0, sticky=E+W+N+S)
        self.RadioVal = StringVar()
        self.RadioList=[]
        for atext, avalue in BuildsList:
            tempradio = Radiobutton(self.RadioFrame, text=atext, value=avalue, variable=self.RadioVal, anchor=W)
            tempradio.pack(fill=X, side=TOP)
            self.RadioList.append(tempradio)
            self.RadioVal.set(avalue+repr(self.counter))


        self.myButton = Button(self, text="PUSH", command=self.myButton_click)
        self.myButton.grid(row=2, column=0)
        self.myButton2 = Button(self, text="PUSH", command=self.myButton2_click)
        self.myButton2.grid(row=2, column=0)
        self.PasswordButton = Button(self,text="Password", command=self.GetPassword)
        self.PasswordButton.grid(row=3, column=0)

        
        self.mainloop()

    def myButton_click(self):
        print("Pushed")
        self.counter=self.counter+1
        for radioobj in self.RadioList:
            radioobj.destroy()

        for atext, avalue in BuildsList:
            tempradio = Radiobutton(self.RadioFrame, text=atext+repr(self.counter), value=avalue+repr(self.counter), variable=self.RadioVal, anchor=W)
            tempradio.pack(fill=X, side=TOP)
            self.RadioVal.set(avalue+repr(self.counter))
            self.RadioList.append(tempradio)

    def myButton2_click(self):
        print(self.RadioVal.get())

    def GetPassword(self):
        TkPassword.TkPassword(self)

MyAppObj = MyApp()
