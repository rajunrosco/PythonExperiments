
import tkinter as tk


class TkPassword(tk.Frame):
    counter = 0
    def __init__(self,parent=None):
        self.counter += 1
        if parent is not None:
            self.PasswordDialog = tk.Toplevel(parent)
            self.PasswordDialog.wm_title("Window #%s" % self.counter)
            # defines a grid 50 x 50 cells in the main window
            rows = 0
            while rows < 10:
                self.PasswordDialog.rowconfigure(rows, weight=1)
                self.PasswordDialog.columnconfigure(rows, weight=1)
                rows += 1
 
 
            # adds username entry widget and defines its properties
            self.username_box = tk.Entry(self.PasswordDialog)
            self.username_box.insert(0, 'Enter Username')
            self.username_box.bind("<FocusIn>", self.clear_widget)
            self.username_box.bind('<FocusOut>', self.repopulate_defaults)
            self.username_box.grid(row=1, column=5, padx=20, pady=10,sticky='NS')
 
 
            # adds password entry widget and defines its properties
            self.password_box = tk.Entry(self.PasswordDialog, show='*')
            self.password_box.insert(0, ' ')
            self.password_box.bind("<FocusIn>", self.clear_widget)
            self.password_box.bind('<FocusOut>', self.repopulate_defaults)
            self.password_box.bind('<Return>', self.login)
            self.password_box.grid(row=2, column=5, padx=20, pady=10, sticky='NS')
 
 
            # adds login button and defines its properties
            self.login_btn = tk.Button(self.PasswordDialog, text='Login', command=self.login)
            self.login_btn.bind('<Return>', self.login)
            self.login_btn.grid(row=5, column=5, padx=20, pady=10, sticky='NESW')

     
    def clear_widget(self,event):
 
        # will clear out any entry boxes defined below when the user shifts
        # focus to the widgets defined below
        if self.username_box == self.PasswordDialog.focus_get() and self.username_box.get() == 'Enter Username':
            self.username_box.delete(0, tk.END)
        elif self.password_box == self.password_box.focus_get() and self.password_box.get() == ' ':
            self.password_box.delete(0, tk.END)
 
    def repopulate_defaults(self,event):
 
        # will repopulate the default text previously inside the entry boxes defined below if
        # the user does not put anything in while focused and changes focus to another widget
        if self.username_box != self.PasswordDialog.focus_get() and self.username_box.get() == '':
            self.username_box.insert(0, 'Enter Username')
        elif self.password_box != self.PasswordDialog.focus_get() and self.password_box.get() == '':
            self.password_box.insert(0, ' ')
 
    def login(self,*event):
 
        # Able to be called from a key binding or a button click because of the '*event'
        print('Username: {}'.format(self.username_box.get()))
        print('Password: {}'.format(self.password_box.get()))
        self.PasswordDialog.destroy()
        # If I wanted I could also pass the username and password I got above to another 
        # function from here.
