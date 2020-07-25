import random
from random import randrange, getrandbits

def isPrime(n, k):
	if(n == 2 or n == 3):
		return True 
	if(n <= 1 or n%2 == 0):
		return False

	s = 0
	r = n-1

	while(r & 1 == 0):
		s += 1
		r //= 2

	for _ in range(k):
		a = randrange(2, n-1)
		x = pow(a, r, n)
		if(x != 1 and x != n-1):
			j = 1
			while(j < s and x != n-1):
				x = pow(x, 2, n)
				if(x == 1):
					return False
				j += 1
			if(x != n-1):
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
	yPhase = generatePrimeNumber() * generatePrimeNumber()
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