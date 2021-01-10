#External libraries
import os.path, time
import pathlib
import glob, os
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import tkinter.font as tkFont

#Internal functionalities
import gemsCruncher
import runesCruncher
import charmsJewelsCruncher
import setUniquesCruncher

computedData = ""
def computeUsingComboboxData():
	computedData  = "Data shall be computed using:\n"
	computedData += combo_files.get()
	computedData += "\n(dumped {0}) as data file and:\n".format(time.ctime(os.path.getmtime(combo_files.get())))
	computedData += combo_options.get()
	computedData += "\nas crunching option."
	text.delete("1.0", "end")
	if combo_options.get() == "Gems":
		gemsCruncher.crunch(combo_files.get().rstrip(".d2x.txt"))
		with open("{0}.purediablo".format(combo_files.get().rstrip(".d2x.txt")), 'r') as file_:
			text.insert(tk.INSERT, file_.read())
	elif combo_options.get() == "Runes":
		runesCruncher.crunch(combo_files.get().rstrip(".d2x.txt"))
		with open("{0}.purediablo".format(combo_files.get().rstrip(".d2x.txt")), 'r') as file_:
			text.insert(tk.INSERT, file_.read())
	elif combo_options.get() == "Charms/Jewels":
		charmsJewelsCruncher.crunch(combo_files.get().rstrip(".d2x.txt"))
		with open("{0}.purediablo".format(combo_files.get().rstrip(".d2x.txt")), 'r') as file_:
			text.insert(tk.INSERT, file_.read())
	elif combo_options.get() == "Sets/Uniques":
		setUniquesCruncher.crunch(combo_files.get().rstrip(".d2x.txt"))
		with open("{0}.purediablo".format(combo_files.get().rstrip(".d2x.txt")), 'r') as file_:
			text.insert(tk.INSERT, file_.read())
	else:
		text.insert(tk.END, computedData)

def deleteDumps():
	confirmed = messagebox.askokcancel("Confirmation request", "Do you really want to delete all .d2x.txt files?")
	print("{0}".format(confirmed))
	if confirmed == True:
		dumps = glob.iglob("*.d2x.txt")
		for dump in dumps:
			os.remove(dump)
		myList = list(pathlib.Path('.').glob('*.d2x.txt'))

def deleteGeneratedFiles():
	confirmed = messagebox.askokcancel("Confirmation request", "Do you really want to delete all .purediablo files?")
	print("{0}".format(confirmed))
	if confirmed == True:
		dumps = glob.iglob("*.purediablo")
		for generated in generatedFiles:
			os.remove(generated)

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

myCrunchingOptionsList = ["Runes","Gems","Sets/Uniques","Charms/Jewels","Other items","Mixed"]
combo_options = ttk.Combobox(frame_configurable_data, values=myCrunchingOptionsList, state="readonly")
combo_options.grid(row=0, column=currentColumn)
currentColumn += 1
combo_options.current(0)

cleanPurediabloFilesButton = tk.Button(
	master=frame_configurable_data,
	text="Clean generated files",
	command=deleteGeneratedFiles
)
cleanPurediabloFilesButton.grid(row=0, column=currentColumn)
currentColumn += 1

deleteButton = tk.Button(
	master=frame_configurable_data,
	text="Delete all dumps",
	command=deleteDumps
)
deleteButton.grid(row=0, column=currentColumn)
currentColumn += 1

currentLine = 0
text = tk.Text(window)
text.grid(row=1, column=0)

text.insert("{0}.0".format(currentLine), computedData)
currentLine += 1
	
window.mainloop()