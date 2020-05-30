import getCipher as gc
import os, glob 
import getMessage as gm
import workflowUtils as wu

def cipherMessage(securityKey, receiversKey):
	message = input('Enter your message: ')
	open('messageCopy.txt', 'w').write(message)
	encrKey = gc.getCipher()
	os.system('del public.key')
	securityKeyWithEncr = wu.getPrintables(wu.embedKeyIntoMessage(int(encrKey), wu.getBitMessageDirect(receiversKey)))
	open('public.key','wb').write(securityKeyWithEncr.encode('utf-8'))

def decipherCipher(yPhase):
	fileCipher = open("finalMessage.txt", 'rb').read().decode('utf-8')
	message = gm.getMessageFromCipher(fileCipher, yPhase)
	print(message)

def mainCLIAction(securityKey, receiversKey):
	while(True):
		userInfo = input('Enter your choice: ')
		if(userInfo == 'Enc'):
			cipherMessage(securityKey, receiversKey)
			break
		elif(userInfo == 'Dec'):
			securityKeyWithEncr = open('public.key','rb').read().decode('utf-8')
			publickeyElems = "".join([str(ord(element)) for element in securityKeyWithEncr])
			privateKey = open('private.key', 'r').read()
			privatekeyElems = "".join([str(ord(element)) for element in privateKey])
			encrKey = int(publickeyElems[:17]) - int(privatekeyElems[:17])
			if(encrKey<0):
				encrKey = int(publickeyElems[:18]) - int(privatekeyElems[:17])
			decipherCipher(encrKey)
			break
		else: 
			print('Enter correct option')

def checkForKey():
	newkeyStatus = False
	getKeyVector = glob.glob('*.key')
	if("private.key" in getKeyVector):
		print('Reading existing unique key!')
		with open("private.key",'r') as keyFile:
			securityKey = keyFile.read()
	else:
		print('Generating new key!')
		securityKey = wu.getAddressKey(47)
		with open('private.key', 'w') as keyFile:
			keyFile.write(securityKey)
			newkeyStatus = True
	return securityKey, newkeyStatus

securityKey, newkeyStatus = checkForKey()
while(True):
	if(newkeyStatus):
		print("Private key generated")
	choice = input("Do you want to continue? Enter y to continue or n to exit: ")
	if(choice == "y"):
		print("Enter the key of the recipient or leave it blank if you're the recipient!")
		receiversKey = input("Enter receiver's unique key: ")
		if(receiversKey == ""):
			print("Assigning key to self!")
			receiversKey = securityKey
		print("Enter \'Enc\' to encrypt a message and \'Dec\' to decrypt an existing cipher!")
		mainCLIAction(securityKey, receiversKey)
		os.system('pause')
		break
	elif(choice == "n"):
		print("Aborting the application!")
		os.system('pause')
		break
	else: 
		print("Please enter right choice!")