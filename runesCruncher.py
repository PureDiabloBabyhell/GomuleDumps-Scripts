#fileNameWithoutExtension = "Runes"
def crunch(fileNameWithoutExtension):
	fp = open(fileNameWithoutExtension+'.d2x.txt')

	counter = 0
	itemName = ""
	items = ['El', 'Eld', 'Tir', 'Nef', 'Eth', 'Ith', 'Tal', 'Ral', 'Ort', 'Thul', 'Amn', 'Sol', 'Shael', 'Dol', 'Hel', 'Io', 'Lum', 'Ko', 'Fal', 'Lem', 'Pul', 'Um', 'Mal', 'Ist', 'Gul', 'Vex', 'Ohm', 'Lo', 'Sur', 'Ber', 'Jah', 'Cham', 'Zod']
	qties = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
	itemIterator = 0
	nbItems = 0

	for line in fp:
		if not "GoMule" in line.rstrip():
			if counter == 0 and line.rstrip():
				counter = 1

			if counter == 1:
				itemName = line.rstrip().split()[0]

				if itemName in items:
					itemIterator = items.index(itemName)
					qties[itemIterator] += 1
				else:
					itemIterator = len(items)
					items.append(itemName)
					qties.append(1)

			if not line.rstrip():
				counter = 0
			else:
				counter += 1

	else:#Handle EOF
		nbItems = 0
		for value in qties:
			nbItems += value
		print("Number of runes: {0}".format(nbItems))

	fp.close()

	#After processing
	outputFile = open(fileNameWithoutExtension+'.purediablo','w')
	#Header
	print("[COLOR=rgb(243, 121, 52)][B]Runes[/B][/COLOR]", file=outputFile)
	#Table
	print("[CODE]", file=outputFile)

	counter = 0
	runeNamesLine = ""
	runeQtiesLine = ""
	for item in items:
		runeNamesLine += "| {0:>5s} ".format(item)
		runeQtiesLine += "| {0:5d} ".format(qties[counter])
		counter += 1
		if (counter % 5) == 0:
			print(runeNamesLine + "|", file=outputFile)
			print(runeQtiesLine + "|", file=outputFile)
			runeNamesLine = ""
			runeQtiesLine = ""		

	if runeNamesLine:
		print(runeNamesLine + "|", file=outputFile)
		print(runeQtiesLine + "|", file=outputFile)

	print("[/CODE]", file=outputFile)
	
	outputFile.close()