
"""
	run4.py
	Autor: Juan Pablo
	
	Deseamos obtener el costo de una carrera universitaria.
	El valor promedio de cada ciclo es de 1200 dolares.
	El valor promedio del seguro educativo por ciclo es de 100$. si la edad del estudiante es menor 0 igual a 20 caso contrario sera de 150$
	Si el estudiante Tiene una modalidad a distancia el numero de ciclos a seguir es de 10 caso contrario debera seguir 8 ciclos
	obtener la proyeccion del costo de la carrera de uun estudiante
"""


#pedimos por teclado los datos
modalidad = input("Ingrese su modalidad: \n")
edad = input("ingrese su edad \n")
edad = int(edad)

#declaramos la variables
ciclos = 0
valorSeguroFinal = 0
valorMatriculaInicial = 1200
valorMatriculaFianl = 0

#validamos la edad para calcular el seguro
if edad <= 20:
	seguro = 100
else:
	seguro = 150

#validamos en la modalidad que va a estudiar
if modalidad == "Distancia":
	ciclos = 10
	valorSeguroFinal = seguro * ciclos
	print(valorSeguroFinal)
	valorMatriculaFianl =  (valorMatriculaInicial * ciclos) + valorSeguroFinal
	print("Usted debera seguir %d, en modalidad %s y su precio a final por la carrera sera de : %d" % (ciclos, modalidad, valorMatriculaFianl))
else:
	ciclos = 8
	valorSeguroFinal = seguro * ciclos
	print(valorSeguroFinal)
	valorMatriculaFianl = (valorMatriculaInicial * ciclos) + valorSeguroFinal
	print("Usted debera seguir %d, en modalidad %s y su precio a final por la carrera sera de : %d" % (ciclos, modalidad, valorMatriculaFianl))