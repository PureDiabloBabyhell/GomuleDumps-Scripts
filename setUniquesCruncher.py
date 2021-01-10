#fileNameWithoutExtension = "Tradable_S_U"
def crunch(fileNameWithoutExtension):
	fp = open(fileNameWithoutExtension+'.d2x.txt')

	counter = 0
	itemName = ""
	#Start with Elite sets for dedicated display
	elitesetitems = ["Aldur's Watchtower", "Aldur's Stony Gaze", "Aldur's Deception", "Aldur's Rhythm", "Aldur's Advance",
	"Griswold's Legacy", "Griswold's Valor", "Griswold's Heart", "Griswold's Redemption", "Griswold's Honor",
	"Immortal King", "Immortal King's Will", "Immortal King's Soul Cage", "Immortal King's Detail", "Immortal King's Forge", "Immortal King's Pillar", "Immortal King's Stone Crusher",
	"M'avina's Battle Hymn", "M'avina's True Sight", "M'avina's Embrace", "M'avina's Icy Clutch", "M'avina's Tenet", "M'avina's Caster",
	"Natalya's Odium", "Natalya's Totem", "Natalya's Mark", "Natalya's Shadow", "Natalya's Soul",
	"Tal Rasha's Wrappings", "Tal Rasha's Fine Spun Cloth", "Tal Rasha's Adjudication", "Tal Rasha's Lidless Eye", "Tal Rasha's Guardianship", "Tal Rasha's Horadric Crest",
	"Trang-Oul's Avatar", "Trang-Oul's Guise", "Trang-Oul's Scales", "Trang-Oul's Wing", "Trang-Oul's Claws", "Trang-Oul's Girth"]
	elitesetqties = [-1, 0, 0, 0, 0,
	-1, 0, 0, 0, 0,
	-1, 0, 0, 0, 0, 0, 0,
	-1, 0, 0, 0, 0, 0,
	-1, 0, 0, 0, 0,
	-1, 0, 0, 0, 0, 0,
	-1, 0, 0, 0, 0, 0]
	elitesetidata = ["", "", "", "", "",
	 "", "", "", "", "",
	 "", "", "", "", "", "", "",
	 "", "", "", "", "", "",
	 "", "", "", "", "",
	 "", "", "", "", "", "",
	 "", "", "", "", "", ""]
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
		for value in elitesetqties:
			if not value == -1:
				nbItems += value
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

	idata[40:].sort()

	#Available header
	print("[B][COLOR=rgb(250, 197, 28)][SIZE=5]Available uniques/sets: {0}[/SIZE][/COLOR][/B]\n".format(nbItems), file=outputFile)

	#Elite sets table
	print("[I][B][COLOR=rgb(65, 168, 95)]Elite Sets[/COLOR][/B][/I]\n[CODE=Rich]", file=outputFile)
	counter = 0
	for item in elitesetitems:
		if elitesetqties[counter] == - 1:#Set name
			print("[COLOR=rgb(65, 168, 95)]{0}[/COLOR]".format(item), file=outputFile)
		else:
			print("[INDENT]{0} x{1}[/INDENT]".format(item, elitesetqties[counter]), file=outputFile)
		if item == "Trang-Oul's Girth":
			break
		counter += 1

	print("[/CODE]", file=outputFile)

	#Uniques and other sets table
	print("[COLOR=rgb(250, 197, 28)][I][B]Uniques & other sets[/B][/I][/COLOR]\n[CODE]", file=outputFile)
	counter = 0
	unlock = 0
	for item in items:
		if unlock:
			print("{0} x{1}".format(item, qties[counter]), file=outputFile)
		if item == "Trang-Oul's Girth":
			unlock = 1
		counter += 1

	print("[/CODE]", file=outputFile)

	#Dumps - under spoiler
	print("[SPOILER=DUMPS]", file=outputFile)
	counter = 0
	first = 1
	for data in elitesetidata:
		if not data == "":
			if first:
				print(elitesetidata[counter], file=outputFile)
				first = 0
			else:
				print("\n{0}".format(elitesetidata[counter]), file=outputFile)
		counter += 1

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