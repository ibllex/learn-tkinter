from tkinter import Tk, Frame, LEFT, Button
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("widget - width & height", 800, 400)

    def init_ui(self):
        frame = Frame(self, borderwidth=10)
        frame.pack()

        btn1 = Button(frame, text='Button')
        btn1.pack(side=LEFT, padx=5)

        btn2 = Button(frame, text='Button', width=8)
        btn2.pack(side=LEFT, padx=5)

        btn3 = Button(frame, text='Button', width=5, height=4)
        btn3.pack(side=LEFT)

        self.pack()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
