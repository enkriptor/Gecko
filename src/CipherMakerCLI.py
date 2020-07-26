import os, glob 
import middleWare as mw 

def mainCLIAction():
	securityKey, receiversKey, useCLI = mw.manageKey()
	while(useCLI):
		userInfo = input('Enter your choice: ')
		if(userInfo == 'Enc'):
			mw.cipherMessage(securityKey, receiversKey)
			break
		elif(userInfo == 'Dec'):
			securityKeyWithEncr = open('public.key','rb').read().decode('utf-8')
			publickeyElems = "".join([str(ord(element)) for element in securityKeyWithEncr])
			privateKey = open('private.key', 'r').read()
			privatekeyElems = "".join([str(ord(element)) for element in privateKey])
			encrKey = int(publickeyElems[:617]) - int(privatekeyElems[:617])
			if(encrKey<0):
				encrKey = int(publickeyElems[:618]) - int(privatekeyElems[:617])
			mw.decipherCipher(encrKey)
			break
		else: 
			print('Enter correct option')

mainCLIAction()