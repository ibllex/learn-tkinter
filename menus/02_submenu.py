from tkinter import Tk, Menu
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Menus - Submenu", 480, 200)

    def init_ui(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        file_menu = Menu(menubar)

        sub_menu = Menu(file_menu)
        sub_menu.add_command(label="Bookmarks")
        sub_menu.add_command(label="Load from plain text")
        file_menu.add_cascade(label="Import", menu=sub_menu)

        file_menu.add_separator()

        file_menu.add_command(label="Exit", command=self.on_exit)
        menubar.add_cascade(label="File", menu=file_menu)

    def on_exit(self):
        self.quit()


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
