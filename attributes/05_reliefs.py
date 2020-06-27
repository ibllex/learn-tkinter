from tkinter import Tk, Frame, Label
from tkinter import BOTH, LEFT, FLAT, SUNKEN, RAISED, GROOVE, RIDGE
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("widget - reliefs", 800, 400)

    def init_ui(self):
        frame = Frame(self, borderwidth=10)
        frame.pack()

        lbl1 = Label(frame, bg='LightSteelBlue3', width=15, height=10, relief=FLAT)
        lbl1.pack(side=LEFT, padx=3)

        lbl2 = Label(frame, bg='LightSteelBlue3', bd=2, width=15, height=10, relief=SUNKEN)
        lbl2.pack(side=LEFT)

        lbl3 = Label(frame, bg='LightSteelBlue3', bd=2, width=15, height=10, relief=RAISED)
        lbl3.pack(side=LEFT, padx=3)

        lbl4 = Label(frame, bg='LightSteelBlue3', bd=3, width=15, height=10, relief=GROOVE)
        lbl4.pack(side=LEFT)

        lbl5 = Label(frame, bg='LightSteelBlue3', bd=3, width=15, height=10, relief=RIDGE)
        lbl5.pack(side=LEFT, padx=3)

        self.pack()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
