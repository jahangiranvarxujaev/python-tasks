import tkinter as tk  #вызов функции
win = tk.Tk()  #вызов окна


win.title('first window')  #наименование окна
win.geometry('500x500')  #параметры
win.minsize(300,300)  #мин размер
win.maxsize(1000,1000)  #макс размер
win.resizable(True, True)  #переизменяемый
win.config(bg='Blue')
word = tk.Label(text='Assalomu aleykum',
                bg='red',
                font=('Arial',20,'bold'))
word.pack()
win.mainloop()  #start

import tkinter as t

window = t.Tk()

greeting = t.Label(text="Hello, Tkinter")
label = t.Label(
    text="Hello, Tkinter",
    foreground="white",
    # Set the text color to white
    background="black"
    # Set the background color to black
)
button = t.Button(
    text="Click me!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow",
)
greeting.pack()
button.pack()
label.pack()
window.mainloop()