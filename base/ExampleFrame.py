from tkinter import BOTH
from tkinter.ttk import Frame, Style


class ExampleFrame(Frame):
    def __init__(self, title="Example", w=450, h=680):
        super(ExampleFrame, self).__init__()

        self.style = Style()
        # ('clam', 'alt', 'default', 'classic')
        self.style.theme_use("clam")

        self.master.title(title)
        self.pack(fill=BOTH, expand=True)
        self.center_window(w, h)

        self.init_ui()

    def init_ui(self):
        pass

    def center_window(self, w=960, h=680):
        sw = self.master.winfo_screenwidth()
        sh = self.master.winfo_screenheight()

        x = int((sw - w) / 2)
        y = int((sh - h) / 2)
        self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))

