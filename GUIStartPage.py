from PIL import ImageTk, Image
import tkinter as tk
from GUIContainer import*
from GUILogin import GUILogInPage

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

if __name__ == "__main__":
    myapp = ChangeFrames()
    myapp.mainloop()