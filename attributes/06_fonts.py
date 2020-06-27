from tkinter import Tk, BOTH
from tkinter.ttk import Frame, Label, Notebook, Style
from tkinter.font import Font
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("widget - fonts", 400, 200)

    def init_ui(self):
        txt = "Today is a beautiful day"

        mono_font = Font(family="Ubuntu Mono", size=16)
        label1 = Label(self, text=txt, font=mono_font)
        label1.grid(row=0, column=0)

        label2 = Label(self, text=txt, font="TkTextFont")
        label2.grid(row=1, column=0)

        label3 = Label(self, text=txt, font=('Times', '18', 'italic'))
        label3.grid(row=2, column=0)


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
