from tkinter import Tk, Button
from tkinter import messagebox as mbox
from base.ExampleFrame import ExampleFrame


class Example(ExampleFrame):
    def __init__(self):
        super().__init__("Dialog - Message Box", 480, 200)

    def init_ui(self):
        error = Button(self, text="Error", command=self.on_error)
        error.grid(padx=5, pady=5)
        warning = Button(self, text="Warning", command=self.on_warn)
        warning.grid(row=1, column=0)
        question = Button(self, text="Question", command=self.on_quest)
        question.grid(row=0, column=1)
        inform = Button(self, text="Information", command=self.on_info)
        inform.grid(row=1, column=1)

    def on_error(self):
        mbox.showerror("Error", "Could not open file")

    def on_warn(self):
        mbox.showwarning("Warning", "Deprecated function call")

    def on_quest(self):
        mbox.askquestion("Question", "Are you sure to quit?")

    def on_info(self):
        mbox.showinfo("Information", "Download completed")


def main():
    root = Tk()
    app = Example()
    root.mainloop()


if __name__ == '__main__':
    main()
