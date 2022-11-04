import tkinter as tk
#from PIL import Image, ImageTk
my_window = tk.Tk()


"""img = ImageTk.PhotoImage(Image.open('logo.png'))"""

my_window.title("Johny's info")
my_window.geometry('500x500')
word = tk.Label(my_window, text='Mening ismim Jahongir. Men 14 yosh man. Men Diplomat maltabga boraman. Men paiton dasturlash yaxshi koraman.',
                bg='red',
                font=('Arial',20,'bold'))
word.pack()
tk.mainloop()
