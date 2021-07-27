"""
The main code for the QUINTA workflow support tool app.
"""
import tkinter as tk
from tkinter import ttk
from tkinter import font as tkfont

import reflection_questions.design as drq


class App(tk.Tk):
    """The main app, which contains all of the frames for each screen."""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Attribution for frame stacking skeleton: 
        # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
        container = ttk.Frame(self)
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for frame_class in (ChooseSessionPage, SessionHomePage, DesignReflectionPage):
            page_name = frame_class.__name__
            frame = frame_class(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        # TODO: make this ChooseSessionPage once built
        self.show_frame('SessionHomePage')

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class ChooseSessionPage(ttk.Frame):
    """The page that lets the user create a new session or create an existing session."""

    def __init__(self, parent, controller) -> None:
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        ttk.Label(self, text='Create a new session:').grid(column=0, row=0)
        # TODO: Add buttons to open sessions or create sessions.
        # These buttons should automaticallytake you to a session screen


class SessionHomePage(ttk.Frame):
    """The homepage of a session that lets users navigate between steps."""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.step_labelframes = {}
        self.ds_processes = ['Design', 'Collection', 'Cleaning',
                             'Exploring', 'Model', 'Interpret']
        # Create labelframes to hold the menu for each data science process
        for step in self.ds_processes:
            self.step_labelframes[step] = ttk.LabelFrame(self, text=step)
        # Grid each labelframe
        for i, step in enumerate(self.step_labelframes):
            self.step_labelframes[step].grid(column=i,
                                             row=(1 if i < len(
                                                 self.step_labelframes)/2 else 2),
                                             sticky='ns')
        button_col = 1

        # Design menu. TODO: Make button take user to reflection page
        ttk.Button(self.step_labelframes['Design'],
                   text='Reflection', command=lambda: controller.show_frame(
            'DesignReflectionPage')).grid(column=button_col, row=0,
                                          sticky='nsew')

        # Data collection menu
        ttk.Button(self.step_labelframes['Collection'],
                   text='Representation analysis').grid(column=button_col, row=0)
        ttk.Button(self.step_labelframes['Collection'],
                   text='Reflection').grid(column=button_col, row=1)

        # Cleaning
        ttk.Button(self.step_labelframes['Cleaning'],
                   text='Pre-reflection').grid(column=button_col, row=0)
        ttk.Button(self.step_labelframes['Cleaning'],
                   text='Comparative representation analysis').grid(column=button_col, row=1)
        ttk.Button(self.step_labelframes['Cleaning'],
                   text='Post-reflection').grid(column=button_col, row=2)


class ReflectionPage(ttk.Frame):
    """A general page of reflection questions."""

    def __init__(self, parent, controller) -> None:
        ttk.Frame.__init__(self, parent)
        ttk.Button(self, text='Return to session home', command=lambda: controller.show_frame(
            'SessionHomePage')).grid(column=1, row=0)
        self.controller = controller
        canvas = tk.Canvas(self)
        canvas.grid(column=0, row=0, sticky='nsew')
        scrollbar = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=canvas.yview)
        scrollbar.grid(column=1, row=0, sticky='ns')
        self.question_frame = ttk.Frame(canvas)
        self.question_frame.grid(column=0, row=0, sticky='nsew')


class DesignReflectionPage(ReflectionPage):
    """A reflection page for design."""

    def __init__(self, parent, controller) -> None:
        ReflectionPage.__init__(self, parent, controller)
        questions = [drq.RESEARCH_PURPOSE, drq.SOCIAL_CONTEXT,
                     drq.PERSONAL_BENEFIT, drq.WHO_HARM, drq.WORST_CASE]
        ttk.Label(self.question_frame, text='Design: Reflection').grid(
            column=0, row=0)
        text_questions = {question: tq for question, tq in zip(
            questions, map(lambda q: TextQuestion(self.question_frame, q), questions))}
        for i, text_question in enumerate(text_questions.values(), 1):
            text_question.show(0, 2*i)



class TextQuestion:
    """A question and a textbox to answer it."""

    def __init__(self, parent, question) -> None:
        self.label = ttk.Label(parent, text=question)
        self.textbox = tk.Text(parent)

    def show(self, column, row):
        """Show the question and answer on screen."""
        self.label.grid(column=column, row=row)
        self.textbox.grid(column=column, row=row+1)


if __name__ == "__main__":
    app = App()
    app.mainloop()
