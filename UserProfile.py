from PIL import ImageTk, Image
import tkinter as tk
from tkinter import messagebox
from GUIContainer import*
from GUIStartPage import GUIStartPage
from GUILogin import*

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
                                       font=('Helvetica', '15'), border=5,
                                  command=lambda: controller.show_frame(GUIStartPage))
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
