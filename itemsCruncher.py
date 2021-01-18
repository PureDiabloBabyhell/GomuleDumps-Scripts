import dico_items

def crunch(fileNameWithoutExtension):
	fp = open(fileNameWithoutExtension+'.d2x.txt')

	itemLineCounter = 0
	#item data
	itemName = ""
	itemBase = ""
	isUnid = 0
	isEth = 0
	ilvl = ""
	version = ""
	fingerprint = ""
	items = []
	qties = []
	builtReqsLines = ""
	builtModsLines = ""
	nbBuiltMods = 0
	idata = []
	currentItemIterator = -1
	sockets = []
	isSocketedItem = 0

	for aLine in fp:
		line = aLine.rstrip('\n')
		if not ("GoMule" in line.rstrip() or ("" == line.rstrip() and itemLineCounter == 0)):
			#line has to be considered
			if itemLineCounter == 0 and line.rstrip():
				itemLineCounter = 1
			else:
				itemLineCounter += 1

			if isSocketedItem and line.rstrip():#item name has been taken on first pass. Now get content until line is empty
				idata[currentItemIterator] += "\n" + line.rstrip()
				
			elif itemLineCounter == 1: #item name
				itemName = line.rstrip()

				if len(sockets):
					#same item
					sockets.remove(itemName)
					isSocketedItem = 1
					# Socketed items dumps are kept as is
					idata[currentItemIterator] += "\n\n" + itemName
				elif itemName in items:
					currentItemIterator = items.index(itemName)
					qties[currentItemIterator] += 1
				else:
					currentItemIterator = len(items)
					items.append(itemName)
					qties.append(1)
					builtReqsLines = ""
					builtModsLines = ""
					idata.append("")
			elif itemLineCounter == 2: #potential item base
				if "Defense" in line or "Damage" in line:#item is gemmed or runed but not runeword
					#Count the line as a mod
					if builtModsLines == "":
						builtModsLines  = dico_items.crunch(line)
					elif builtModsLines.endswith("\n"):
						builtModsLines += dico_items.crunch(line)
					else:
						builtModsLines += "\n" + dico_items.crunch(line)
					nbBuiltMods += 1
				else:#is the item base
					itemBase = ", " + line.strip()
			elif "Fingerprint" in line:
				fingerprint = " [" + line.replace("Fingerprint: ", "") +"]"
			elif ("Required Level" in line or "Required Strength" in line or "Required Dexterity" in line):
				#is a requirement
				if builtReqsLines == "":
					builtReqsLines  = dico_items.crunch(line)
				else:
					builtReqsLines += "\n{0}".format(dico_items.crunch(line))
			elif "Item Level" in line:
				ilvl = dico_items.crunch(line)
			elif "Version" in line:
				version = dico_items.crunch(line)
			elif "Unidentified" in line:
				isUnid = 1
			elif "Ethereal" in line:
				isEth = 1
			elif "Socketed" in line.strip():
				#Do something
				#print("Socket for {0} ({1})".format(itemName, line.strip()[10:]))
				sockets.append(line.strip()[10:])
				#idata[currentItemIterator] += "\n" + line.strip()
			elif line:
				#is a mod
				if builtModsLines == "":
					builtModsLines  = dico_items.crunch(line)
				elif builtModsLines.endswith("\n"):
					builtModsLines += dico_items.crunch(line)
				else:
					builtModsLines += "\n" + dico_items.crunch(line)
				nbBuiltMods += 1
			#elif "Version" in line.strip():
			#	#Handle saved data
			#	idata[currentItemIterator] += "\n" + builtReqsLines
			#	idata[currentItemIterator] += "\n" + builtModsLines
			#elif "Socketed" in line.strip():
			#	sockets.append(line.strip()[10:])
			#	idata[currentItemIterator] += "\n" + line.strip()
			#elif line.strip():
			#	idata[currentItemIterator] += "\n" + line.strip()

			if not (line.rstrip() or isSocketedItem):
				####Build idata
				#print(itemName + "\nbase=" + itemBase + "\nfp=" + fingerprint)
				# Separation lines as necessary
				if not idata[currentItemIterator] == "":
					idata[currentItemIterator] += "\n\n"
				# First line: <Identification status> <Eth status> <item name> <item base> <fingerprint>
				if isUnid:
					idata[currentItemIterator] += "[Unid]"
				if isEth:
					idata[currentItemIterator] += "[Eth]"
				if isUnid or isEth:
					idata[currentItemIterator] += " "
					isUnid = 0
					isEth = 0
				idata[currentItemIterator] += itemName + itemBase + fingerprint + "\n"
				itemName = ""
				itemBase = ""
				fingerprint = ""
				# info when defined:
				# <version>
				# <item level>
				# <fingerprint>
				# <Requirements (lvl, strength, dexterity)>
				# <item mods>
				if isUnid:
					idata[currentItemIterator] += "Unid.\n"
					isUnid = 0
				if version:
					idata[currentItemIterator] += version + "\n"
					version = ""
				if ilvl:
					idata[currentItemIterator] += ilvl + "\n"
					ilvl = ""
				if builtReqsLines:
					idata[currentItemIterator] += builtReqsLines + "\n"
					builtReqsLines = ""
				if builtModsLines:
					idata[currentItemIterator] += builtModsLines
					builtModsLines = ""

			if not line.rstrip():
				itemLineCounter = 0
				isSocketedItem = 0

	else:#Handle EOF
		nbItems = 0
		for value in qties:
			if not value == -1:
				nbItems += value
		print("Number of items: {0}".format(nbItems))

	fp.close()

	#After processing
	outputFile = open(fileNameWithoutExtension+'.purediablo','w')
	itemLineCounter = 0
	for item in items:
		if qties[itemLineCounter] > 0:
			idata[itemLineCounter] = "{0} x{1}\n[SPOILER=DUMPS]{2}\n[/SPOILER]".format(item, qties[itemLineCounter], idata[itemLineCounter])
		itemLineCounter += 1

	#idata[40:].sort()

	#Available header
	print("[B][COLOR=rgb(250, 197, 28)][SIZE=5]Available items: {0}[/SIZE][/COLOR][/B]\n".format(nbItems), file=outputFile)

	#Items table
	print("[CODE]", file=outputFile)
	itemLineCounter = 0
	for item in items:
		print("{0} x{1}".format(item, qties[itemLineCounter]), file=outputFile)
		itemLineCounter += 1

	print("[/CODE]", file=outputFile)

	#Dumps - under spoiler
	print("[SPOILER=DUMPS]", file=outputFile)
	itemLineCounter = 0
	first = 1
	for data in idata:
		if not data == "":
			if first:
				print(idata[itemLineCounter], file=outputFile)
				first = 0
			else:
				print("\n{0}".format(idata[itemLineCounter]), file=outputFile)
		itemLineCounter += 1
	
	print("[/SPOILER]", file=outputFile)
	outputFile.close()