import sys
import rsa
import time
def decrypt(message,*privateKeys):
	print("\n\n\n\n",*privateKey)
	privateKey = rsa.key.PrivateKey(*privateKeys)
	print("*"*20,privateKey,type(privateKey))
	decryptmessage = rsa.decrypt(message.encode(), privateKey)
	return decrypt
# print(sys.argv[1])
# print(rsa.key.PrivateKey(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5])))
privasi = rsa.key.PrivateKey(int(sys.argv[1]),int(sys.argv[2]),int(sys.argv[3]),int(sys.argv[4]),int(sys.argv[5]))
# print("="*50,"\n",privasi)
# message = input()
# message = (b'a\xafY\x89\x14\xfcE\x1b\xef\xeec+zK\x8b\xcbL~\xa1\xa6\xd5y\xb6w\x0eu}\xc9\xea\x7f\xf3k,_\x1d6\xdc\x0e\xdd\x9ai\xd4\xbb\x00w\xc9\rs\xe1\xfe\x12\t[xz\x1d\xa7\x07\x1e\xa8\x1bV.\xe3')
# message = bytes('a\xafY\x89\x14\xfcE\x1b\xef\xeec+zK\x8b\xcbL~\xa1\xa6\xd5y\xb6w\x0eu}\xc9\xea\x7f\xf3k,_\x1d6\xdc\x0e\xdd\x9ai\xd4\xbb\x00w\xc9\rs\xe1\xfe\x12\t[xz\x1d\xa7\x07\x1e\xa8\x1bV.\xe3')
# print(message,type(message))
print(rsa.decrypt(sys.argv[1],privasi))