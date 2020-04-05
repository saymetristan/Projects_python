# -*- coding: utf-8 -*-

def calificaciones():
	calif = {}
	calif['algoritmos'] = 9
	calif['matematicas'] = 10
	calif['web'] = 8
	calif['base_de_datos'] = 10

	for key in calif:
		print (key)

	for value in calif.values():
		print(value)

	for key, value in calif.items():
		print('llave: {}, valor: {}'.format(key, value))

	suma_de_calificaciones = 0
	for calificacion in calif.values():
		suma_de_calificaciones += calificacion
		promedio = suma_de_calificaciones / len(calif)
	print('Promedio: {}'.format(promedio))


if __name__ == '__main__':
	calificaciones()