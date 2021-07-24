import tkinter as tk
from tkinter import ttk

import reflection_questions.design as drq

class TextQuestion:
    """A question and a textbox to answer it."""
    def __init__(self, question, parent) -> None:
        self.label = ttk.Label(parent, text=question)
        self.textbox = tk.Text(parent)

    def show(self, c, r):
        """Show the question and answer on screen."""
        self.label.grid(column=c, row=r)
        self.textbox.grid(column=c, row=r+1)
        

root = tk.Tk()
design_reflection = ttk.Frame(root)
design_reflection.grid(column=0, row=0)
ttk.Label(design_reflection, text='Design: Reflection').grid()
TextQuestion(drq.RESEARCH_PURPOSE, design_reflection).show(0, 2)
TextQuestion(drq.SOCIAL_CONTEXT, design_reflection).show(0, 4)
TextQuestion(drq.PERSONAL_BENEFIT, design_reflection).show(0, 6)
TextQuestion(drq.WHO_HARM, design_reflection).show(0, 8)
TextQuestion(drq.WORST_CASE, design_reflection).show(0, 10)



root.mainloop()
