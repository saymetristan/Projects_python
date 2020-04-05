# -*- coding: utf-8 -*-

COUNT = 0

def binary_search(numbers, number_to_find, low, high):

	global COUNT 

	COUNT += 1
	
	#Si el indice low se vuelve mas alto que high regresa False
	if low  > high:
		return False

	#Se genera un indice mid para comenzar a buscar a la mitad	
	mid = (low + high) / 2

	#Si el numero de la mitad es el numero a buscar regresa True
	if numbers[mid] == number_to_find:
		return True

	#Si el numero de la mitar es mas grande que el numero a encontrar se genera una recursión en la mitad de numeros inferiores
	elif numbers[mid] > number_to_find:
		return binary_search(numbers, number_to_find, low, mid - 1)

		#Si el numero de la mitar es mas chico que el numero a encontrar se genera una recursión en la mitad de numeros suèriores	
	else: 
		return binary_search(numbers, number_to_find, mid + 1, high)


if __name__ == '__main__':
	numbers = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]

	number_to_find = int(raw_input('Ingresa un numero: '))

	result = binary_search(numbers, number_to_find, 0, len(numbers) - 1) 

	if result is True:
		print('El numero esta en la lista y tarde {} ciclos en saberlo' .format(COUNT))
	else:
		print('El numero no esta en la lista y tarde {} ciclos en saberlo' .format(COUNT))