from figura import Figurageometrica

class Cuadrado(Figurageometrica):

	def __init__(self,lado):
		super(). __init__(lado,lado)


	def imprimir(self):
		resultado = ""

		for i in range (self.altura):
			resultado += "* " *(self.base) + "\n"

		return resultado