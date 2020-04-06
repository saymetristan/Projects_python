def primos():
	number = int(raw_input("Escribe in numero: "))
	result=calculos(number)

	if result is True:
		print("Tu numero es primo")
	else:
		print("Tu numero no es primo")

def calculos(number):
	if number < 2 :
		return False
	elif number == 2:
		return True
	elif number > 2 and number % 2 == 0:
		return False
	else:
		for i in range(3, number):
			if number % i == 0:
				return False
	return True

if __name__ == "__main__":
    primos()