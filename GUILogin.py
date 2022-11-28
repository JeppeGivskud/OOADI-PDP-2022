from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from UserProfile import*
from GUIStartPage import*
from GUIContainer import*

class GUILogInPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.label = tk.Label(self)
        self.label.grid(rowspan=15, columnspan=9)
        self.img1 = ImageTk.PhotoImage(Image.open("Tivoli.png"))
        img1_label = tk.Label(self, image=self.img1)
        img1_label.grid(row=0, column=0)
        log_in = tk.Label(self, text="Log in", font=("Helvetica", 25))
        log_in.grid(row=1, padx=10, column=2, pady=50)

        def log_in(self):
            self.entered_email = self.email_entry.get()
            self.email_entry.delete(0, 'end')
            self.entered_pwd = self.pwd_entry.get()
            self.pwd_entry.delete(0, 'end')

            if self.entered_email == "qqq" and self.entered_pwd == "aaa":
                log_in_button1 = tk.Button(self, text=f"Welcome {self.entered_email} \n Press here to go to your profile",
                                          width=40, height=10, fg='green', bg='white',
                                          font=('Helvetica', '15', 'bold'), border=5,
                                          command=lambda: controller.show_frame(GUIUserProfile))
                log_in_button1.grid(row=2, column=3)
            elif self.entered_email != "qqq" and self.entered_pwd != "aaa":
                messagebox.showerror("Error", "Invalid e-mail or password")
            elif self.entered_email == "" or self.entered_pwd == "":
                messagebox.showerror("Error", "All fields are required")


        email_label = tk.Label(self, text="E-mail", font=("Goudy old style", 25, "bold"))
        email_label.grid(row=2, column=2, padx=20, pady=20)
        self.email_entry = tk.Entry(self, width=50, bg='#fce5cd', borderwidth=2, font=("Goudy old style", 15))
        self.email_entry.grid(row=2, column=3)

        pwd_label = tk.Label(self, text="Password", font=("Goudy old style", 25, "bold"))
        pwd_label.grid(row=4, column=2, padx=20, pady=20)
        self.pwd_entry = tk.Entry(self, width=50, bg='#fce5cd', borderwidth=2, font=("Goudy old style", 15))
        self.pwd_entry.grid(row=4, column=3)

        log_in_button = tk.Button(self, text="Log in", width=30, height=2, fg='white', bg='#d4ac74',
                                  font=('Helvetica', '16'), border=5,
                                  command=log_in)
        log_in_button.grid(row=6, column=3)


        sau_label = tk.Label(self, text="Or", font=("Helvetica", 15))
        sau_label.grid(row=9, column=3, padx=30)

        create_account_button = tk.Button(self, text="Create account", width=30, height=2, fg='#d4ac74', bg='white',
                                  font=('Helvetica', '16'), border=5,
                                  command=lambda: controller.show_frame(GUIStartPage))
        create_account_button.grid(row=11, column=3)


if __name__ == "__main__":
    myapp = ChangeFrames()
    myapp.mainloop()