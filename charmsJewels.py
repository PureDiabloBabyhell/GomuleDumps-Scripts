import dico_jewel
import dico_charm

fileNames = ["Charms Skillers", "Charms_MF", "Charms", "Jewels_Good", "Jewels"]
#fileNames = ["Jewels_Good"]
for fileName in fileNames:
	file = open(fileName+'.d2x.txt', 'r')
	outputFile = open(fileName+".purediablo",'w')

	counter = 0

	currentItemIterator = -1
	builtItemNameLines = []
	qties = []
	builtReqLvlLines = []
	builtModsLines = []
	nbBuiltMods = 0
	itemName=""
	fingerprint = ""

	for aLine in file:
		line = aLine.rstrip('\n')
		if not "GoMule" in line:
			if line == "" in line:
				counter = 0
				if not currentItemIterator == -1:
					if not fingerprint in builtModsLines[currentItemIterator]:
						builtModsLines[currentItemIterator] += fingerprint.rstrip('\n')
			else:
				counter += 1
			if not line == "":
				if counter == 3:#itemName is complete
					if itemName in builtItemNameLines:#existing item
						currentItemIterator = builtItemNameLines.index(itemName)
						qties[currentItemIterator] += 1
						builtModsLines[currentItemIterator] += "\n"
					else:#new item
						currentItemIterator = len(builtItemNameLines)
						builtItemNameLines.append(itemName)
						qties.append(1)
						builtReqLvlLines.append("")
						builtModsLines.append("")
						nbBuiltMods = 0
				if counter == 1: #item name
					itemName = line
				elif counter == 2: #item base
					itemName += ", " + line
				elif "Fingerprint" in line:
					fingerprint = " [" + line.replace("Fingerprint: ", "") +"]"
				elif "Required Level" in line:
					builtReqLvlLines[currentItemIterator] = line
				elif not ("Item Level" in line or "Version" in line or "Unidentified" in line):
					#is a mod
					if builtModsLines[currentItemIterator] == "":
						if "Charms" in fileName:
							builtModsLines[currentItemIterator] = dico_charm.crunch(line)
						else: #Jewels
							builtModsLines[currentItemIterator] = dico_jewel.crunch(line)
					elif builtModsLines[currentItemIterator].endswith("\n"):
						if "Charms" in fileName:
							builtModsLines[currentItemIterator] += dico_charm.crunch(line)
						else: #Jewels
							builtModsLines[currentItemIterator] += dico_jewel.crunch(line)
					else:
						if "Charms" in fileName:
							builtModsLines[currentItemIterator] += ", " + dico_charm.crunch(line)
						else: #Jewels
							builtModsLines[currentItemIterator] += ", " + dico_jewel.crunch(line)
					nbBuiltMods += 1

	file.close()
	
	#After file processing
	#computing total quantity
	totalQty = 0
	for qty in qties:
		if qty > 0:
			totalQty += qty

	#sorting
	idata = []
	for iterator in range(0, len(builtItemNameLines) - 1):
		idata.append(builtItemNameLines[iterator] + " x{0}".format(qties[iterator]))
		idata[iterator] += "\n"+builtReqLvlLines[iterator]
		idata[iterator] += "\n"+builtModsLines[iterator]

	idata.sort()	

	#Table view
	print("[COLOR=rgb(44, 130, 201)][I][B]"+fileName+" ({0})[/B][/I][/COLOR]\n[CODE]".format(totalQty), file=outputFile)
	counter = 0
	for iterator in range(0, len(builtItemNameLines) - 1):
		print(idata[iterator].rsplit("\n")[0], file=outputFile)
	print("[/CODE]", file=outputFile)

	print("[SPOILER=CRUNCHED DUMPS]", file=outputFile)
	print(idata[0], file=outputFile)
	for iterator in range(1, len(builtItemNameLines) - 1):
		print("\n"+idata[iterator], file=outputFile)
	print("[/SPOILER]", file=outputFile)
	#End of process
	outputFile.close()