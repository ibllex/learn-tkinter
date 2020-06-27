from tkinter import Tk, Frame, Label
from tkinter import BOTH, LEFT
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("widget - cursors", 600, 200)

    def init_ui(self):
        frame = Frame(self, borderwidth=10)
        frame.pack()

        lbl1 = Label(frame, bg='SlateGray3', width=15, height=10, cursor='tcross')
        lbl1.pack(side=LEFT, padx=3)

        lbl2 = Label(frame, bg='SlateGray4', width=15, height=10, cursor='hand2')
        lbl2.pack(side=LEFT)

        lbl3 = Label(frame, bg='DarkSeaGreen3', width=15, height=10, cursor='heart')
        lbl3.pack(side=LEFT, padx=3)

        lbl4 = Label(frame, bg='DarkSeaGreen4', width=15, height=10, cursor='pencil')
        lbl4.pack(side=LEFT)

        self.pack()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
