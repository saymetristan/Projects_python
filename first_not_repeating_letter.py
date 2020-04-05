# -*- coding: utf-8 -*-

def first_not_repeating_char(char_sequence):
    #Se declara un diccionario, y se itera toda la secuencia de caracteres obteniendo el indice y las letras
    seen_letters = {}

    for idx, letter in enumerate(char_sequence):
        #si la letra ya la vimos se marca y la guardamos en una tupla 
    	if letter not in seen_letters:
    		seen_letters[letter] = (idx, 1)
        #Si no es el caso se guarda su posicion y cuantas veces la vimos
    	else:
    		seen_letters[letter] = (seen_letters[letter][0], seen_letters[letter][1] + 1) 

    #declamramos una variable que almacena una tupla de que letras vimos una vez
    final_letters = []
    for key, value in seen_letters.items():
    	if value[1] == 1:
    		final_letters.append( (key, value[0]) )

    #Definimos una nuevsa variable que almacenara el primer elemento de la lista de forma ordenada
    not_repeated_letters = sorted(final_letters, key=lambda value: value[1])

    #Si la estructura variable tiene algo entonces devuelve el caracter, si no devuelve un guion
    if not_repeated_letters:
    	return not_repeated_letters[0][0]
    else:
    	return '_'

if __name__ == '__main__':
    char_sequence = str(raw_input('Escribe una secuencia de caracteres: '))

    result = first_not_repeating_char(char_sequence)

    if result == '_':
        print('Todos los caracteres se repiten.')
    else:
        print('El primer caracter no repetido es: {}'.format(result))