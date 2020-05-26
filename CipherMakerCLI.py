import getCipher as gc
import keyGenerator as kg
import os
import glob, json
import getMessage as gm
import fileManager as fm

def cipherMessage(securityKey, recieversKey):
	message = input('Enter your message: ')
	fm.createFile(message, 'messageCopy', '.txt', 'w')
	encrKey = gc.getCipher()
	os.system('del public.key')
	if(securityKey == recieversKey):
		securityKeyWithEncr = securityKey + encrKey
	else:
		securityKeyWithEncr = recieversKey + encrKey
	open('public.key','w').write(securityKeyWithEncr)

def decipherCipher(yPhase):
	fileCipher = open("finalMessage.txt", 'rb').read().decode('utf-8')
	message = gm.getMessageFromCipher(fileCipher, yPhase)
	print(message)

def mainCLIAction(securityKey, recieversKey):
	while(True):
		userInfo = input('Enter your choice: ')
		if(userInfo == 'Enc'):
			cipherMessage(securityKey, recieversKey)
			break
		elif(userInfo == 'Dec'):
			securityKeyWithEncr = open('public.key','r').read()
			privateKey = open('private.key', 'r').read()
			if(securityKeyWithEncr[:47] == privateKey):
				decipherCipher(securityKeyWithEncr[47:len(securityKeyWithEncr)])
			else:
				print("You have wrong public key!")
			break
		else: 
			print('Enter correct option')

def checkForKey():
	getKeyVector = glob.glob('*.key')
	if(len(getKeyVector) > 1):
		print('Reading existing unique key!')
		with open("private.key",'r') as keyFile:
			securityKey = keyFile.read()
	else:
		print('Generating new key!')
		securityKey = kg.getKey(47)
		with open('private.key', 'w') as keyFile:
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