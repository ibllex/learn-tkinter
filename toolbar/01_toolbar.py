from tkinter import Tk, Menu, Frame, Button
from tkinter import RAISED, FLAT, LEFT, TOP, X
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Toolbar", 480, 200)

    def init_ui(self):
        menubar = Menu(self.master)

        file_menu = Menu(menubar)

        file_menu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=file_menu)

        toolbar = Frame(self.master, bd=1, relief=RAISED)
        exit_btn = Button(toolbar, relief=FLAT,text="Q", command=self.quit)
        exit_btn.pack(side=LEFT, padx=2, pady=2)

        toolbar.pack(side=TOP, fill=X)
        self.master.config(menu=menubar)
        self.pack()

    def on_exit(self):
        self.quit()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
