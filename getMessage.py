import workflowUtils as wu 

def getMessageFromCipher(fileCipher, yPhase):
	originalMessage = wu.getPrintables(wu.getBitMessage(wu.getNumericEncrypted(fileCipher), int(yPhase)))
	return originalMessage