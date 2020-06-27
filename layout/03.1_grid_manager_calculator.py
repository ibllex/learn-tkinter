from tkinter import Tk, W, E, S, N
from tkinter.ttk import Button, Entry, Style
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Grid Manager - Calculator", 680, 450)

    def init_ui(self):
        Style().configure("TButton", padding=(0, 5, 0, 5), font='serif 10')

        self.columnconfigure(0, pad=3, weight=1)
        self.columnconfigure(1, pad=3, weight=1)
        self.columnconfigure(2, pad=3, weight=1)
        self.columnconfigure(3, pad=3, weight=1)

        self.rowconfigure(0, pad=3)
        self.rowconfigure(1, pad=3, weight=1)
        self.rowconfigure(2, pad=3, weight=1)
        self.rowconfigure(3, pad=3, weight=1)
        self.rowconfigure(4, pad=3, weight=1)

        entry = Entry(self)
        entry.grid(row=0, columnspan=4, sticky=W + E)
        cls = Button(self, text="Cls")
        cls.grid(row=1, column=0, sticky=W + E + S + N)
        bck = Button(self, text="Back")
        bck.grid(row=1, column=1, sticky=W + E + S + N)
        lbl = Button(self)
        lbl.grid(row=1, column=2, sticky=W + E + S + N)
        clo = Button(self, text="Close")
        clo.grid(row=1, column=3, sticky=W + E + S + N)
        sev = Button(self, text="7")
        sev.grid(row=2, column=0, sticky=W + E + S + N)
        eig = Button(self, text="8")
        eig.grid(row=2, column=1, sticky=W + E + S + N)
        nin = Button(self, text="9")
        nin.grid(row=2, column=2, sticky=W + E + S + N)
        div = Button(self, text="/")
        div.grid(row=2, column=3, sticky=W + E + S + N)

        fou = Button(self, text="4")
        fou.grid(row=3, column=0, sticky=W + E + S + N)
        fiv = Button(self, text="5")
        fiv.grid(row=3, column=1, sticky=W + E + S + N)
        six = Button(self, text="6")
        six.grid(row=3, column=2, sticky=W + E + S + N)
        mul = Button(self, text="*")
        mul.grid(row=3, column=3, sticky=W + E + S + N)

        one = Button(self, text="1")
        one.grid(row=4, column=0, sticky=W + E + S + N)
        two = Button(self, text="2")
        two.grid(row=4, column=1, sticky=W + E + S + N)
        thr = Button(self, text="3")
        thr.grid(row=4, column=2, sticky=W + E + S + N)
        mns = Button(self, text="-")
        mns.grid(row=4, column=3, sticky=W + E + S + N)

        zer = Button(self, text="0")
        zer.grid(row=5, column=0, sticky=W + E + S + N)
        dot = Button(self, text=".")
        dot.grid(row=5, column=1, sticky=W + E + S + N)
        equ = Button(self, text="=")
        equ.grid(row=5, column=2, sticky=W + E + S + N)
        pls = Button(self, text="+")
        pls.grid(row=5, column=3, sticky=W + E + S + N)


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
