from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter import colorchooser
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Dialog - Color Chooser", 480, 200)

    def init_ui(self):
        self.btn = Button(self, text="Choose Color", command=self.on_choose)
        self.btn.place(x=30, y=30)

        self.frame = Frame(self, border=1, relief=SUNKEN, width=100, height=100)
        self.frame.place(x=160, y=30)

    def on_choose(self):
        (rgb, hx) = colorchooser.askcolor()
        self.frame.config(bg=hx)


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
