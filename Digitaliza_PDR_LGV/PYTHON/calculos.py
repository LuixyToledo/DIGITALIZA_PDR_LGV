from operaciones import *
a = 0
b = 0
dict1 = {"1":"suma", "2":"resta", "3":"producto", "4":"division", "5":"potencia", "6":"salir"}
print("CALCULADORA")
while(True):
	try:
		a = int(input("Introduce un numero: "))
		b = int(input("Introduce otro numero: "))
		break
	except ValueError:
		print("Introduce un entero!!!")
while(True):
	print("----------MENÚ----------\n----------\n1.- Suma\n2.- Resta\n3.- Multìplicacion\n4.- Division\n5.- Potencia\n6.- Salir")
	try:
		opc = int(input("Introduce una opcion: "))
		if str(opc) in dict1:
			print("Has elegido ",dict1[str(opc)])
			while(True):
				if opc == 1:
					print("{} + {} = {}".format(a,b,suma(a,b)))
					break
				elif opc == 2:
					print("{} - {} = {}".format(a,b,resta(a,b)))
					break
				elif opc == 3:
					print("{} * {} = {}".format(a,b,producto(a,b)))
					break
				elif opc == 4:
					print("{} / {} = {}".format(a,b,division(a,b)))
					break
				elif opc == 5:
					print("{} ^ {} = {}".format(a,b,potencia(a,b)))
					break
				elif opc == 6:
					print("HASTA LUEGO!!!")
					exit()
		else:
			print("Introduce una opcion entre 1 y 6. No es tan complicado.....")
	except ValueError:
		print("Error: Tipo de dato no válido")