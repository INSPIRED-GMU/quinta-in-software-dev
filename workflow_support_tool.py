from tkinter import *
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column=0, row=0)
        Label(self, text='Hello').grid(column=0, row=0)
        ttk.Labelframe(self, text='Design').grid(column=0, row=0)
        ttk.Labelframe(self, text='Data Collection').grid(column=1, row=0)
        ttk.Labelframe(self, text='Cleaning').grid(column=2, row=0)
        ttk.Labelframe(self, text='Explore').grid(column=0, row=1)
        ttk.Labelframe(self, text='Model').grid(column=1, row=1)
        ttk.Labelframe(self, text='Interpret').grid(column=2, row=1)
        StartPage(self)
        

class StartPage: # TODO: Create the start page 
    def __init__(self, parent):
        start_frame = Frame(parent)
        start_frame.grid(column=0, row=0)
        design = ttk.Labelframe(start_frame, text='Design')
        data_collection = ttk.Labelframe(start_frame, text='Data Collection')
        cleaning = ttk.Labelframe(start_frame, text='Cleaning')
        explore = ttk.Labelframe(start_frame, text='Explore')
        model = ttk.Labelframe(start_frame, text='Model')
        interpret = ttk.Labelframe(start_frame, text='Interpret')

        design.grid(column=0, row=0)
        data_collection.grid(column=1, row=0)
        cleaning.grid(column=2, row=0)
        explore.grid(column=0, row=1)
        model.grid(column=1, row=1)
        interpret.grid(column=2, row=1)

        design_reflection = ttk.Button(design, text='Reflection')
        design_reflection.grid(column=1, row=0)


class SessionHome:
    pass

class DesignReflectionPage:
    pass

root = Tk()
root.title = 'QUINTA Workflow Support Tool'
App(root)
root.mainloop()