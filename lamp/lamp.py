# -*- coding: utf-8 -*-

#Clases inician con mayuscula y se escriben en camel
class Lamp:
	_LAMPS = ['''
          .
     .    |    ,
      \   '   /
       ` ,-. '
    --- (   ) ---
         \ /
        _|=|_
       |_____|
    ''',
    '''
         ,-.
        (   )
         \ /
        _|=|_
       |_____|
    ''']

    #Se define la clase lampara, con sus metodos de encendido, apagado y el display de la imagen 
	def __init__(self, is_turned_on):
		self._is_turned_on = is_turned_on

	def turn_on(self):
			self._is_turned_on = True
			self._display_image()

	def turn_off(self):
		self._is_turned_on = False
		self._display_image()

	def _display_image(self):
		if self._is_turned_on:
			print(self._LAMPS[0])
		else:
			print(self._LAMPS[1])