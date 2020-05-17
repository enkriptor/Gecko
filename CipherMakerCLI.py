import getCipher as gc
import keyGenerator as kg
import os
import glob, json
import getMessage as gm
import fileManager as fm

jsonData = fm.getFile('generalConstants.json', 'r')
jsonParse = json.loads(jsonData)

def cipherMessage(securityKey, recieversKey):
	message = input('Enter your message: ')
	fm.createFile(message, 'messageCopy', '.txt', 'w')
	if(len(message)<=jsonParse['lengthMessage']):
		fm.createFile(gc.getCipher(securityKey, recieversKey), kg.getKey(25), '.enc', 'w')
	else:
		print("Enter message of length less than 300")

def decipherCipher(getFileName, securityKey, recieversKey):
	fileCipher = fm.getFile(getFileName, 'r')
	message = gm.getMessageFromCipher(fileCipher, securityKey, recieversKey)
	print(message)

def mainCLIAction(securityKey, recieversKey):
	while(True):
		userInfo = input('Enter your choice: ')
		if(userInfo == 'Enc'):
			cipherMessage(securityKey, recieversKey)
			break
		elif(userInfo == 'Dec'):
			getFileNameVector = glob.glob('*.enc')
			for getFileName in getFileNameVector:
				if(getFileName):
					decipherCipher(getFileName, securityKey, recieversKey)
				else:
					print('Cipher a message first!')
					break
			break
		else: 
			print('Enter correct option')

def checkForKey():
	getKeyVector = glob.glob('*.key')
	if(len(getKeyVector)>1):
		print("Multiple keys exist! Aborting the process!")
		os.system('exit')
	else:
		if(len(getKeyVector) == 1):
			print('Reading existing unique key!')
			with open(getKeyVector[0],'r') as keyFile:
				securityKey = keyFile.read()
		else:
			print('Generating new key!')
			securityKey = kg.getKey(47)
			with open(kg.getKey(25)+'.key', 'w') as keyFile:
				keyFile.write(securityKey)
	return securityKey

securityKey = checkForKey()
recieversKey = input("Enter receiver's unique key: ")
if(recieversKey == ""):
	print("Assigning key to self!")
	recieversKey = securityKey
print("Enter \'Enc\' to encrypt a message and \'Dec\' to decrypt an existing cipher!")
mainCLIAction(securityKey, recieversKey)
os.system('pause')