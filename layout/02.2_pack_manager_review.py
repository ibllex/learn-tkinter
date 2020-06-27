from tkinter import Tk, LEFT, BOTH, X, N, Text
from tkinter.ttk import Frame, Label, Entry
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Pack Manager - Review", 450, 500)

    def init_ui(self):
        frame_01 = Frame(self)
        frame_01.pack(fill=X)

        label_01 = Label(frame_01, text="Title", width=6)
        label_01.pack(side=LEFT, padx=5, pady=5)

        entry_01 = Entry(frame_01)
        entry_01.pack(fill=X, padx=5, expand=True)

        frame_02 = Frame(self)
        frame_02.pack(fill=X)

        label_02 = Label(frame_02, text="Author", width=6)
        label_02.pack(side=LEFT, padx=5, pady=5)

        entry_02 = Entry(frame_02)
        entry_02.pack(fill=X, padx=5, expand=True)

        frame_03 = Frame(self)
        frame_03.pack(fill=BOTH, expand=True)

        label_03 = Label(frame_03, text="Review", width=6)
        label_03.pack(side=LEFT, anchor=N, padx=5, pady=5)

        txt = Text(frame_03)
        txt.pack(fill=BOTH, pady=5, padx=5, expand=True)


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
