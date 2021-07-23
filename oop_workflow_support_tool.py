import tkinter as tk
from tkinter import ttk

from reflection_questions.design import *

class Session(ttk.Frame):
    """The main session screen."""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        design = ttk.Labelframe(self, text='Design')
        data_collection = ttk.Labelframe(self, text='Data Collection')
        cleaning = ttk.Labelframe(self, text='Cleaning')
        explore = ttk.Labelframe(self, text='Explore')
        model = ttk.Labelframe(self, text='Model')
        interpret = ttk.Labelframe(self, text='Interpret')

        design.grid(column=0, row=0)
        data_collection.grid(column=1, row=0)
        cleaning.grid(column=2, row=0)
        explore.grid(column=0, row=1)
        model.grid(column=1, row=1)
        interpret.grid(column=2, row=1)
        
class DesignReflectionScreen(ttk.Frame):
    """A screen of reflection questions for the Design phase."""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        ttk.Label(self, text='Hello').grid(column=0, row=0)

class TextQuestion:
    """A question and a textbox to answer it."""
    def __init__(self, question, parent) -> None:
        self.question = question
        self.label = ttk.Label(parent, text=question)
        self.textbox = tk.Text(parent)
        
root = tk.Tk()
session = Session(root).grid(column=0,  row=0)
DesignReflectionScreen(session).grid(column=0, row=0)
root.mainloop()