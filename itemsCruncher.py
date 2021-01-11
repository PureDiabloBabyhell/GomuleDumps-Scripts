def crunch(fileNameWithoutExtension):
	fp = open(fileNameWithoutExtension+'.d2x.txt')

	counter = 0
	itemName = ""
	items = []
	qties = []
	idata = []
	itemIterator = len(idata)
	sockets = []

	for line in fp:
		if not fileNameWithoutExtension in line.rstrip():
			if counter == 0 and line.rstrip():
				counter = 1

			if counter == 1:
				itemName = line.rstrip()

				if len(sockets):
					#same item
					idata[itemIterator] += "\n\n{0}".format(itemName)
					sockets.remove(itemName)
				elif itemName in items:
					itemIterator = items.index(itemName)
					qties[itemIterator] += 1
					if idata[itemIterator] == "":
						idata[itemIterator] = "\n{0}".format(itemName)
					else:
						idata[itemIterator] += "\n\n{0}".format(itemName)
				else:
					itemIterator = len(items)
					items.append(itemName)
					qties.append(1)
					if itemIterator == 0:
						idata.append(itemName)
					else:
						idata.append("\n" + itemName)

			elif "Socketed" in line.strip():
				sockets.append(line.strip()[10:])
				idata[itemIterator] += "\n" + line.strip()
			elif line.strip():
				idata[itemIterator] += "\n" + line.strip()

			if not line.rstrip():
				counter = 0
			else:
				counter += 1

	else:#Handle EOF
		nbItems = 0
		for value in qties:
			if not value == -1:
				nbItems += value
		print("Number of items: {0}".format(nbItems))

	fp.close()

	#After processing
	outputFile = open(fileNameWithoutExtension+'.purediablo','w')
	counter = 0
	for item in items:
		if qties[counter] > 0:
			idata[counter] = "{0} x{1}\n[SPOILER=DUMPS]{2}\n[/SPOILER]".format(item, qties[counter], idata[counter])
		counter += 1

	#idata[40:].sort()

	#Available header
	print("[B][COLOR=rgb(250, 197, 28)][SIZE=5]Available items: {0}[/SIZE][/COLOR][/B]\n".format(nbItems), file=outputFile)

	#Items table
	print("[CODE]", file=outputFile)
	counter = 0
	for item in items:
		print("{0} x{1}".format(item, qties[counter]), file=outputFile)
		counter += 1

	print("[/CODE]", file=outputFile)

	#Dumps - under spoiler
	print("[SPOILER=DUMPS]", file=outputFile)
	counter = 0
	first = 1
	for data in idata:
		if not data == "":
			if first:
				print(idata[counter], file=outputFile)
				first = 0
			else:
				print("\n{0}".format(idata[counter]), file=outputFile)
		counter += 1
	
	print("[/SPOILER]", file=outputFile)
	outputFile.close()