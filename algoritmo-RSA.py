
"""
Universidad del Valle de Guatemala 
Seguridad en sistemas de computación

Pablo Viana - 16091

Implementación de algoritmo RSA con tres modos de ejecución 

1. Creación de llaves (pública, privada).
2. Cifrado de mensaje dado una llave pública y el mensaje a cifrar. 
3. Descifrado de mensaje dado un ciphertext y una llave privada.
"""
import random

NUM_RAND = 521568765413

"""
	Función para calcular el máximo común divisor
"""
def gcd(a, b):
	while b != 0:
		c = a % b
		a = b
		b = c
	return a

"""
	Funcion de modulo inverso
"""
def modinv(a, m):
	for x in range(1, m):
		if (a * x) % m == 1:
			return x
	return None

"""
	Función para encontrar un número coprimo de a
"""
def coprimes(a):
	l = []
	for x in range(2, a):
		if gcd(a, x) == 1 and modinv(x,a) != None:
			l.append(x)
	for x in l:
		if x == modinv(x,a):
			l.remove(x)

	try:
		random.shuffle(l)
		return l.pop()
	except IndexError as e:
		print("Los números escogidos no son números primos")
		return None

def creacion_llaves():
	try:
		prim_uno = int(input("Eliga el primer número primo: "))
	except ValueError as e:
		prim_uno = NUM_RAND
		pass

	try:
		prim_dos = int(input("Eliga el segundo número primo: "))
	except ValueError as e:
		prim_dos = NUM_RAND
		pass

	if prim_uno == NUM_RAND or prim_dos == NUM_RAND:
		print("solo numeros")
	else:
		#Calculamos n 
		N = prim_uno * prim_dos

		#Calculamos la función phi de Euler
		phi = (prim_uno-1)*(prim_dos-1)

		e = coprimes(phi)
		d = modinv(e, phi)

		print("llave publica: " + str(e) + str(N))
		print("e: " + str(e))
		print("llave privada: " + str(d) + str(N))
		print("d: " + str(d))
		print("n: " + str(N))

		#Creamos archivo con las llaves
		text_file = open("llave.txt", "w")
		text_file.write(" n = " + str(N))
		text_file.write(" e = " + str(e))
		text_file.write(" d = " + str(d))
		text_file.write(" llave pública = " + str(e) + str(N))
		text_file.write(" llave privada = " + str(d) + str(N))
		text_file.close()

def encriptar(m, e, n):
	cipher = modinv(m**e, n)
	if cipher == None: print("no existe un modular inverso para este bloque "+ str(m))
	return cipher

def descifrar(m, d, n):
	s = modinv(m**d, n)
	if s == None: print("no existe un modular inverso para este bloque "+ str(m))
	return s

def menu():

	flag = True

	print("------------- Bienvenido implementación algoritmo RSA -------------")
	print("1. creación de llave pública y privada")
	print("2. cifrado de mensaje (se necesita una llave pública)")
	print("3. descifrado de mensaje (se necesita una llave pública)")
	
	while(flag):
		try:
			res = int(input("Eliga una opción: "))
		except ValueError as e:
			res = NUM_RAND
			pass


		if res == 1:
			creacion_llaves()
			flag = False
		elif res == 2:
			msg = input("mensaje para encriptar: ")
			e = int(input("ingrese <e> de su llave pública: "))
			n = int(input("ingrese <n> de su llave pública: "))
			#ciframos mensaje
			cipher = ''.join([chr(encriptar(ord(x), e, n)) for x in list(msg)])
			print("mensaje encriptado: " + cipher)

			flag = False
		elif res == 3:
			msg = input("mensaje para descifrar: ")
			d = int(input("ingrese <d> de su llave pública: "))
			n = int(input("ingrese <n> de su llave pública: "))
			#desciframos mensaje
			simpletxt = ''.join([chr(encriptar(ord(x), d, n)) for x in list(msg)])
			print("mensaje descifrado: " + simpletxt)
			flag = False
		elif res == NUM_RAND:
			print("solo numeros")
		else:
			print("ingrese opción válida")

if __name__ == '__main__':
	menu()