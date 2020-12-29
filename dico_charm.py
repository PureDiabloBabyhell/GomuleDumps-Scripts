dico = open('dicos/dico_charm.txt')

line = dico.readline().rstrip('\n')
counter = 0

dicoEntries = []
dicoCrunched = []

while line:
	content = line.rsplit("::")
	dicoEntries.append(content[0])
	dicoCrunched.append(content[1])
	line = dico.readline().rstrip('\n')

def crunch(itemMod):
	iterator = 0
	for entry in dicoEntries:
		if entry in itemMod:
			return itemMod.replace(entry, dicoCrunched[iterator])
		else:
			iterator += 1
	return itemMod