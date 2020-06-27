from tkinter import Frame, Tk, BOTH, Text, Menu, END
from tkinter import filedialog
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Dialog - Color Chooser", 480, 200)

    def init_ui(self):
        menubar = Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu = Menu(menubar)
        fileMenu.add_command(label="Open", command=self.on_open)
        menubar.add_cascade(label="File", menu=fileMenu)

        self.txt = Text(self)
        self.txt.pack(fill=BOTH, expand=1)

    def on_open(self):
        ftypes = [('Python files', '*.py'), ('All files', '*')]
        dlg = filedialog.Open(self, filetypes=ftypes)
        fl = dlg.show()

        if fl != '':
            text = self.read_file(fl)
            self.txt.insert(END, text)

    def read_file(self, filename):
        with open(filename, "r") as f:
            text = f.read()

        return text


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
