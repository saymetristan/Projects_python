# -*- coding: utf-8-*-


def factorial(number):
	if number == 0:
		return 1

	return number * factorial(number - 1)



if __name__ == "__main__":
	print("c o n d i c i o n a l e s")
	print(" ")
	number = int(raw_input("Escribe un número: "))

	result = factorial(number)

    print(result)