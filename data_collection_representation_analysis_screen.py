import tkinter as tk
from tkinter import ttk
from matplotlib.pyplot import text
import pandas as pd

import data_exploration_utils as deu


root = tk.Tk()
mainframe = ttk.Frame(root)
mainframe.grid()

ttk.Label(mainframe, text='Representation Analysis').grid(column=0, row=0)

# Create a tk.StringVar to hold the filename from the filedialog
ttk.Label(mainframe, text='Choose a file format:').grid(column=0, row=1)
filepath = tk.StringVar()
tk.Button(mainframe, text='Load dataset', command= lambda: [filepath.set(
    tk.filedialog.askopenfilename()), Data(filepath.get(), format), col_listbox(mainframe), 
    listbox.grid(column=1, row=2)]).grid(column=0, row=5)

# Create radiobuttons for file formats
radiobutton_frame = ttk.Frame(mainframe)
radiobutton_frame.grid(column=0, row=2)
format = tk.StringVar()
file_format_radio_buttons = {file_format: ttk.Radiobutton(radiobutton_frame,
  text=file_format, variable=format, value=file_format) 
  for file_format in ['CSV', 'TSV', 'JSON', 'Excel']}
for i, ff in enumerate(file_format_radio_buttons):
    file_format_radio_buttons[ff].grid(column=0, row=i)

def read_data(file_path, format_string_var):
    """Return a pandas.DataFrame that reads data in the right format."""
    format = format_string_var.get()
    read_func = pd.read_csv
    if format == 'CSV':
        read_func = pd.read_csv
    elif format == 'TSV':
        read_func = pd.read_table
    elif format == 'JSON':
        read_func = pd.read_json
    elif format == 'Excel':
        read_func = pd.read_excel
    try:
        return read_func(file_path)
    except FileNotFoundError:
        pass



def plot_rep_pie(df, col_list, parent):
    """Plot intersectional representation."""
    deu.intersectional_rep_pie(df, col_list, parent).get_tk_widget().grid(column=2, row=2)



class Data:
    data = pd.DataFrame()
    def __init__(self, filepath, format) -> None:
        Data.data = read_data(filepath, format)
        self.selected_cols = []
    def set_selected_cols(self, cols):
        self.selected_cols = cols


# Make a listbox out of the column headers of the table
def col_listbox(parent):
    global listbox
    columns_var = tk.StringVar(value=list(Data.data.columns))
    listbox = tk.Listbox(parent, listvariable=columns_var, selectmode='extended')


ttk.Button(mainframe, text='''See what's selected''', command=lambda: print(listbox.curselection())).grid(column=4, row=4)
ttk.Button(mainframe, text='Plot representation', command=lambda: plot_rep_pie(Data.data, 
    list(listbox.curselection()), mainframe)).grid(column=3, row=0)
   

    

root.mainloop()
