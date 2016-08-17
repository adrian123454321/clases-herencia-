from cuadrado import Cuadrado
from triangulo import Triangulo





print("1)elejir una figura")
print("2)salir")
resp=int(input("elija una opcion"))
if resp==1:
	while resp !=2:
		print("1)Cuadrado 2)tRIANGULO")
		figura=int(input("ELIJA UNA figura"))
		if figura==1:
			res=int(input("1)base 2)imprimir"))
			if res==1:
				num=int(input("Ingrese la base"))
				
			else:
				mi_cuadrado_1 = Cuadrado(num)
				print("Area:", mi_cuadrado_1.calcular_area())
				print(mi_cuadrado_1.imprimir())



			print("1)elejir una figura")
			print("2)salir")
			resp=int(input("elija una opcion"))

				

		if figura==2:
			res=int(input("1)base 2)imprimir"))
			
			if res==1:
				base=int(input("Ingrese la base"))
				altura=int(input("Ingrese la altura"))
			else:
				mi_triangulo_1= Triangulo(base,altura)
				print("Area:", mi_triangulo_1.calcular_area())
				print(mi_triangulo_1.imprimir())
				
			print("1)elejir una figura")
			print("2)salir")
			resp=int(input("elija una opcion"))

				


		





