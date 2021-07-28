"""
The main code for the QUINTA workflow support tool app.
"""

import tkinter as tk
from tkinter import ttk
import pandas as pd

import data_exploration_utils as deu
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
        for frame_class in (ChooseSessionPage, SessionHomePage, DesignReflectionPage,
                            CollectionRepresentationAnalysis):
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
                   text='Representation analysis',
                   command=lambda: controller.show_frame(
                       'CollectionRepresentationAnalysis')
                   ).grid(column=button_col, row=0)
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
        self.canvas = tk.Canvas(self)
        self.canvas.grid(column=0, row=0, sticky='nsew')
        scrollbar = ttk.Scrollbar(
            self, orient=tk.VERTICAL, command=self.canvas.yview)
        scrollbar.grid(column=1, row=0, sticky='ns')
        self.canvas.configure(yscrollcommand=scrollbar.set)
        self.question_frame = ttk.Frame(self.canvas)
        self.question_frame.grid(column=0, row=0, sticky='nsew')
        self.question_frame.bind('<Configure', self.canvas.configure(
            scrollregion=self.canvas.bbox('all')))


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


class Data:
    """Represents a dataset, """

    def __init__(self, filepath, data_format) -> None:
        self.data_format = data_format
        self.data = self.read_data(filepath)
        self.listbox = tk.Listbox()
        self.selected_cols = []

    def set_selected_cols(self, cols):
        """Set selected_cols."""
        self.selected_cols = cols

    def read_data(self, file_path):
        """Return a pandas.DataFrame that reads data in the right format."""
        data_format = self.data_format.get()
        read_func = pd.read_csv
        if data_format == 'CSV':
            read_func = pd.read_csv
        elif data_format == 'TSV':
            read_func = pd.read_table
        elif data_format == 'JSON':
            read_func = pd.read_json
        elif data_format == 'Excel':
            read_func = pd.read_excel
        try:
            return read_func(file_path)
        except FileNotFoundError:
            pd.DataFrame()

    def col_listbox(self, parent):
        """Create a listbox from the data headers that is the child of parent."""
        columns_var = tk.StringVar(value=list(self.data.columns))
        self.listbox = tk.Listbox(
            parent, listvariable=columns_var, selectmode='extended')


class RepresentationAnalysis(ttk.Frame):
    """A general frame for reprsentation analysis."""

    def __init__(self, parent, controller) -> None:
        ttk.Frame.__init__(self, parent)
        self.controller = controller
        self.radiobutton_frame = ttk.Frame(self)
        self.radiobutton_frame.grid(column=0, row=1)
        self.data_format = tk.StringVar()
        self.data_object = None
        self.file_format_radio_buttons = {file_format: ttk.Radiobutton(self.radiobutton_frame,
                                                                       text=file_format,
                                                                       variable=self.data_format,
                                                                       value=file_format)
                                          for file_format in ['CSV', 'TSV', 'JSON', 'Excel']}

        for i, file_format in enumerate(self.file_format_radio_buttons):
            self.file_format_radio_buttons[file_format].grid(
                column=0, row=i, sticky='ns')
                
        ttk.Button(self, text='Return to session home', command=lambda: controller.show_frame(
            'SessionHomePage')).grid(column=1, row=0)

    def plot_rep_pie(self, dataframe, col_list):
        """Plot intersectional representation."""
        deu.intersectional_rep_pie(
            dataframe, col_list, self).get_tk_widget().grid(column=2, row=2)

    def set_data_object(self) -> None:
        """Return"""
        self.data_object = Data(tk.filedialog.askopenfilename(),
                                self.data_format)


class CollectionRepresentationAnalysis(RepresentationAnalysis):
    """The collection representation analysis screen."""

    def __init__(self, parent, controller) -> None:
        RepresentationAnalysis.__init__(self, parent, controller)
        ttk.Label(self, text='Representation analysis').grid(column=0, row=0)

        plot_button = ttk.Button(self, text='Plot representation', state=['disabled'], command=lambda: self.plot_rep_pie(
            self.data_object.data, list(self.data_object.listbox.curselection())).grid(column=2, row=0))
        load_button = ttk.Button(self, text='Load dataset',
                                 command=lambda: [self.set_data_object(), self.data_object.col_listbox(
                                     self), self.data_object.listbox.grid(column=1, row=1, sticky='nsew'), plot_button.state(['!disabled'])]
                                 )
        load_button.grid(column=0, row=2)
        plot_button.grid(column=1, row=2)


if __name__ == "__main__":
    app = App()
    app.mainloop()
