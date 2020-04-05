# -*- coding: utf-8-*-
def say_hello():
	print("c o n d i c i o n a l e s")
	print(" ")
	age = float(raw_input("¿Cual es tu edad?: "))
	if age > 18:
	    print("hola señor")
	else:
		print("hola niño")

if __name__ == "__main__":
    say_hello()