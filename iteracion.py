# -*- coding: utf-8-*-


def main(number, number2):
	for i in range (number):
		print ("*" * i)
	for i in range (number):
		print ("*" * (number2-i))


if __name__ == "__main__":
	print("I T E R A C I O N")
	print(" ")
	number = int(raw_input("Escribe un número: "))
	number2=number
	main(number,number2) 