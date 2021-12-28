"""This module contains data analysis screens and their parts.

Classes:
Data--A dataset with its file format, columns of interest, dataframe, and Tk.Listbox.
RepresentationAnalysis--A ttk.Frame associated with a Data object and plotting functions.
CollectionRepresentationAnalysis--A ttk.Frame for drawing a pie chart of a dataset.
ComparativeRepresentationAnalysis--A ttk.Frame for drawing pie charts of two datasets and
    visualizing changes in representation.
"""
import tkinter as tk
from tkinter import ttk
import pandas as pd

import data_exploration_utils as deu


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
        """Create a frame associated with a dataset and its visualization.

        Instance variables:
        controller
        button_frame -- a
        """
        super().__init__(parent)
        self.controller = controller
        self.button_frame = ttk.Frame(self)
        self.button_frame.grid(column=0, row=1)
        self.radiobutton_frame = ttk.Frame(self.button_frame)
        self.radiobutton_frame.grid(column=0, row=0)
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
        
  

    def create_listbox(self, column=1, row=1):
        """Create and grid a listbox from self.data_object."""
        self.set_data_object()
        self.data_object.col_listbox(self)
        self.data_object.listbox.grid(column=column, row=row, sticky='nsew')
        self.data_object.listbox.bind('<<ListboxSelect>>', 
        lambda e: (self.set_selected_cols()))
        # if list(self.data_object.listbox.curselection()) != [] else self.data_object.selected_cols))

    def set_selected_cols(self):
        if list(self.data_object.listbox.curselection()) != []:
            self.data_object.selected_cols = list(self.data_object.listbox.curselection())
            

    

    def plot_rep_pie(self):
        """Plot intersectional representation."""
        selected_cols = list(self.data_object.listbox.curselection())
        deu.intersectional_rep_pie(
            self.data_object.data, selected_cols, self).get_tk_widget().grid(column=2, row=1)
        missed_intersects = deu.missed_intersects(
            self.data_object.data, selected_cols)
        if missed_intersects != set():
            ttk.Label(self, text='The following identities are not represented: ' +
                      str(missed_intersects), foreground='red').grid(column=2, row=2)

    def set_data_object(self) -> None:
        """Return"""
        self.data_object = Data(tk.filedialog.askopenfilename(),
                                self.data_format)


class CollectionRepresentationAnalysis(RepresentationAnalysis):
    """The collection representation analysis screen. Also used in Comparative."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent, controller)
        ttk.Button(self, text='Return to session home', command=lambda: controller.show_frame(
            'SessionHomePage')).grid(column=1, row=0)
        ttk.Label(self, text='Representation analysis').grid(column=0, row=0)

        plot_button = ttk.Button(self, text='Plot representation', state=[
                                 'disabled'], command=self.plot_rep_pie)
        load_button = ttk.Button(self.button_frame, text='Load dataset',
                                 command=lambda: [self.create_listbox(
                                 ), plot_button.state(['!disabled'])]
                                 )
        load_button.grid(column=0, row=1)
        plot_button.grid(column=1, row=2)


class ComparativeRepresentationAnalysis(RepresentationAnalysis):
    """The representation analysis screen."""

    def __init__(self, parent, controller) -> None:
        """Create a new comparative representation analysis screen.

        The frame will allow the user to select two files and
        create a pie chart of intersectional representation in each,
        as well as create a bar chart that shows changes in relative
        representation between the files.
        """
        super().__init__(parent, controller)
        self.before_frame = CollectionRepresentationAnalysis(self, controller)
        self.before_frame.grid(column=0, row=1)
        self.after_frame = CollectionRepresentationAnalysis(self, controller)
        self.after_frame.grid(column=0, row=2)
        self.difference_frame = ttk.Frame(self)
        self.difference_frame.grid(column=1, row=0)
        ttk.Button(self.difference_frame, text='Plot relative change',
                   command=lambda: self.rel_change_bar(self.difference_frame)).pack()

    def rel_change_bar(self, parent):
        """Draw a barchart representing the relative change in representation."""
        # For debugging purposes, print data
        print(self.before_frame.data_object.data)
        print(self.after_frame.data_object.data)
        print('Before selection')
        print(self.before_frame.data_object.selected_cols)
        print('After selection')
        print(self.after_frame.data_object.selected_cols)
        
        deu.intersectional_rep_rel_change_bar(
            self.before_frame.data_object.data,
            self.after_frame.data_object.data,
            self.before_frame.data_object.selected_cols,
            self.after_frame.data_object.selected_cols,
            parent
        ).get_tk_widget().pack()
