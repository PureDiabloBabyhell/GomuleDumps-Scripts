import os.path, time
import pathlib
import glob, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

computedData = ""
def computeUsingComboboxData():
	computedData  = "Data shall be computed using:\n"
	computedData += combo_files.get()
	computedData += "\n(dumped {0}) as data file and:\n".format(time.ctime(os.path.getmtime(combo_files.get())))
	computedData += combo_options.get()
	computedData += "\nas crunching option."
	text.delete("1.0", "end")
	text.insert(tk.END, computedData)
	print("computeUsingComboboxData processed")

def deleteDumps():
	confirmed = messagebox.askokcancel("Confirmation request", "Do you really want to delete all .d2x.txt files?")
	print("{0}".format(confirmed))
	if confirmed == True:
		print("step in")
		dumps = glob.iglob("*.d2x.txt")
		for dump in dumps:
			os.remove(dump)
		myList = list(pathlib.Path('.').glob('*.d2x.txt'))

window = tk.Tk()
window.title("GoMule Dumps Cruncher")
window.rowconfigure([0, 1, 2], minsize=30, weight=1)
window.columnconfigure(0, minsize=80, weight=1)

fontStyle = tkFont.Font(family="Courier", size=14)

frame_configurable_data = tk.Frame(window)
frame_configurable_data.grid(row=0, column=0)
currentColumn = 0

crunchButton = tk.Button(
	master=frame_configurable_data,
	text="Crunch!",
	command=computeUsingComboboxData
)
crunchButton.grid(row=0, column=currentColumn)
currentColumn += 1

myList = list(pathlib.Path('.').glob('*.d2x.txt'))
combo_files = ttk.Combobox(frame_configurable_data, values=myList, state="readonly")
combo_files.grid(row=0, column=currentColumn)
currentColumn += 1
combo_files.current(0)

label_as = tk.Label(frame_configurable_data, text=" as ")
label_as.grid(row=0, column=currentColumn)
currentColumn += 1

myCrunchingOptionsList = ["Runes","Gems","Sets/Uniques","Charms","Jewels","Mixed"]
combo_options = ttk.Combobox(frame_configurable_data, values=myCrunchingOptionsList, state="readonly")
combo_options.grid(row=0, column=currentColumn)
currentColumn += 1
combo_options.current(0)

deleteButton = tk.Button(
	master=frame_configurable_data,
	text="Delete all dumps",
	command=deleteDumps
)
deleteButton.grid(row=0, column=currentColumn+5)

currentLine = 0
text = tk.Text(window)
text.grid(row=1, column=0)

text.insert("{0}.0".format(currentLine), computedData)
currentLine += 1
	
window.mainloop()