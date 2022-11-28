from ClientUpgraded import*
from PIL import  ImageTk, Image
import tkinter as tk
from tkinter import messagebox


class ChangeFrames(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)

        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (GUIStartPage, GUILogInPage, GUIUserProfile):

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
            self.show_frame(GUIStartPage)

        #Client stuff

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class GUIStartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self)
        label.grid(rowspan=15, columnspan=9)

        self.img1 = ImageTk.PhotoImage(Image.open("Tivoli.png"))
        img1_label = tk.Label(self, image=self.img1)
        img1_label.grid(row=0, column=0)
        log_in_button = tk.Button(self, text="Log in", width=15, height=2, fg='#cd863b',
                                  font=('Helvetica', '15'), border=5,
                                  command=lambda: controller.show_frame(GUILogInPage))
        log_in_button.grid(row=0, column=7)
        self.img2 = ImageTk.PhotoImage(Image.open("Tivoli1.png"))
        img2_label = tk.Label(self, image=self.img2)
        img2_label.grid(row=1, column=0, rowspan=14, columnspan=9)
        buy_ticket_button = tk.Button(self, text="Buy ticket", width=15, height=2, fg='white',
                                      font=('Helvetica', '20'), background='#d4ac74', border=5)
        buy_ticket_button.grid(row=10, column=3)


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

        def log_in():
            entered_email = self.email_entry.get()
            self.email_entry.delete(0, 'end')
            entered_pwd = self.pwd_entry.get()
            self.pwd_entry.delete(0, 'end')

            if entered_email == "qqq" and entered_pwd == "aaa":
                log_in_button1 = tk.Button(self, text=f"Welcome {entered_email} \n"
                                                      f" Press here to go to your profile",
                                           width=40, height=10, fg='green', bg='white',
                                           font=('Helvetica', '15', 'bold'), border=5,
                                           command=lambda: controller.show_frame(GUIUserProfile))
                log_in_button1.grid(row=2, column=3)
            elif entered_email != "qqq" and entered_pwd != "aaa":
                messagebox.showerror("Error", "Invalid e-mail or password")

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
                                          font=('Helvetica', '16'), border=5)
        create_account_button.grid(row=11, column=3)


class GUIUserProfile(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = tk.Label(self)
        label.grid(rowspan=14, columnspan=9)

        self.img1 = ImageTk.PhotoImage(Image.open("TivoliBg.png"))
        img1_label = tk.Label(self, image=self.img1)
        img1_label.grid(row=0, column=0, rowspan=14, columnspan=9)

        self.img2 = ImageTk.PhotoImage(Image.open("Tivoli.png"))
        img1_label = tk.Label(self, image=self.img2)
        img1_label.grid(row=0, column=0)

        log_out_button = tk.Button(self, text="Log out", width=15, height=2, fg='#ba8d03',
                                   font=('Helvetica', '15'), border=5)
        log_out_button.grid(row=0, column=8)

        personal_info = tk.Label(self, text="Personal Information", font=("Helvetica", 20), bg='white')
        personal_info.grid(row=3, column=0)

        self.img3 = ImageTk.PhotoImage(Image.open("UserInfo.png"))
        user_info = tk.Label(self, image=self.img3)
        user_info.grid(row=4, column=0)

        edit_prifile_button = tk.Button(self, text="Edit Profile", width=15, height=2, fg='white',
                                        font=('Helvetica', '15'), background='#d4ac74', border=5)
        edit_prifile_button.grid(row=5, column=0)

        purchases = tk.Label(self, text="Purchases", font=("Helvetica", 20), bg='white')
        purchases.grid(row=3, column=7)
        self.img4 = ImageTk.PhotoImage(Image.open("UserPurchases.png"))
        user_purcheses = tk.Label(self, image=self.img4)
        user_purcheses.grid(row=4, column=7)

        buy_ticket_button = tk.Button(self, text="Buy New Ticket", width=15, height=2, fg='white',
                                      font=('Helvetica', '15'), background='#d4ac74', border=5)
        buy_ticket_button.grid(row=5, column=7)


if __name__ == "__main__":
    myapp = ChangeFrames()
    myapp.mainloop()
