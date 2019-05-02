"""
	run2.py
	Autor: Juan Pablo
"""

from misVariable import *

#uso de condicional simple


nota= input("Ingrese la nota 1: \n")
nota2 = input("Ingrese nota 2: \n")

nota = int(nota)
nota2 = int(nota2)

if nota >= 18:
	print("%s, su nota es: %d" % (mensaje, nota))
else:
	print("%s, su nota es: %d" % (mensaje2, nota))

if nota2 >= 18:
	print("%s, su nota es: %d" % (mensaje, nota2))
else:
	print("%s, su nota es: %d" % (mensaje2, nota2))

