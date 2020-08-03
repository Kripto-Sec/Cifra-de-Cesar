import sys 
ALFABETO = 'abcdefghijklmnopqrstuvwxyz'
ROTA = 13

print '###################################'
print '#         CIFRA DE CESAR          #' 
print '#                                 #'
print '# https://github.com/Kripto-Sec   #'
print '#   :)                            #'
print '###################################'



def cifra(message, dir):
	m = ''
	for c in message:
		if c in ALFABETO:
			c_index = ALFABETO.index(c)
			m += ALFABETO[(c_index + (dir *ROTA)) % len(ALFABETO)]
		else:
			m += c
	return m 

def encrypt(message):
	return cifra(message, 1)



def decrypt(message):
	return cifra(message, -1)

def main():
	command = sys.argv[1].lower()
	message = sys.argv[2].lower()

	if command == '-e':
		print encrypt(message)
	elif command == '-d':
		print decrypt(message)
	else:
		print command + ' NAO ENCONTRADO TENTE python cifra_cesar.py -e OU -d frase(entre aspas) '

if __name__ == '__main__':
	main()
