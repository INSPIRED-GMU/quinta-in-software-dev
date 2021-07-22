from tkinter import *
from tkinter import ttk

class App(Tk):
    def __init__(self):
        self.title = 'QUINTA Workflow Support Tool'
        self.grid(column=0, row=0)
        SessionHome(self)
        

class StartPage:
    pass

class SessionHome:
    def __init__(self, parent):
        # Create a frame to hold all the widgets for the session
        session = Frame(parent)
        session.grid(column=0, row=0)

        # Create labelframes to hold buttons for each step of DS
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
        data_collect_rep_analysis = ttk.Button(design,
                                               text='Represenatation analysis')
        data_collect_rep_analysis.grid(column=1, row=0)
        

class DesignReflectionPage:
    pass

class DataCollectionRepresentationAnalysisPage:
    """Visualize intersectional representation in a dataset."""
    pass


App().mainloop()

