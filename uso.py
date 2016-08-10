from cuadrado import Cuadrado


mi_cuadrado_2 = Cuadrado(10)


print("1)elejir una figura")
print("2)salir")
resp=int(input("elija una opcion"))
if resp==1:
	print("1)Cuadrado 2)tRIANGULO")
	figura=int(input("ELIJA UNA figura"))
	if figura==1:
		num=int(input("Ingrese la base"))
		mi_cuadrado_1 = Cuadrado(num)








print("Area:", mi_cuadrado_1.calcular_area())
print(mi_cuadrado_1.imprimir())

print("Area:", mi_cuadrado_2.calcular_area())
print(mi_cuadrado_2.imprimir())

