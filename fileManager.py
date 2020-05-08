def createFile(finalCipher, key):	
	file = open(key+'.enc', 'w')
	file.write(finalCipher)
	file.close()

def getFile(key):
	file = open(key, 'r')
	fileCipher = file.read()
	file.close()
	return fileCipher