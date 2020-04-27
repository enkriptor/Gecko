def vectorDifference(cipherMessagevector, cipherRawVector):
	index = 0
	differenceVector = []
	while(index != len(cipherRawVector)):
		difference = cipherMessagevector[index] - cipherRawVector[index]
		differenceVector.append(chr(difference))
		index += 1
	return differenceVector

def getNumerical(fileCipher):
	index = 0
	fileCipherNumerical = ''
	while(True):
		if(index == len(fileCipher)):
			break
		numSubstring = ord(fileCipher[index])
		status = (numSubstring >= 33 and numSubstring<=47) or (numSubstring>=58 and numSubstring<=126)
		if(status):
			fileCipherNumerical += str(numSubstring)
		else:
			fileCipherNumerical += fileCipher[index]
		index += 1
	return fileCipherNumerical

def getMessageFromCipher(fileCipher):
	fileCipher = getNumerical(fileCipher)
	elemLen, index, maxLen = 7, 0, 89
	element = ''
	cipherVector = []
	while(fileCipher != ''):
		element = fileCipher[index:elemLen]
		cipherVector.append(int(element))
		fileCipher = fileCipher[elemLen:len(fileCipher)]
	cipherVector = cipherVector[:len(cipherVector)-maxLen]
	cipherRawVector = cipherVector[index:maxLen]
	cipherMessagevector = cipherVector[maxLen:len(cipherVector)]
	differenceVector = vectorDifference(cipherMessagevector, cipherRawVector)
	return "".join(differenceVector)


file = open('cipher.txt', 'r')
fileCipher = file.read()
file.close()

message = getMessageFromCipher(fileCipher)
print(message)