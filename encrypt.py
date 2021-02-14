import sys
import rsa
import time
def encrpt(message,publicKey,publicKeySub):
	publicKey = rsa.key.PublicKey(publicKey,publicKeySub)
	encmessage = rsa.encrypt(str(message).encode(),publicKey)
	return encmessage
def decrypt(message,*privateKey):
	privateKey = rsa.key.PrivateKey(*privateKey)
	print("*"*20,privateKey,type(privateKey))
	decryptmessage = rsa.decrypt(message.encode(), privateKey)
	return decrypt
def generateKey(lengthKey):
    return rsa.newkeys(lengthKey)
# publicKeyex = str(sys.argv[2])
print("="*10)
print("="*3,"MENU","="*3)
print("1.Encrpt Message")
print("2.Decrypt Message")
print("3.Generate Public and PrivateKey")
print("="*10)
option = int(input("what you gonna do do do? : "))
if option == 2:
	message = str(input("message to be decrypt : "))
	print(type(message))
	publicKey = str(input("the publicKey ? "))
	publicKey = ''.join(publicKey.split(','))
	publicKey = publicKey.split(' ')
	print(publicKey)
	time.sleep(10)
	try:
		print("="*10,"The message is decrypt\n",decrypt(message,int(publicKey[0]),int(publicKey[1]),int(publicKey[2]),int(publicKey[3]),int(publicKey[4])))
	except Exception as e:
		raise e
if option == 1:
	message = str(input("message to be encrypted : "))
	publicKey = str(input("the publicKey ? "))
	publicKey = ''.join(publicKey.split(','))
	publicKey = publicKey.split(' ')
	print(publicKey[0],publicKey[1])
	print("You will encrypt the message")
	time.sleep(3)
	try:
		print("="*10,"The message is encrypted\n",encrpt(message,int(publicKey[0]),int(publicKey[1])))
	except Exception as e:
		raise e
# print("The message is encrypted\n",encrpt(sys.argv[1],sys.argv[2],sys.argv[3]))
if option == 3:
	print("Key length should be atleast 16")
	lengthKey = int(input("How long the key do want ? "))
	for i in range(5):
		print("process"+"."*i)
		time.sleep(1)
	publicKey,privateKey = (generateKey(lengthKey))
	print("="*10)
	print("PublicKey\n",publicKey)
	print("PrivateKey\n",privateKey)
	print("="*10)
