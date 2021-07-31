"""The reflection screen classes and helper classes."""
import tkinter as tk
from tkinter import ttk
import datetime
import reflection_questions.design as drq
import reflection_questions.collection as crq


class ReflectionPage(ttk.Frame):
    """A general page of reflection questions."""
    
    

    def __init__(self, parent, controller) -> None:
        ttk.Frame.__init__(self, parent)
        ttk.Button(self, text='Return to session home', command=lambda: controller.show_frame(
            'SessionHomePage')).grid(column=0, row=0)
        ttk.Button(self, text='Save responses', command=self.save).grid(column=1, row=2)
        self.controller = controller
        self.canvas = tk.Canvas(self)
        self.canvas.grid(column=0, row=1, sticky='nsew')
        scrollbar = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.grid(column=1, row=0, sticky='ns')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.question_frame = ttk.Frame(self.canvas)
        self.canvas.create_window(0, 0, window=self.question_frame, anchor='nw')
        

        self.question_frame.bind('<Configure>', self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))

        self.text_questions = {}

    def save(self):
            # TODO: Make file names more specific, exception handling
            with open(self.controller.session_dir + "/" + type(self).__name__ + str(datetime.date.today()) +'.txt', 'w') as save_file:
                for question in self.text_questions:
                    save_file.write('# ' + question + '\n' + self.text_questions[question].textbox.get(1.0, tk.END) + '\n\n')

        

    
    

class DesignReflectionPage(ReflectionPage):
    """A reflection page for design."""

    def __init__(self, parent, controller) -> None:
        ReflectionPage.__init__(self, parent, controller)
        questions = [drq.RESEARCH_PURPOSE, drq.SOCIAL_CONTEXT,
                     drq.PERSONAL_BENEFIT, drq.WHO_HARM, drq.WORST_CASE]
        ttk.Label(self.question_frame, text='Design: Reflection').grid(
            column=0, row=0)
        self.text_questions = {question: tq for question, tq in zip(
            questions, map(lambda q: TextQuestion(self.question_frame, q), questions))}
        for i, text_question in enumerate(self.text_questions.values(), 1):
            text_question.show(0, 2*i)
    
    def save(self):
        super().save()


class CollectionReflectionPage(ReflectionPage):
    """A reflection for data collection."""

    def __init__(self, parent, controller) -> None:
        ReflectionPage.__init__(self, parent, controller)
        questions = [crq.INTERSECTIONAL_DATA, crq.MOST_REPPED, crq.LEAST_REPPED]
        ttk.Label(self.question_frame, text='Collection: Reflection').grid(
            column=0, row=0)
        text_questions = {question: tq for question, tq in zip(
            questions, map(lambda q: TextQuestion(self.question_frame, q), questions))}
        for i, text_question in enumerate(text_questions.values(), 1):
            text_question.show(0, 2*i)
    

class TextQuestion:
    """A question and a textbox to answer it."""

    def __init__(self, parent, question) -> None:
        self.label = ttk.Label(parent, text=question, wraplength='20cm')
        self.textbox = tk.Text(parent)

    def show(self, column, row):
        """Show the question and answer on screen."""
        self.label.grid(column=column, row=row, sticky='ew')
        self.textbox.grid(column=column, row=row+1, sticky='ew')
