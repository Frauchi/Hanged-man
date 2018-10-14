import random

palabras = ['casa', 'barco', 'culpa', 'dado', 'ejemplo']
indice = random.randint(0, longitud(palabras) - 1)
palabra = (palabras[indice])

aciertos = []
fallos = []

aciertos = 

letra_elegida = input("Elige una letra: ")

def longitud(lista):
	cantidad = 0

	for elemento in lista:
		cantidad = cantidad + 1
		
	return cantidad


def contiene(lista, valor):
	for elemento in lista:
		if elemento == valor:
			return True
		else:
			return False


def ahorcado(fallos):
	if longitud(fallos) <= 7:
		return False
	else:
		return True


def actualizar(palabra, letra, aciertos, fallos):
	if contiene(palabra, letra):	
		return (aciertos + [letra], fallos)
	else:
		return (aciertos, fallos + [letra])
	

