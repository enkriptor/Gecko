def createFile(finalCipher, key, ext, mode):	
	file = open(key+ext, mode)
	file.write(finalCipher)
	file.close()

def getFile(key, mode):
	readFile = open(key, mode)
	if(mode == 'rb'):
		data = " ".join(map(str, readFile.read())) 
		fileData = [int(element) for element in data.split()]
	else:
		fileData = readFile.read()
	readFile.close()
	return fileData