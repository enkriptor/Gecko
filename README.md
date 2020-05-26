# Encrypter
An encryption daemon to encrypt a message using keys generated.

[![Generic badge](https://img.shields.io/badge/Release-v1.4.2-<COLOR>.svg)](https://shields.io/)

# Prerequisites
* Download and setup python from (www.python.org)
* Download or clone the repository to your system

# What's new feature in v1.4.2?
* Change in algorithm
* Added user private and sharable public key generation feature.
* Removed the previous limit of 300 character message for encryption and decryption.
* Simpler ways to handle the encrypted messages and keys.

# How to run the daemons?
## Encryption of text
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

## Decryption of cipher
* Open command prompt or shell(Linux/Unix)
* Type `python CipherMakerCLI.py` and hit `Enter`
* The daemon will generate a unique key if not already present on the system otherwise will read the existing key.
* The daemon will prompt for the receiver's unique key, if left blank and `Enter` receiver's key will be the existing unique key from the system.
* The daemon will prompt you to enter your choice of `Enc` and `Dec` enter
* `Dec` is for decrypting the existing cipher
* Enter `Dec` and hit `Enter`
* You will get your original message 