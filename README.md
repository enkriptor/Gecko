# Encrypter
An encryption daemon to encrypt a message using keys generated.

[![Generic badge](https://img.shields.io/badge/Release-v1.5.2-<COLOR>.svg)](https://shields.io/)

## What's new feature in v1.5.3?
* Created seperate key generation
* Created the `.exe` application of the source

# For Windows Users:
* Goto the `dist` folder and run the `CipherMakerCLI.exe`
* Enter `y` to continue doing encryption or decryption or `n` to only generate the `private.key` for your system
* If you have entered `y`, then follow the instructions as given on the CLI
* Enter the key recipient a.k.a the `private.key` of the person you want to send the encrypted message. You can leave it blank and `Enter` if the recipient is you yourself!
* You'll then get the option to encrypt or decrypt the message by typing `Enc` or `Dec` respectively!
* For encryption, type `Enc` and hit `Enter`
* Then enter the message you want to encrypt and `Enter`
* You will get the following files `finalMessage.txt`(contains encrypted message), `messageCopy.txt`(contains a copy of the original message), `private.key`(contains the unique private key for your system) and `public.key`(contains encrypted key to be sent with `finalMessage.txt`)
* You can share the `finalMessage.txt` and `public.key` with your concerned recipient.
* For decryption, type `Dec` and hit `Enter`
* You will be prompted by the message you want to see
* The decryption requires you to have the `finalMessage.txt` and `public.key` you received to decrypt the encrypted message.

# For developers:
## Prerequisites
* Download and setup python from (www.python.org)
* Download or clone the repository to your system

## How to run the daemon?
* Goto the `src` folder for the main and linked daemons!
### Encryption of text
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
* The daemon will generate a unique `private key` if not already present on the system otherwise will read the existing key.
* The daemon will prompt for the receiver's unique `public key`, if left blank and `Enter` receiver's key will be the existing unique key from the system.
* The daemon will prompt you to enter your choice of `Enc` and `Dec` to enter
* `Enc` is for encrypting a message
* Enter `Enc` and hit `Enter`
* The daemon will prompt you to enter your message
* Enter your message and hit `Enter`
* The cipher will be stored in a file `finalMessage.txt`
* The original message will be stored in `messageCopy.txt`
* You can now share `finalMessage.txt` and `public.key` with your friends

### Decryption of cipher
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
* The daemon will generate a unique key if not already present on the system otherwise will read the existing key.
* The daemon will prompt for the receiver's unique key, if left blank and `Enter` receiver's key will be the existing unique key from the system.
* The daemon will prompt you to enter your choice of `Enc` and `Dec` enter
* `Dec` is for decrypting the existing cipher
* Enter `Dec` and hit `Enter`
* You will get your original message 