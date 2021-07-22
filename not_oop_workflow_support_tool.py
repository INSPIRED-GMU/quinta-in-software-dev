import tkinter as tk
from tkinter import ttk


root = tk.Tk()
root.title = 'QUINTA Workflow Support Tool'
mainframe = ttk.Frame(root, padding=(3, 3, 12, 12))
mainframe.grid(column=0, row=0)


session = ttk.Frame(mainframe, padding=(3, 3, 12, 12))
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

design_reflection_screen = ttk.Frame(mainframe, padding=(3, 3, 12, 12))



design_reflection = ttk.Button(design, text='Reflection', command=design_reflection_screen.tkraise)
design_reflection.grid(column=1, row=0)
tk.Label(design_reflection_screen, text='Reflection question').grid(column=0, row=0)

design_reflection_screen.grid(column=0, row=0)

        

# class DesignReflectionPage(ttk.Frame):
#     def __init__(self, parent):
#         super().__init__(parent)

    
#     pass



root.mainloop()