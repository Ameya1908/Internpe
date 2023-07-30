from tkinter import *
from time import strftime
root = Tk()
root.geometry("400x400")
root.resizable(0,0)
root.title('Python Clock')
Label(root,text = 'Ameya Kumar Chandrakar', font ='arial 20 bold italic').pack(side=BOTTOM)
def time():
    string = strftime('%H:%M:%S %p')
    mark.config(text = string)
    mark.after(1000, time)
mark = Label(root, 
            font = ('arial', 40, 'bold'),
            pady=150,
            foreground = 'green')
mark.pack(anchor = 'center')
time()
 
mainloop()