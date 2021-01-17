dico = open('dicos/dico_items.txt')

line = dico.readline().rstrip('\n')
counter = 0

dicoEntries = []
dicoCrunched = []

while line:
	if not (line.strip()[0] == '#'):
		content = line.rsplit("::")
		dicoEntries.append(content[0])
		dicoCrunched.append(content[1])
	line = dico.readline().rstrip('\n')

def crunch(itemMod):
	iterator = 0
	#print("#######")
	for entry in dicoEntries:
	#	print("is {0} in {1} ?".format(entry, itemMod))
		if entry in itemMod:
			#Specific cases
			if "Durability" in itemMod:
				return crunch(itemMod.replace(entry, dicoCrunched[iterator]))
			else:
				return itemMod.replace(entry, dicoCrunched[iterator])
		else:
			iterator += 1
	return itemMod