import tkinter as tk
from tkinter import ttk

import reflection_questions.design as drq

class Session(ttk.Frame):
    """The main session screen."""
    def __init__(self, parent):
        self.parent = parent
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

    def switch_to_design(self):
        self.grid_forget()
        DesignReflectionScreen(self.parent).grid(column=0, row=0)
        
class DesignReflectionScreen(ttk.Frame):
    """A screen of reflection questions for the Design phase."""
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent)
        research_purpose = TextQuestion(drq.RESEARCH_PURPOSE, parent)
        research_purpose.show(0, 1)

class TextQuestion:
    """A question and a textbox to answer it."""
    def __init__(self, question, parent) -> None:
        self.label = ttk.Label(parent, text=question)
        self.textbox = tk.Text(parent)

    def show(self, c, r):
        """Show the question and answer on screen."""
        self.label.grid(column=c, row=r)
        self.textbox.grid(column=c, row=r+1)
        
class PhaseMenu(ttk.Labelframe):
    """A menu for the phase."""
    def __init__(self, parent, buttons):
        ttk.Labelframe.__init__(self, parent)
        for i, button_text, frame in buttons:
            ttk.Button(self, text=button_text, command=lambda parent, self: replace_frame(parent, self)).grid(column=0, row=i)


def replace_frame(frame1, frame2):
    """Replace frame1 with frame2 on screen."""
    frame1.grid_forget()
    frame2.grid(column=0, row=0)

root = tk.Tk()
session = Session(root).grid(column=0,  row=0)

root.mainloop()