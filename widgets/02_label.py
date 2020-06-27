from tkinter import Tk, Label
from PIL import Image, ImageTk
from base.ExampleFrame import ExampleFrame
import sys


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Widgets - Label", 280, 100)

    def load_image(self):
        try:
            self.img = Image.open("../layout/images/craig-melville-CY2sDlYLSuE-unsplash.jpg")
        except IOError:
            print("Unable to load image")
            sys.exit(1)

    def init_ui(self):
        self.load_image()
        craig = ImageTk.PhotoImage(self.img)

        label = Label(self, image=craig)

        # reference must be stored
        label.image = craig

        label.pack()
        self.pack()

    def set_geometry(self):
        w, h = self.img.size
        self.center_window(w, h)

def main():
    root = Tk()
    app = Example()
    app.set_geometry()
    root.mainloop()


if __name__ == '__main__':
    main()
