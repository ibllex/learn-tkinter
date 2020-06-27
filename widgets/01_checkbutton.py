from tkinter import Tk, Checkbutton
from tkinter import BooleanVar
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Widgets - CheckButton", 280, 100)

    def init_ui(self):
        self.var = BooleanVar()

        cb = Checkbutton(self, text="Show title", variable=self.var, command=self.on_click)
        cb.select()
        cb.place(x=50, y=20)

    def on_click(self):
        if self.var.get():
            self.master.title("Widgets - CheckButton")
        else:
            self.master.title("")

def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
