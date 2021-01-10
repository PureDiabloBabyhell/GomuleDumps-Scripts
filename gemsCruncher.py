from math import *

#fileNameWithoutExtension = "Gems"
def crunch(fileNameWithoutExtension):

	fp = open(fileNameWithoutExtension+'.d2x.txt')

	PerfectAndFlawlessGems = 0

	counter = 0
	itemName = ""
	items = ["Perfect Amethyst", "Perfect Ruby", "Perfect Skull", "Perfect Emerald", "Perfect Sapphire", "Perfect Diamond", "Perfect Topaz"]
	qties = [0, 0, 0, 0, 0, 0, 0]
	itemIterator = 2
	nbItems = 0

	for line in fp:
		if not fileNameWithoutExtension in line.rstrip():
			if counter == 0 and line.rstrip():
				counter = 1

			if counter == 1:
				itemName = line.rstrip()

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
		print("Number of gems: {0}".format(nbItems))

	fp.close()

	#After processing
	outputFile = open(fileNameWithoutExtension+'.purediablo','w')

	if PerfectAndFlawlessGems:
		counter = 0
		nbPerfectGems = 0
		for item in items:
			if 'Perfect' in item:
				nbPerfectGems += qties[counter]
				print(item + "{0}".format(qties[counter]))
			counter += 1

		pamethystsIterator = items.index("Perfect Amethyst")
		prubiesIterator = items.index("Perfect Ruby")
		#Header
		print("[B][COLOR=rgb(147, 101, 184)]P[/COLOR][COLOR=rgb(247, 218, 100)]g[/COLOR][COLOR=rgb(97, 189, 109)]e[/COLOR][COLOR=rgb(226, 80, 65)]m[/COLOR][COLOR=rgb(44, 130, 201)]s[/COLOR][COLOR=rgb(255, 255, 255)]![/COLOR][/B]", file=outputFile)
		#Table
		print("[CODE]", file=outputFile)
		print("| Total || Pamethysts | Prubies | Others", file=outputFile)
		print("| {0:5d} || {1:10d} | {2:7d} | {3:6d}".format(nbPerfectGems, qties[pamethystsIterator], qties[prubiesIterator], nbPerfectGems - qties[pamethystsIterator] - qties[prubiesIterator]), file=outputFile)

		counter = 0
		nbFlawlesses = 0
		for item in items:
			if 'Flawless' in item:
				nbFlawlesses += qties[counter]
			counter += 1

		print("Flawlesses: {0}".format(nbFlawlesses), file=outputFile)
		print("[/CODE]", file=outputFile)
	else:
		counter = 0
		nbPerfectGems = 0

		pamethystsIterator = items.index("Perfect Amethyst")
		prubiesIterator = items.index("Perfect Ruby")
		psapphiresIterator = items.index("Perfect Sapphire")
		ptopazesIterator = items.index("Perfect Topaz")
		pemeraldsIterator = items.index("Perfect Emerald")
		pdiamondsIterator = items.index("Perfect Diamond")
		pskullsIterator = items.index("Perfect Skull")

		#Count flawless per 3 as perfect gems
		for item in items:
			if 'Flawless' in item:
				if 'Amethyst' in item:
					qties[pamethystsIterator] += floor(qties[counter]/3)
				elif 'Ruby' in item:
					qties[prubiesIterator] += floor(qties[counter]/3)
				elif 'Sapphire' in item:
					qties[psapphiresIterator] += floor(qties[counter]/3)
				elif 'Topaz' in item:
					qties[ptopazesIterator] += floor(qties[counter]/3)
				elif 'Emerald' in item:
					qties[pemeraldsIterator] += floor(qties[counter]/3)
				elif 'Diamond' in item:
					qties[pdiamondsIterator] += floor(qties[counter]/3)
				elif 'Skull' in item:
					qties[pskullsIterator] += floor(qties[counter]/3)
			counter += 1
		#Header
		print("[B][COLOR=rgb(147, 101, 184)]P[/COLOR][COLOR=rgb(247, 218, 100)]g[/COLOR][COLOR=rgb(97, 189, 109)]e[/COLOR][COLOR=rgb(226, 80, 65)]m[/COLOR][COLOR=rgb(44, 130, 201)]s[/COLOR][COLOR=rgb(255, 255, 255)]![/COLOR][/B]", file=outputFile)
		#Table
		print("[CODE]", file=outputFile)
		print("| Total || Pamethysts | Prubies | Others", file=outputFile)
		print("| {0:5d} || {1:10d} | {2:7d} | {3:6d}".format(qties[pamethystsIterator] + qties[prubiesIterator] + qties[psapphiresIterator] + qties[ptopazesIterator] + qties[pemeraldsIterator] + qties[pdiamondsIterator] + qties[pskullsIterator], qties[pamethystsIterator], qties[prubiesIterator], qties[psapphiresIterator] + qties[ptopazesIterator] + qties[pemeraldsIterator] + qties[pdiamondsIterator] + qties[pskullsIterator]), file=outputFile)
		print("Note: includes cubable flawless ones\n[/CODE]", file=outputFile)

	outputFile.close()