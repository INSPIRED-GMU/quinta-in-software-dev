import tkinter as tk
from tkinter import mainloop, ttk
from tkinter.constants import VERTICAL

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

mainframe = ttk.Frame(root)
mainframe.grid()
canvas = tk.Canvas(mainframe)
canvas.grid()
design_reflection = ttk.Frame(canvas)
design_reflection.grid()

# TODO: fix scrollbar
scrollbar = ttk.Scrollbar(canvas, orient=VERTICAL, command=canvas.yview)
scrollbar.grid(column=2, row=0)
canvas.create_window(5, 5, window=design_reflection)
canvas.configure(yscrollcommand=scrollbar.set)

design_reflection.bind('<Configure>', lambda canvas=canvas: canvas.configure(scrollregion=canvas.bbox('all')))


design_reflection.grid(column=0, row=0)
ttk.Label(design_reflection, text='Design: Reflection').grid()

questions = [drq.RESEARCH_PURPOSE, drq.SOCIAL_CONTEXT, drq.PERSONAL_BENEFIT, drq.WHO_HARM, drq.WORST_CASE]
for i, question in [pair for pair in zip([2*x for x in range(1, len(questions)+1)], questions)]:
    TextQuestion(question, design_reflection).show(0, i)



root.mainloop()
