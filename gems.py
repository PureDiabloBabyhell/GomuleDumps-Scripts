fileName = "Gems"
fp = open(fileName+'.d2x.txt')

counter = 0
itemName = ""
items = []
qties = []
itemIterator = 0
nbItems = 0

for line in fp:
	if not fileName in line.rstrip():
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
counter = 0
nbPerfectGems = 0
for item in items:
	if 'Perfect' in item:
		nbPerfectGems += qties[counter]
		print(item + "{0}".format(qties[counter]))
	counter += 1

outputFile = open(fileName+'.purediablo','w')
pamethystsIterator = items.index("Perfect Amethyst")
prubiesIterator = items.index("Perfect Ruby")
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
	
outputFile.close()