import random
from random import randrange, getrandbits

def isPrime(number, numberOfTests):
	if(number == 2 or number == 3):
		return True 
	if(number <= 1 or number%2 == 0):
		return False

	sumTotal = 0
	recursions = number-1

	while(recursions & 1 == 0):
		sumTotal += 1
		recursions //= 2

	for _ in range(numberOfTests):
		randomNumber = randrange(2, number-1)
		modulo = pow(randomNumber, recursions, number)
		if(modulo != 1 and modulo != number-1):
			jIndex = 1
			while(jIndex < sumTotal and modulo != number-1):
				modulo = pow(modulo, 2, number)
				if(modulo == 1):
					return False
				jIndex += 1
			if(modulo != number-1):
				return False
	return True

def generatePrimeCandidate(length):
	p = getrandbits(length)
	p |= (1 << length-1) | 1
	return p

def generatePrimeNumber(length=1024):
	p = 4
	while(not isPrime(p, 256)):
		p = generatePrimeCandidate(length)
	return p

def getBitMessageDirect(testMessage):
	messageBitVector = [str(ord(element)) for element in testMessage]
	messageBitNumeric = "".join(messageBitVector)
	return messageBitNumeric

def getPrintables(message):
	originalMessage = ""
	readLen = 3
	while(len(message) != 0):
		readForm = int(message[:readLen])
		if(readForm>=100 and readForm<=255):
			originalMessage += str(chr(readForm))
			message = message[readLen:len(message)]
		else:
			readForm = int(message[:readLen-1])
			if(readForm>=10 and readForm<=99):
				originalMessage += str(chr(readForm))
				message = message[readLen-1:len(message)]
			else:
				readForm = int(message[:readLen-2])
				originalMessage += str(chr(readForm))
				message = message[readLen-2:len(message)]
	return originalMessage

def getKey(messageBitNumeric):
	pPhase, qPhase = generatePrimeNumber(), generatePrimeNumber()
	while(True):
		if(pPhase != qPhase):
			yPhase = pPhase * qPhase
			break
	return yPhase

def embedKeyIntoMessage(yPhase, messageBitNumeric):
	encryptedMsg = ""
	while(len(messageBitNumeric) != 0):
		yPhaseLen = len(str(yPhase))
		if(len(messageBitNumeric) > yPhaseLen):
			readForm = int(messageBitNumeric[:yPhaseLen]) + yPhase
			messageBitNumeric = messageBitNumeric[yPhaseLen:len(messageBitNumeric)]
		else:
			readForm = int(messageBitNumeric[:len(messageBitNumeric)]) + yPhase
			messageBitNumeric = ""
		encryptedMsg += str(readForm)
	return encryptedMsg

def getNumericEncrypted(originalMessage):
	messageNumeric = ""
	for element in originalMessage:
		messageNumeric += str(ord(element))
	return messageNumeric

def getBitMessage(messageNumeric, yPhase):
	message = ""
	while(len(messageNumeric)!=0):
		yPhaseLen = len(str(yPhase))
		readForm = int(messageNumeric[:yPhaseLen]) - yPhase
		if(readForm < 0):
			readForm = int(messageNumeric[:yPhaseLen+1]) - yPhase
			if(len(str(readForm))!=yPhaseLen):
				if(len(messageNumeric)<=yPhaseLen):
					message += str(readForm)
				else:
					message += "0"+str(readForm)
			else:
				message += str(readForm)
			messageNumeric = messageNumeric[yPhaseLen+1:len(messageNumeric)]
		else:
			if(len(str(readForm))!=yPhaseLen):
				if(len(messageNumeric)<=yPhaseLen):
					message += str(readForm)
				else:
					message += "0"+str(readForm)
			else:
				message += str(readForm)
			messageNumeric = messageNumeric[yPhaseLen:len(messageNumeric)]
	return message

def getAddressKey(keyLength):
	msg = ""
	state = True
	while(state):
		asciiNum = random.randint(65, 122)
		if(asciiNum!=92 and asciiNum!=96 and asciiNum!=91):
			msg += chr(asciiNum)
		if(len(msg) == keyLength): 
			state = False 
		else: 
			state = True
	return msg