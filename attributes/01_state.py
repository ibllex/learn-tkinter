from tkinter import Tk, NORMAL, ACTIVE, DISABLED
from tkinter.ttk import Label
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("widget - state", 800, 80)

    def init_ui(self):
        self.columnconfigure(0, pad=5)
        self.columnconfigure(1, pad=5)
        self.columnconfigure(2, pad=5)

        txt = "Today is a beautiful day"

        label1 = Label(self, text=txt, state=NORMAL)
        label1.grid(row=0, column=0)

        label2 = Label(self, text=txt, state=ACTIVE)
        label2.grid(row=0, column=1)

        label3 = Label(self, text=txt, state=DISABLED)
        label3.grid(row=0, column=2)


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
