import tkinter as tk #вызов функции
win = tk.Tk() #вызов окна

photo = tk.PhotoImage(file='logo.png')
win.iconphoto(False,photo)

win.title('first window') #наименование окна
win.geometry('500x500') #параметры
win.minsize(300,300) #мин размер
win.maxsize(1000,1000) #макс размер
win.resizable(True, True) #переизменяемый
win.config(bg='Blue')
word = tk.Label(win, text='Assalomu aleykum',
                bg='red',
                font=('Arial',20,'bold'))
word.pack()
tk.mainloop() #start