"""The reflection screen classes and helper classes."""
import tkinter as tk
from tkinter import ttk
import datetime
import reflection_questions.design as drq
import reflection_questions.collection as crq
import reflection_questions.cleaning as clrq
import reflection_questions.explore as erq
import reflection_questions.model as mrq
import reflection_questions.interpret as irq


class ReflectionPage(ttk.Frame):
    """A general page of reflection questions."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent)

        buttons = ttk.Frame(self)
        ttk.Button(buttons, text='Return to session home', command=lambda: controller.show_frame(
            'SessionHomePage')).grid(column=0, row=0)
        ttk.Button(buttons, text='Save responses',
                   command=self.save).grid(column=1, row=0)
        buttons.pack()

        self.controller = controller
        self.canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(
            self, orient='vertical', command=self.canvas.yview)
        self.question_frame = ttk.Frame(self.canvas)
        self.question_frame.bind('<Configure>', self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))

        self.canvas.create_window(
            0, 0, window=self.question_frame, anchor='nw')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.canvas.pack(fill='both', side='left', expand=True)
        scrollbar.pack(side='right', fill='y', anchor='e')

        self.text_questions = {}

    def save(self):
        """Save the responses in all the text_questions to file in the session folder."""
        with open(self.controller.session_dir + "/" + type(self).__name__ +
                  str(datetime.datetime.today()) + '.txt', 'w') as save_file:
            for question in self.text_questions:
                save_file.write(
                    '# ' + question + '\n' +
                    self.text_questions[question].textbox.get(1.0, tk.END) + '\n\n')

    def grid_text_questions(self, questions):
        """Put the text questions on screen."""
        self.text_questions = {question: tq for question, tq in zip(
            questions, map(lambda q: TextQuestion(self.question_frame, q), questions))}
        for i, text_question in enumerate(self.text_questions.values(), 1):
            text_question.show(0, 2*i)


class DesignReflectionPage(ReflectionPage):
    """A reflection page for design."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller)
        questions = [drq.RESEARCH_PURPOSE, drq.SOCIAL_CONTEXT,
                     drq.PERSONAL_BENEFIT, drq.WHO_HARM, drq.WORST_CASE]
        ttk.Label(self.question_frame, text='Design: Reflection').grid(
            column=0, row=0, sticky='w')
        self.text_questions = {question: tq for question, tq in zip(
            questions, map(lambda q: TextQuestion(self.question_frame, q), questions))}
        for i, text_question in enumerate(self.text_questions.values(), 1):
            text_question.show(0, 2*i)


class CollectionReflectionPage(ReflectionPage):
    """A reflection for data collection."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller)
        questions = [crq.INTERSECTIONAL_DATA,
                     crq.MOST_REPPED, crq.LEAST_REPPED]
        ttk.Label(self.question_frame, text='Collection: Reflection').grid(
            column=0, row=0)
        self.grid_text_questions(questions)


class CleaningReflectionPage(ReflectionPage):
    """A reflection for data cleaning."""

    def __init__(self, parent, controller):
        super().__init__(parent, controller)
        questions = [clrq.RELATIVE_CHANGE, clrq.UNDERREPRESENT]
        self.grid_text_questions(questions)


class ExploreReflectionPage(ReflectionPage):
    """A reflection for exploration."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller)
        questions = [erq.USING_PROXIES, erq.HARM]
        self.grid_text_questions(questions)


class ModelReflectionPage(ReflectionPage):
    """A reflection for the model phase."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller)
        questions = [mrq.MOST_FAVORED, mrq.LEAST_FAVORED,
                     mrq.TREATMENT_SIMILARITIES, mrq.TREATMENT_DIFFERENCES]
        self.grid_text_questions(questions)


class InterpretReflectionPage(ReflectionPage):
    """A reflection page for the interpret phase."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller)
        questions = [irq.ENHANCED_STRUCT_INEQ, irq.HOW_INTERPRET]
        self.grid_text_questions(questions)


class TextQuestion:
    """A question and a textbox to answer it."""

    def __init__(self, parent, question) -> None:
        self.label = ttk.Label(parent, text=question, wraplength='20cm')
        self.textbox = tk.Text(parent)

    def show(self, column, row):
        """Show the question and answer on screen."""
        self.label.grid(column=column, row=row, sticky='ew')
        self.textbox.grid(column=column, row=row+1, sticky='ew')
