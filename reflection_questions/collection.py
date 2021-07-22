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

INTERSECTIONAL_DATA = 'Are your data intersectional? Why or why not? Remember' \
    'that the experiences associated with one identity a person has' \
    'are not necessarily independent of or separate from another identity of' \
    'that person. How well can your dataset reflect this?'

MOST_REPPED = 'Think about the intersectional identities that are the most ' \
    'represented. Who is being centered in the data? Why? How might this ' \
    'affect the equity of your analysis?'

LEAST_REPPED = 'Think about the intersectional identities that are the least ' \
    'represented. Who is being centered in the data? Why? How might this ' \
    'affect the equity of your analysis?'
