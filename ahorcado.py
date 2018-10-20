import random

aciertos = []
fallos = []


def longitud(lista):
	cantidad = 0

	for elemento in lista:
		cantidad = cantidad + 1
		
	return cantidad


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

	print("\n" "Letras erróneas:", ",".join(fallos), "\n" "Letras acertadas:", ",".join(aciertos))


if ganador(aciertos) == True:
	print("Has ganado, la palabra era " + palabra + "!")
else:
	print("Has perdido, la palabra era " + palabra + ".")
