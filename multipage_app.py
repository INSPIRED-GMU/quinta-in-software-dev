"""
The main code for the QUINTA workflow support tool app.
"""

import tkinter as tk
from tkinter import ttk
import reflection_pages as rp
import representation_analysis as ra


class App(tk.Tk):
    """The main app, which contains all of the frames for each screen."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title('Quintessence')
        self.session_dir = ''
        # Attribution for frame stacking skeleton:
        # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
        container = ttk.Frame(self)
        container.grid()

        self.frames = {}
        for frame_class in (ChooseSessionPage, SessionHomePage, rp.DesignReflectionPage,
                            ra.CollectionRepresentationAnalysis,
                            rp.CollectionReflectionPage, rp.CleaningReflectionPage,
                            ra.ComparativeRepresentationAnalysis,
                            rp.ExploreReflectionPage, rp.ModelReflectionPage,
                            rp.InterpretReflectionPage):
            page_name = frame_class.__name__
            frame = frame_class(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('ChooseSessionPage')

    def show_frame(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames[page_name]
        frame.tkraise()


class ChooseSessionPage(ttk.Frame):
    """The page that lets the user create a new session or create an existing session."""

    def __init__(self, parent, controller) -> None:
        super().__init__(parent)
        self.controller = controller
        ttk.Label(
            self, text=('Welcome to Quintessence, a workflow support tool '
                        'for Quantitative Intersectional Data (QUINTA).')
        ).grid(column=0, row=0, sticky='nsew')
        ttk.Button(self, text='Choose a session folder',
                   command=self.open_session_folder
                   ).grid(column=0, row=2)

    def open_session_folder(self):
        """Create a session folder."""
        self.controller.session_dir = tk.filedialog.askdirectory()
        if self.controller.session_dir != '':
            self.controller.show_frame('SessionHomePage')
        else:
            ttk.Label(self, text='You must select a folder to continue.',
                      foreground='red').grid(column=0, row=1)


class SessionHomePage(ttk.Frame):
    """The homepage of a session that lets users navigate between steps."""
    BUTTON_COL = 1

    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.step_labelframes = {}
        self.ds_processes = ['Design', 'Collection', 'Cleaning',
                             'Explore', 'Model', 'Interpret']
        # Create labelframes to hold the menu for each data science process
        for step in self.ds_processes:
            self.step_labelframes[step] = ttk.LabelFrame(self, text=step)
        # Grid each labelframe
        row_length = int(len(self.step_labelframes)/2)
        for i, step in enumerate(self.step_labelframes):
            self.step_labelframes[step].grid(column=(i if i < row_length else i - row_length),
                                             row=(1 if i < len(
                                                 self.step_labelframes)/2 else 2),
                                             sticky='nsew')

        # The column the button goes in is a constant in case we add more information
        # to other columns that makes us have to move all of the buttons over.

        # Design menu. TODO: Make button take user to reflection page
        ttk.Button(self.step_labelframes['Design'],
                   text='Reflection', command=lambda: controller.show_frame(
            'DesignReflectionPage')).grid(column=SessionHomePage.BUTTON_COL, row=0,
                                          sticky='ew')

        # Data collection menu
        ttk.Button(self.step_labelframes['Collection'],
                   text='Representation analysis',
                   command=lambda: controller.show_frame(
                       'CollectionRepresentationAnalysis')
                   ).grid(column=SessionHomePage.BUTTON_COL, row=0, sticky='ew')
        ttk.Button(self.step_labelframes['Collection'],
                   text='Reflection',
                   command=lambda: controller.show_frame(
                       'CollectionReflectionPage')
                   ).grid(column=SessionHomePage.BUTTON_COL, row=1, sticky='ew')

        # Cleaning
        ttk.Button(self.step_labelframes['Cleaning'],
                   text='Reflection',
                   command=lambda: controller.show_frame(
                       'CleaningReflectionPage')
                   ).grid(column=SessionHomePage.BUTTON_COL, row=0, sticky='ew')
        ttk.Button(self.step_labelframes['Cleaning'],
                   text='Comparative representation analysis',
                   command=lambda: controller.show_frame(
                       'ComparativeRepresentationAnalysis')
                   ).grid(column=SessionHomePage.BUTTON_COL, row=1, sticky='ew')

        # Explore
        ttk.Button(self.step_labelframes['Explore'], text='Reflection',
                   command=lambda: controller.show_frame(
                       'ExploreReflectionPage')
                   ).grid(column=SessionHomePage.BUTTON_COL, row=0, sticky='ew')

        # Model
        ttk.Button(self.step_labelframes['Model'], text='Intersectional accuracy',
                   command=lambda: controller.show_frame(
                       'ModelReflectionPage')
                       ).grid(column=SessionHomePage.BUTTON_COL, row=0, sticky='ew')

        ttk.Button(self.step_labelframes['Model'], text='Reflection',
                   command=lambda: controller.show_frame(
                       'ModelReflectionPage')
                       ).grid(column=SessionHomePage.BUTTON_COL, row=1, sticky='ew')

        # Interpret
        ttk.Button(self.step_labelframes['Interpret'], text='Reflection',
                   command=lambda: controller.show_frame(
                       'InterpretReflectionPage')
                       ).grid(column=SessionHomePage.BUTTON_COL, row=0, sticky='ew')


if __name__ == '__main__':
    app = App()
    app.mainloop()
