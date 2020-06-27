from tkinter import Tk, Menu
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Menus - Popup Menu", 480, 200)

    def init_ui(self):
        self.menu = Menu(self.master, tearoff=0)
        self.menu.add_command(label="Beep", command=self.bell)
        self.menu.add_command(label="Exit", command=self.on_exit)

        self.master.bind("<Button-3>", self.show_menu)
        self.pack()

    def on_exit(self):
        self.quit()

    def show_menu(self, e):
        self.menu.post(e.x_root, e.y_root)

def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
