# -*- coding: utf-8 -*-
import random


IMAGES = ['''

    +---+
    |   |
        |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
        |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
    |   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|   |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
        |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
        |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   /    |
        =========''', '''

    +---+
    |   |
    O   |
   /|\  |
    |   |
   / \  |
        =========''', '''
''']

WORDS = [
    'ablandar',
    'avestruz',
    'agricola',
    'almohada',
    'corredor',
    'concepto',
    'industria',
    'computadora',
    'refrigerador',
    'manzana',
    'murcielago',
    'ferrocarril',
    'puerta',
    'elevador',
    'chimenea',
    'platano'
]

#Aqui se genera el display juego
def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print('')
    print(hidden_word)
    print('')
    print('')

#Se genera una palabra aleatoria en base a las palabras programadas
def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]

#Esta es la funcion principal, pide una palabra y entra en un ciclo, termina cuando haces los 7 intentos oa ciertas
def run():
    word = random_word()
    hidden_word = ['-'] * len(word)
    tries = 0
    
    while True:
        #Se muestra el teclado y se pide introducir una letra
        display_board(hidden_word, tries)
        current_letter = str(raw_input('Escoge una letra: '))

        #Se compara la letra introducida con cada letra de la palabra que el juego eligio, en caso de ser igual a alguna rellena la bandera
        letter_indexes = []
        for idx in range(len(word)):
            if word[idx] == current_letter:
                letter_indexes.append(idx)

        #Si la bandera queda vacia se agrega un intento, si llega a 7 intentos termina el juego        
        if len(letter_indexes) == 0:
            tries += 1

            if tries == 7:
                display_board(hidden_word, tries)
                print('')
                print('¡Perdiste! La palabra correcta era: {}'.format(word))
                break
        #Si la bandera tiene algo quiere decir que la letra era correcta y se agrega la letra a los espacios de hidden_word        
        else:
            for idx in letter_indexes:
                hidden_word[idx] = current_letter

            letter_indexes = []

        #El juego termina tambien si ya no quedan - en la lista hidden_word
        try:
            hidden_word.index('-')
        except ValueError:
            print('')
            print('¡Felicidades, Ganaste! La palabra es: {}'.format(word))
            break

 #Aqui inicia el codigo           
if __name__ == '__main__':
    print('A H O R C A D O')
    run()
















