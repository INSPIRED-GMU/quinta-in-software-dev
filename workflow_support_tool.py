from tkinter import *
from tkinter import ttk

class App:
    def __init__(self, root):
        root.title('QUINTA Workflow Suport Tool')

        mainframe = ttk.Frame(root) # TODO: add padding
        

class StartPage: # TODO: Create the start page 
    def __init__(self, root, mainframe):
        design = ttk.Labelframe(mainframe, text='Design')
        data_collection = ttk.Labelframe(mainframe, text='Data Collection')
        explore = ttk.Labelframe(mainframe, text='Explore')
        model = ttk.Labelframe(mainframe, text='Model')
        interpret = ttk.Labelframe(mainframe, text='Interpret')
        mainframe.grid()

class SessionHome:
    pass

class DesignReflectionPage:
    pass