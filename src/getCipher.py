import workflowUtils as wu

def makeCipher(message):
	messageCopy = message
	while(True):
		messageBitNumeric = wu.getBitMessageDirect(message)
		yPhase = wu.getKey(messageBitNumeric)
		encryptedMsg = wu.getPrintables(wu.embedKeyIntoMessage(yPhase, messageBitNumeric))
		originalMessage = wu.getPrintables(wu.getBitMessage(wu.getNumericEncrypted(encryptedMsg), yPhase))
		if(originalMessage == messageCopy):
			with open("finalMessage.txt", 'wb') as finFile:
				finFile.write(encryptedMsg.encode('utf-8'))
			break
		break
	return str(yPhase)

def getCipher():
	message = open('messageCopy.txt', 'r').read()
	print('Message laid!')
	encrKey = makeCipher(message)
	print('Cipher created!')
	return encrKey