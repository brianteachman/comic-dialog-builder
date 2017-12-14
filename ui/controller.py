import tkinter as tk

from ui.view import View


class Controller(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        parent.title("Controller")
        self.view = View(parent)


if __name__ == "__main__":
    root = tk.Tk()
    Controller(root)
    root.mainloop()

