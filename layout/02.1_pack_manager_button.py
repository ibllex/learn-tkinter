from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Pack Manager - Button", 480, 360)

    def init_ui(self):
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)

        close_btn = Button(self, text="Close")
        close_btn.pack(side=RIGHT, padx=5, pady=5)

        ok_btn = Button(self, text="Ok")
        ok_btn.pack(side=RIGHT)


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
