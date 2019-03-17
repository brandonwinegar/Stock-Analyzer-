from tkinter import *
from tkinter import ttk


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
        # A label at location 2,2 in the grid has it's textvariable set to meters
        # that value will automatically update on the window whenever that value is changed
    except ValueError:
        pass

# Creates a Main window and names it 'root'
root = Tk()
root.title("Feet to Meters")

# Creates a frame widget, which will hold the all of the content for the UI and attach it to the main window
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)   # Allows the frame to scale with the window if the size is changed
root.rowconfigure(0, weight=1)      # Allows the frame to scale with the window if the size is changed

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

# Setting 'textvariable' to one of the pre-defined StringVar objects  allow
# the label to update whenever 'meters' changes values
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()