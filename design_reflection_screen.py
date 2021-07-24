import tkinter as tk
from tkinter import ttk
from tkinter.constants import END, VERTICAL
from datetime import date

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

# design_reflection.bind('<Configure>', lambda canvas=canvas: canvas.configure(scrollregion=canvas.bbox('all')))


design_reflection.grid(column=0, row=0)
ttk.Label(design_reflection, text='Design: Reflection').grid()

questions = [drq.RESEARCH_PURPOSE, drq.SOCIAL_CONTEXT, drq.PERSONAL_BENEFIT, drq.WHO_HARM, drq.WORST_CASE]

text_questions = {question: tq for question, tq in zip(questions, 
map(lambda q: TextQuestion(q, design_reflection), questions))}
for i, tq in enumerate(text_questions.values(), 1):
    tq.show(0, 2*i)

# TODO: store answers in markdown file with questions as headings
# Make a save button. Store answers in markdown file when saved

switch = False


def save():
    # TODO: Make file names more specific, exception handling
    with open('session/design_reflection_responses' + str(date.today()) +'.txt', 'w') as save_file:
        for question in text_questions:
            save_file.write('# ' + question + '\n' + text_questions[question].textbox.get(1.0, END) + '\n\n')


ttk.Button(design_reflection, text='Save', command=save).grid(column=3, row=0)



root.mainloop()
