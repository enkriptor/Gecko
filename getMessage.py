import matrixOperation as mop
import fileManager as fm
import json

jsonData = fm.getFile('generalConstants.json', 'r')
jsonParse = json.loads(jsonData)

def vectorDifference(cipherMessagevector, cipherRawVector):
	index = 0
	differenceVector = []
	while(index != len(cipherRawVector)):
		difference = cipherMessagevector[index] - cipherRawVector[index]
		status = (difference >=jsonParse['Const0'] and difference<=jsonParse['Const4']) 
		if(status):
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
		status1 = (numSubstring >=jsonParse['Const1'] and numSubstring<=jsonParse['Const2']) 
		status2 = (numSubstring>=jsonParse['Const3'] and numSubstring<=jsonParse['Const4'])
		if(status1 or status2):
			fileCipherNumerical += str(numSubstring)
		else:
			fileCipherNumerical += fileCipher[index]
		index += 1
	return fileCipherNumerical

def getMessageFromCipher(fileCipher, securityKey, recieversKey):
	fileCipher = getNumerical(fileCipher)
	elemLen = jsonParse['checkLength']
	index, lengthMessage = 0, jsonParse['lengthMessage']
	element = ''
	cipherVector = []
	while(fileCipher != ''):
		element = fileCipher[index:elemLen]
		cipherVector.append(int(element))
		fileCipher = fileCipher[elemLen:len(fileCipher)]
	cipherMatrix = mop.matrixTransposer(mop.squareMatrixMakerOnList(cipherVector))
	cipherVector = mop.matrixToVector(cipherMatrix)[:len(cipherVector)]
	cipherRawVector = cipherVector[index:lengthMessage]
	cipherMessageVector = cipherVector[lengthMessage:len(cipherVector)-lengthMessage]
	cipherSignatureVector = cipherVector[len(cipherVector)-lengthMessage:len(cipherVector)]
	differenceMessageVector = vectorDifference(cipherMessageVector, cipherRawVector)
	differenceSignatureVector = vectorDifference(cipherSignatureVector, cipherRawVector)
	if(recieversKey in "".join(differenceSignatureVector)):
		return "".join(differenceMessageVector)
	else:
		print("Provide correct key for the cipher!")