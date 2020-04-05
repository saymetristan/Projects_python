# -*- coding: utf-8-*-

import random


def palindrome(word):
	reversed_letters = []

	for letter in word:
		reversed_letters.insert(0,letter)

	reversed_word = "".join(reversed_letters)

	if reversed_word == word:
		print("Verdadero")
	else:
		print("Falso")
	


if __name__ == "__main__":
	word = str(raw_input("Escribe una palabra: "))
	palindrome(word)