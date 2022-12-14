from ClientUpgraded import *
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox


class PagesContainer(tk.Tk):

    user = CostumerWithProfile

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        pages_container = tk.Frame(self)

        pages_container.pack(side="top", fill="both", expand=True)

        self.pages = {}

        for Page in (GUIStartPage, GUILogInPage, GUIUserProfile):
            page = Page(pages_container, self)
            self.pages[Page] = page
            page.grid(row=0, column=0, sticky="nsew")
            self.show_page(GUIStartPage)

        #self.user = CostumerWithProfile

    def show_page(self, this_page):
        page = self.pages[this_page]
        page.tkraise()


class GUIStartPage(tk.Frame):
    def __init__(self, parent, change_page):
        tk.Frame.__init__(self, parent)

        self.img1 = ImageTk.PhotoImage(Image.open("Tivoli.png"))
        img1_label = tk.Label(self, image=self.img1)
        img1_label.grid(row=0, column=0)
        log_in_button = tk.Button(self, text="Log in", width=15, height=2, fg='#cd863b',
                                  font=('Helvetica', '15'), border=5,
                                  command=lambda: change_page.show_page(GUILogInPage))
        log_in_button.grid(row=0, column=7)
        self.img2 = ImageTk.PhotoImage(Image.open("Tivoli1.png"))
        img2_label = tk.Label(self, image=self.img2)
        img2_label.grid(row=1, column=0, rowspan=14, columnspan=9)
        buy_ticket_button = tk.Button(self, text="Buy ticket", width=15, height=2, fg='white',
                                      font=('Helvetica', '20'), background='#d4ac74', border=5)
        buy_ticket_button.grid(row=10, column=3)


class GUILogInPage(tk.Frame):
    def __init__(self, parent, change_page):
        tk.Frame.__init__(self, parent)

        self.img1 = ImageTk.PhotoImage(Image.open("Tivoli.png"))
        img1_label = tk.Label(self, image=self.img1)
        img1_label.grid(row=0, column=0)

        log_in = tk.Label(self, text="Log in", font=("Helvetica", 25))
        log_in.grid(row=1, padx=10, column=2, pady=50)

        # Client stuff
        self.C = Client()
        self.C.connect()

        # self.user = CostumerWithProfile

        def log_in():
            entered_email = self.email_entry.get()
            self.email_entry.delete(0, 'end')
            entered_pwd = self.pwd_entry.get()
            self.pwd_entry.delete(0, 'end')

            # Client stuffs
            self.C.login(entered_email, entered_pwd)
            PagesContainer.user = self.C.User

            if len(self.C.User.order_list) > 0:
                self.C.disconnect()
                log_in_button1 = tk.Button(self, text=f"Welcome {entered_email} \n"
                                                      f" Press here to go to your profile",
                                           width=40, height=10, fg='green', bg='white',
                                           font=('Helvetica', '15', 'bold'), border=5,
                                           command=lambda: change_page.show_page(GUIUserProfile))
                log_in_button1.grid(row=2, column=3)
            else:
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
    def __init__(self, parent, change_page):
        tk.Frame.__init__(self, parent)


        #Client stuff
        self.user = CostumerWithProfile
        print(self.user)

        self.img1 = ImageTk.PhotoImage(Image.open("TivoliBg.png"))
        img1_label = tk.Label(self, image=self.img1)
        img1_label.grid(row=0, column=0, rowspan=14, columnspan=9)

        self.img2 = ImageTk.PhotoImage(Image.open("Tivoli.png"))
        img1_label = tk.Label(self, image=self.img2)
        img1_label.grid(row=0, column=0)



        self.personal_info = tk.Label(self, text="Personal Information", font=("Helvetica", 20), bg='white')
        self.personal_info.grid(row=3, column=0)

        self.user_personal_info = tk.Text(self, width=25, height=15, bd=2, font=('Helvetica', '15'))
        self.user_personal_info.grid(row=4, column=0)


        self.purchases = tk.Label(self, text="Purchases", font=("Helvetica", 20), bg='white')
        self.purchases.grid(row=3, column=7)

        self.user_purcheses = tk.Text(self, width=55, height=15, bd=2, font=('Helvetica', '15'))
        self.user_purcheses.grid(row=4, column=7)

        self.buy_ticket_button = tk.Button(self, text="Buy New Ticket", width=15, height=2, fg='white',
                                      font=('Helvetica', '15'), background='#d4ac74', border=5)
        self.buy_ticket_button.grid(row=5, column=7)

        self.update_button = tk.Button(self, text="Update user info", width=20, height=2, fg='white', bg='green',
                                       font=('Helvetica', '16'), border=5,
                                       command=self.update_text)
        self.update_button.grid(row=3, column=7)

        self.log_out_button = tk.Button(self, text="Log out", width=15, height=2, fg='#ba8d03',
                                        font=('Helvetica', '15'), border=5)
        self.log_out_button.grid(row=0, column=8)

        self.edit_prifile_button = tk.Button(self, text="Edit Profile", width=15, height=2, fg='white',
                                             font=('Helvetica', '15'), background='#d4ac74', border=5)
        self.edit_prifile_button.grid(row=5, column=0)
    def update_text(self):
        self.user = PagesContainer.user

        self.user_personal_info.delete(0.0, 100.0)
        self.user_personal_info.insert(0.0, repr(self.user))

        self.user_purcheses.delete(0.0, 100.0)
        self.user_purcheses.insert(0.0, repr(self.user.order_list[0]))


if __name__ == "__main__":
    myapp = PagesContainer()
    myapp.mainloop()
