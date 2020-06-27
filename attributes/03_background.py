from tkinter import Tk, Frame, LEFT, Label
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("widget - bg & fg", 800, 400)

    def init_ui(self):
        frame = Frame(self, borderwidth=10)
        frame.pack()

        lbl1 = Label(frame, bg='SlateGray3', fg="#fff", width=15, height=10, text="Label 01")
        lbl1.pack(side=LEFT, padx=3)

        lbl2 = Label(frame, bg='SlateGray4', fg="#fff", width=15, height=10, text="Label 02")
        lbl2.pack(side=LEFT)

        lbl3 = Label(frame, bg='DarkSeaGreen3', fg="#fff", width=15, height=10, text="Label 03")
        lbl3.pack(side=LEFT, padx=3)

        lbl4 = Label(frame, bg='DarkSeaGreen4', fg="#fff", width=15, height=10, text="Label 04")
        lbl4.pack(side=LEFT)

        self.pack()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
