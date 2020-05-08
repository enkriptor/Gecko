import time
import random
import timeStampGenerator as tsg
import matrixOperation as mop

def checkLength(num):
	state = False
	if(len(num)<=7):
		while(len(num)<7):
			num = '0' + num
		state = True
	else:
		state = False
	return (num, state)

def embedCipher(cipherVector, messageVector):
	cipherMessageVector = []
	messageLen, index = len(messageVector), 0
	for primeFactor in cipherVector:
		if(index >= messageLen):
			numAssetStr = primeFactor
		else:
			numAssetStr = str(int(primeFactor) + ord(messageVector[index]))
		numAssetStr, status = checkLength(numAssetStr)
		if(status):
			cipherMessageVector.append(numAssetStr)
		index += 1
	return cipherMessageVector

def makeCipherVector(messageVector, timeStampVector):
	cipherVector, cipherMessageVector = [], []
	lengthMessage = 300
	while(len(cipherVector) != lengthMessage):
		num = random.randint(10000, 9999999)
		numStr, stateNumStr = checkLength(str(num))
		if(stateNumStr):
			cipherVector.append(numStr)
	cipherMessageVector += embedCipher(cipherVector, messageVector)
	cipherMessageVector += embedCipher(cipherVector, timeStampVector)
	return cipherVector + cipherMessageVector

def getCipherMessage(joinedCipher):
	index, length = 0, 2
	cipherList = []
	while(len(joinedCipher) != 0):
		numSubstring = int(joinedCipher[index : index + length])
		status = (numSubstring >= 33 and numSubstring<=47) or (numSubstring>=58 and numSubstring<=126)
		if(status):
			cipherList.append(chr(numSubstring))
			joinedCipher = joinedCipher[index + length : len(joinedCipher)]
		else:
			cipherList.append(joinedCipher[index])
			joinedCipher = joinedCipher[index + 1 : len(joinedCipher)]
	return "".join(cipherList)

def getCipher(message):
	messageVector = [element for element in message]
	timeStampVector = [element for element in tsg.getTimeStamp()]
	print('Message laid!')
	finalCipherVector = makeCipherVector(messageVector, timeStampVector)
	cipherMatrix = mop.matrixTransposer(mop.squareMatrixMakerOnList(finalCipherVector)) 
	finalCipher = getCipherMessage("".join(mop.matrixToVector(cipherMatrix)))
	print('Cipher created!')
	return finalCipher