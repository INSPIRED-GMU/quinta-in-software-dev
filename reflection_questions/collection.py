import tkinter as tk


# These possible attributes are from page 44 of Alicia Boyd's dissertation
# from a list that was not meant to be exhaustive
possible_attributes = tk.StringVar(value=['Race', 'Class', 'Gender',
                                          'Sexuality', 'Dis/ability',
                                          'Ethnicity', 'Nation', 'Religion',
                                          'Age'])
def listbox_attributes(parent):
    """Display a listbox of attributes included in the data"""
    return Listbox(parent, listvariable=possible_attributes)
