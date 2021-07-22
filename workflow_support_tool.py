from tkinter import *
from tkinter import ttk

class App(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        self.grid(column=0, row=0)
        # TODO: make the app open on the start page
        SessionHome(self)
        

class StartPage:
    pass

class SessionHome:
    def __init__(self, parent):
        session = ttk.Frame(parent)
        session.grid(column=0, row=0)
        design = ttk.Labelframe(session, text='Design')
        data_collection = ttk.Labelframe(session, text='Data Collection')
        cleaning = ttk.Labelframe(session, text='Cleaning')
        explore = ttk.Labelframe(session, text='Explore')
        model = ttk.Labelframe(session, text='Model')
        interpret = ttk.Labelframe(session, text='Interpret')

        design.grid(column=0, row=0)
        data_collection.grid(column=1, row=0)
        cleaning.grid(column=2, row=0)
        explore.grid(column=0, row=1)
        model.grid(column=1, row=1)
        interpret.grid(column=2, row=1)

        design_reflection = ttk.Button(design, text='Reflection')
        design_reflection.grid(column=1, row=0)

        design_reflection_screen = ttk.Frame(design, )
        

# class DesignReflectionPage(ttk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

    
#     pass

root = Tk()
root.title = 'QUINTA Workflow Support Tool'
App(root)
root.mainloop()