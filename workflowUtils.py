import random

def sieveOfEratosthenes(num):
	sieveVector = [True for index in range(num+1)]
	sieve = []
	primeFactor = 2
	while(primeFactor*primeFactor <= num):
		if(sieveVector[primeFactor] == True):
			for index in range(primeFactor*primeFactor, num+1, primeFactor):
				sieveVector[index] = False
		primeFactor += 1
	for index in range(2, num+1):
		if(sieveVector[index]):
			sieve.append(index)
	return sieve

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
	yPhase = 0
	while(True):
		try:
			primeConst = sieveOfEratosthenes(random.randint(len(messageBitNumeric), 99999))[random.randint(0, len(sieveOfEratosthenes(random.randint(100, 99999))))]
			break
		except:
			pass
	while(True):
		xPhase = random.randint(0, primeConst)
		yPhase = xPhase**2 + primeConst
		if(yPhase < primeConst**2):
			break
	return yPhase

def embedKeyIntoMessage(yPhase, messageBitNumeric):
	encryptedMsg = ""
	while(len(messageBitNumeric) != 0):
		yPhaseLen = len(str(yPhase))
		try:
			readForm = int(messageBitNumeric[:yPhaseLen]) + yPhase
		except:
			readForm = int(messageBitNumeric[:len(messageBitNumeric)]) + yPhase
		encryptedMsg += str(readForm)
		messageBitNumeric = messageBitNumeric[yPhaseLen:len(messageBitNumeric)]
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