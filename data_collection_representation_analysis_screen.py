import tkinter as tk
from tkinter import ttk
import pandas as pd


import data_exploration_utils as deu



root = tk.Tk()

mainframe = ttk.Frame(root)
mainframe.grid()

# Create a tk.StringVar to hold the filename from the filedialog
filename = tk.StringVar()
tk.Button(mainframe, text='Load dataset', command= lambda: filename.set(
    tk.filedialog.askopenfilename())).grid()
format = tk.StringVar()
file_format_radio_buttons = {file_format: ttk.Radiobutton(mainframe,
 text=file_format, variable=format, value=file_format) for file_format in ['CSV', 'TSV', 'JSON', 'SQL']}
# TODO: make the file buttons actually change file format
for i, ff in enumerate(file_format_radio_buttons, 3):
    file_format_radio_buttons[ff].grid(column=0, row=i)

class PlotRep:
    """Plot intersectional representation."""
    def __init__(file_path, col_list, format_string_var, parent):
        format = format_string_var.get()
        if format == 'CSV':
            read_func = pd.read_csv
        elif format == 'TSV':
            read_func = pd.read_table
        elif format == 'JSON':
            read_func = pd.read_json
        elif format == 'SQL':
            read_func = pd.read_sql
        deu.intersectional_rep_pie(read_func(file_path), col_list, parent).grid(column=4, row=2)

    

root.mainloop()