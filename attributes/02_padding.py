from tkinter import Tk, Frame, LEFT, TOP
from tkinter.ttk import Button
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("widget - padding", 800, 640)

    def init_ui(self):
        frame = Frame(self, bd=5)
        frame.pack()

        btn1 = Button(frame, text='Button')
        btn1.pack(side=LEFT, padx=5)

        btn2 = Button(frame, text='Button')
        btn2.pack(side=LEFT, padx=5)

        frame2 = Frame(self, bd=5)
        frame2.pack()

        btn1 = Button(frame2, text='Button')
        btn1.pack(side=TOP, pady=15)

        btn2 = Button(frame2, text='Button')
        btn2.pack(side=TOP, pady=15)

        self.pack()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
