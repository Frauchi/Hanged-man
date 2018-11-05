import random

aciertos = []
fallos = []


def longitud(lista):
	cantidad = 0

	for elemento in lista:
		cantidad = cantidad + 1
		
	return cantidad


def dibujo(fallos):
	
	longitud_fallos = longitud(fallos)
	parte_superior = "______" "\n" 
	parte_inferior = "-------" "\n" "|_____|"

	if longitud_fallos == 0:
		centro ="|" "\n" "|" "\n" "|" "\n" "|" "\n" "|" "\n"

	elif longitud_fallos == 1:
		centro = "|    |" "\n" "|" "\n" "|" "\n" "|" "\n" "|" "\n"

	elif longitud_fallos == 2:
		centro = "|    |" "\n" "|    O" "\n" "|" "\n" "|" "\n" "|" "\n"

	elif longitud_fallos == 3:
		centro = "|    |" "\n" "|    O" "\n" "|    |" "\n" "|" "\n" "|" "\n"

	elif longitud_fallos == 4:
		centro = "|    |" "\n" "|    O" "\n" "|   /|" "\n" "|" "\n" "|" "\n"

	elif longitud_fallos == 5:
		centro = "|    |" "\n" "|    O" "\n" r'|   /|\ ' "\n" "|" "\n" "|" "\n"

	elif longitud_fallos == 6:
		centro = "|    |" "\n" "|    O" "\n" r'|   /|\ ' "\n" "|   /" "\n" "|" "\n"

	elif longitud_fallos == 7:
		centro = "|    |" "\n" "|    O" "\n" r'|   /|\ ' "\n" r'|   / \ ' "\n" "|" "\n"

	print(parte_superior + centro + parte_inferior)



def contiene(lista, valor):
	for elemento in lista:
		if elemento == valor:
			return True

	return False


def ahorcado(fallos):
	if longitud(fallos) < 7:
		return False
	else:
		return True


def ganador(aciertos):
	for letra in palabra:
		if not contiene(aciertos, letra):
			return False

	return True


palabras = ['casa', 'barco', 'culpa', 'dado', 'ejemplo']
indice = random.randint(0, longitud(palabras) - 1)
palabra = (palabras[indice])


while ahorcado(fallos) != True and ganador(aciertos) != True:
	
	letra = input("Elige una letra: ")

	if contiene(palabra, letra):
		aciertos = aciertos + [letra]
	else:
		fallos = fallos + [letra]

	dibujo(fallos)
	
	print("\n" "Letras erróneas:", ",".join(fallos), "\n" "Letras acertadas:", ",".join(aciertos))


if ganador(aciertos) == True:
	print("Has ganado, la palabra era " + palabra + "!")
else:
	print("Has perdido, la palabra era " + palabra + ".")
