# -*- coding: utf-8-*-

import random


def adivinar(num):
	number_found= False
	random_number = random.randint(0,num)

	while not number_found:
		number = int(raw_input("Adivina el numero: "))

		if number == random_number:
			print("Felicidades encontraste el numero")
			number_found = True
		elif number > random_number:
			print("El numero es mas pequeño")
		else:
			print("El numero es mas grande")


if __name__ == "__main__":
	num = int(raw_input("Hasta que numeros quieres adivinar: "))
	adivinar(num)