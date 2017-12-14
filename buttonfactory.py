import tkinter as tk


class ButtonFactory:
    """ Button Builder """
    def create_button(self, type_):
        return button_types[type_]()


class ButtonBase:
    """ Base class """
    relief = 'flat'
    foreground = 'white'

    def get_button_config(self):
        return self.relief, self.foreground


class ButtonRidge(ButtonBase):
    relief = 'ridge'
    foreground = 'red'


class ButtonSunken(ButtonBase):
    relief = 'sunken'
    foreground = 'blue'


class ButtonGroove(ButtonBase):
    relief = 'groove'
    foreground = 'green'


button_types = [ButtonRidge, ButtonSunken, ButtonGroove]


class Main:
    def __init__(self):
        self.win = tk.Tk()
        self.win.title("Button Factory")
        self.create_widgets()

    def run(self):
        self.win.mainloop()

    def create_widgets(self):
        bf = ButtonFactory()

        # button 1
        rel = bf.create_button(0).get_button_config()[0]
        fg = bf.create_button(0).get_button_config()[1]
        action = tk.Button(self.win, text='Button'+str(0+1), relief=rel, foreground=fg)
        action.grid(column=0, row=1)

        # button 2
        rel = bf.create_button(1).get_button_config()[0]
        fg = bf.create_button(1).get_button_config()[1]
        action = tk.Button(self.win, text='Button' + str(1 + 1), relief=rel, foreground=fg)
        action.grid(column=1, row=1)

        # button 1
        rel = bf.create_button(2).get_button_config()[0]
        fg = bf.create_button(2).get_button_config()[1]
        action = tk.Button(self.win, text='Button' + str(2 + 1), relief=rel, foreground=fg)
        action.grid(column=2, row=1)


if __name__ == '__main__':
    app = Main()
    app.run()
