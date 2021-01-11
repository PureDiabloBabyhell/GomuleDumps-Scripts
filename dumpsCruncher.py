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
import charmsCruncher
import jewelsCruncher
import setUniquesCruncher
import itemsCruncher

def getStrippedFileName(dumpFileNameWithExtension):
	return dumpFileNameWithExtension.removesuffix(".d2x.txt")

computedData = ""
def computeUsingComboboxData():
	#get stripped name without the GoMule dump extension
	strippedName = getStrippedFileName(combo_files.get())
	
	#call the requested cruncher process
	if combo_options.get() == "Gems":
		gemsCruncher.crunch(strippedName)
	elif combo_options.get() == "Runes":
		runesCruncher.crunch(strippedName)
	elif combo_options.get() == "Charms":
		charmsCruncher.crunch(strippedName)
	elif combo_options.get() == "Jewels":
		jewelsCruncher.crunch(strippedName)
	elif combo_options.get() == "Sets/Uniques":
		setUniquesCruncher.crunch(strippedName)
	elif combo_options.get() == "Non-specific items":
		itemsCruncher.crunch(strippedName)

	#put file content in text area
	text.delete("1.0", "end")
	with open("{0}.purediablo".format(strippedName), 'r') as file_:
		text.insert(tk.INSERT, file_.read())

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

myCrunchingOptionsList = ["Runes","Gems","Charms","Jewels","Sets/Uniques","Non-specific items","Mixed [not available]"]
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