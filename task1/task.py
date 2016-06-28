from Crypto.Cipher import AES
import sys
import time
import md5

def	DecryptFile(filename, password):
	inF = open(filename, 'r')
	inData = inF.read()
	inF.close()

	aes = AES.new(password, AES.MODE_ECB)
	outData = aes.decrypt(inData)

	outData = outData[:-ord(outData[-1])]

	decryptedFileName = filename + '.dec'
	outF = open(decryptedFileName, 'w')
	outF.write(outData)
	outF.close()

	print 'Written ' + decryptedFileName

def	EncryptFile(filename):
	PASSWORD_LEN = 32
	password = ''
	ts = int(time.time())
	alphabet = 'abcdefghijklmnopqrstuvwxyz0123456789'
	for i in range(0, 32):
		password += alphabet[ts % len(alphabet)]
		ts = ( ( ts * 0xB11924E1 ) + 0x27100001 ) >> 8

	print 'Password: ' + password

	inF = open(filename, 'r')
	inData = inF.read()
	inF.close()

	length = 32 - (len(inData) % 16)
	inData += chr(length)*length

	aes = AES.new(password, AES.MODE_ECB)
	outData = aes.encrypt(inData)

	encryptedFileName = filename + '.enc'
	outF = open(encryptedFileName, 'w')
	outF.write(outData)
	outF.close()

	print 'Written ' + encryptedFileName

if ( len(sys.argv) <= 1 ):
	print 'Usage:\n -e encrypt_file_name\n -d decrypt_file_name password\n'
	exit(0)

if ( sys.argv[1] == '-d' ) :
	if ( len(sys.argv) < 4 ) :
		print 'Need filename and password\n'
		exit(1)
	DecryptFile(sys.argv[2], sys.argv[3])

if ( sys.argv[1] == '-e' ) :
	if ( len(sys.argv) < 3 ) :
		print 'Need filename\n'
		exit(1)
	EncryptFile(sys.argv[2])


