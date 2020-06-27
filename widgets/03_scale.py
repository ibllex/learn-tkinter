from tkinter import Tk, Scale, Label
from tkinter import IntVar, LEFT
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Widgets - Scale", 280, 100)

    def init_ui(self):
        scale = Scale(self, from_=0, to=100, command=self.on_scale)
        scale.pack(side=LEFT, padx=15)

        self.var = IntVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack(side=LEFT)

    def on_scale(self, val):
        v = int(float(val))
        self.var.set(v)

def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
