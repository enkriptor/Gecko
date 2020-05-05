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
	while(True):
		num = random.randint(10000, 9999999)
		numStr, stateNumStr = checkLength(str(num))
		if(stateNumStr):
			cipherVector.append(numStr)
		if(len(cipherVector) == lengthMessage):
			break
	while(len(messageVector) != 0):
		if(len(messageVector)>lengthMessage):
			messageVectorDelta = messageVector[0:lengthMessage]
			messageVector = messageVector[lengthMessage:len(messageVector)]
		else:
			messageVectorDelta = messageVector 
			messageVector = []
		cipherMessageVector += embedCipher(cipherVector, messageVectorDelta)
	cipherMessageVector += embedCipher(cipherVector, timeStampVector)
	return (cipherVector, cipherMessageVector)

def joinCipherVector(cipherVector):
	return "".join(cipherVector)

def getCipherMessage(joinedCipher):
	index, length = 0, 2
	cipherList = []
	while(len(joinedCipher) != 0):
		subStringCipher = joinedCipher[index : index + length]
		numSubstring = int(subStringCipher)
		status = (numSubstring >= 33 and numSubstring<=47) or (numSubstring>=58 and numSubstring<=126)
		if(status):
			cipherList.append(chr(numSubstring))
			joinedCipher = joinedCipher[index + length : len(joinedCipher)]
		else:
			cipherList.append(joinedCipher[index])
			joinedCipher = joinedCipher[index + 1 : len(joinedCipher)]
	return "".join(cipherList)
		
message = input('Enter your message: ')
timestamp = tsg.getTimeStamp()
messageVector = [element for element in message]
timeStampVector = [element for element in timestamp]
print('Message laid!')
cipherVector, cipherMessageVector = makeCipherVector(messageVector, timeStampVector)
finalCipherVector = cipherVector + cipherMessageVector
cipherMatrix = mop.squareMatrixMakerOnList(finalCipherVector)
cipherMatrix = mop.matrixTransposer(cipherMatrix)
finalCipherVector = mop.matrixToVector(cipherMatrix)
joinedCipher = joinCipherVector(finalCipherVector)
finalCipher = getCipherMessage(joinedCipher)
print('Cipher created!')
file = open('cipher.txt', 'w')
file.write(finalCipher)
file.close()