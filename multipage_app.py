"""
The main code for the QUINTA workflow support tool app.
"""

import tkinter as tk
from tkinter import ttk

from matplotlib.pyplot import text

import reflection_pages as rp
import representation_analysis as ra


class App(tk.Tk):
    """The main app, which contains all of the frames for each screen."""

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.session_dir = 'sample_session'  # TODO: make it ''
        # Attribution for frame stacking skeleton:
        # https://stackoverflow.com/questions/7546050/switch-between-two-frames-in-tkinter/7557028#7557028
        container = ttk.Frame(self)
        container.grid()

        self.frames = {}
        for frame_class in (ChooseSessionPage, SessionHomePage, rp.DesignReflectionPage,
                            ra.CollectionRepresentationAnalysis,
                            rp.CollectionReflectionPage, rp.CleaningReflectionPage,
                            rp.ExploreReflectionPage):
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
        ttk.Button(self, text='Create or open a session folder',
                   command=lambda: [self.open_session_folder(
                   ), controller.show_frame('SessionHomePage')]
                   ).grid(column=0, row=0, sticky='nsew')

        # TODO: Make button populate session screen with information

    def open_session_folder(self):
        """Creates a session folder."""
        self.controller.session_dir = tk.filedialog.askdirectory()


class SessionHomePage(ttk.Frame):
    """The homepage of a session that lets users navigate between steps."""

    def __init__(self, parent, controller):
        ttk.Frame.__init__(self, parent)
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
        BUTTON_COL = 1

        # Design menu. TODO: Make button take user to reflection page
        ttk.Button(self.step_labelframes['Design'],
                   text='Reflection', command=lambda: controller.show_frame(
            'DesignReflectionPage')).grid(column=BUTTON_COL, row=0,
                                          sticky='ew')

        # Data collection menu
        ttk.Button(self.step_labelframes['Collection'],
                   text='Representation analysis',
                   command=lambda: controller.show_frame(
                       'CollectionRepresentationAnalysis')
                   ).grid(column=BUTTON_COL, row=0, sticky='ew')
        ttk.Button(self.step_labelframes['Collection'],
                   text='Reflection',
                   command=lambda: controller.show_frame(
                       'CollectionReflectionPage')
                   ).grid(column=BUTTON_COL, row=1, sticky='ew')

        # Cleaning
        ttk.Button(self.step_labelframes['Cleaning'],
                   text='Reflection',
                   command=lambda: controller.show_frame(
                       'CleaningReflectionPage')
                   ).grid(column=BUTTON_COL, row=0, sticky='ew')
        ttk.Button(self.step_labelframes['Cleaning'],
                   text='Comparative representation analysis').grid(column=BUTTON_COL, row=1,
                                                                    sticky='ew')

        # Explore
        ttk.Button(self.step_labelframes['Explore'], text='Reflection',
                   command=lambda: controller.show_frame(
                       'ExploreReflectionPage')
                   ).grid(column=BUTTON_COL, row=0, sticky='ew')

        # Model
        ttk.Button(self.step_labelframes['Model'], text='Intersectional accuracy',
                   command=lambda: controller.show_frame(
                       'ModelReflectionPage')).grid(column=BUTTON_COL, row=0, sticky='ew')

        ttk.Button(self.step_labelframes['Model'], text='Reflection',
                   command=lambda: controller.show_frame(
                       'ModelReflectionPage', text='Reflection')).grid(column=BUTTON_COL, row=1, sticky='ew')

        # Interpret
        ttk.Button(self.step_labelframes['Interpret'], text='Reflection',
                   command=lambda: controller.show_frame(
                       'InterpretReflectionPage')).grid(column=BUTTON_COL, row=0, sticky='ew')


if __name__ == "__main__":
    app = App()
    app.mainloop()
