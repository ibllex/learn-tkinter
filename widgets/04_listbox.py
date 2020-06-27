from tkinter import Tk, Listbox, Label
from tkinter import StringVar, END
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Widgets - Listbox", 280, 400)

    def init_ui(self):
        acts = [
            'Scarlett Johansson', 'Rachel Weiss',
            'Natalie Portman', 'Jessica Alba'
        ]

        lb = Listbox(self)

        for i in acts:
            lb.insert(END, i)

        lb.bind("<<ListboxSelect>>", self.on_select)

        lb.pack(pady=15)

        self.var = StringVar()
        self.label = Label(self, text=0, textvariable=self.var)
        self.label.pack()

    def on_select(self, val):
        sender = val.widget
        idx = sender.curselection()
        value = sender.get(idx)

        self.var.set(value)

def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
