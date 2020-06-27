from tkinter import Tk
from tkinter.ttk import Label
from PIL import Image, ImageTk
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Absolute positioning", 960, 480)

    def init_ui(self):
        self.style.configure("TFrame", background="#edeff4")

        image_kevin = Image.open("images/kevin-mueller-6w-jK5Bfz2k-unsplash.jpg").resize((200, 200))
        kevin = ImageTk.PhotoImage(image_kevin)
        label1 = Label(self, image=kevin)
        label1.image = kevin
        label1.place(x=20, y=20)

        image_craig = Image.open("images/craig-melville-CY2sDlYLSuE-unsplash.jpg").resize((200, 200))
        craig = ImageTk.PhotoImage(image_craig)
        label2 = Label(self, image=craig)
        label2.image = craig
        label2.place(x=240, y=20)

        image_karl = Image.open("images/karl-lee-gM7LYJYrBSw-unsplash.jpg").resize((200, 200))
        karl = ImageTk.PhotoImage(image_karl)
        label2 = Label(self, image=karl)
        label2.image = karl
        label2.place(x=460, y=20)


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
