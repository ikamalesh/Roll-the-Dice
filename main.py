from tkinter import *
from PIL import Image, ImageTk
import random
import time
class Dice():
    def __init__(self, window):
        window.geometry("600x500")
        window.resizable(0,0)
        window.title("Dice")
        window.config(bg='black')
        global image1, image2, image3, image4, image5, image6, piclabel, num_label

        image1, image2, image3, image4, image5, image6 = Image.open('1.png'), Image.open('2.png'), Image.open(
            '3.png'), Image.open('4.png'), Image.open('5.png'), Image.open('6.png')

        image1, image2, image3, image4, image5, image6 = ImageTk.PhotoImage(image1), ImageTk.PhotoImage(
            image2), ImageTk.PhotoImage(image3), ImageTk.PhotoImage(image4), ImageTk.PhotoImage(
            image5), ImageTk.PhotoImage(image6),

        piclabel = Label(window, image=image1)
        piclabel.place(x=200, y=140)
        num_label = Label(window, text='1', font='calibri 50 bold', fg='white',bg='black')
        num_label.place(x=270,y=20)
        Button(window, text='Shuffle', width=10, bg='white',font='calibri 12 bold',command = Dice.change).place(x=245, y=400)
        global changelist
        changelist = [image2, image4, image6, image5, image1, image3]
    def change():
        r = random.choice(changelist)
        s = str(r)
        print(s)
        piclabel.config(image=r)
        num_label.config(text=s[-1])
if __name__ == '__main__':
    window = Tk()
    app = Dice(window)
    window.mainloop()
