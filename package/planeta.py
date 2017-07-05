class Planeta:
	def __init__(self,radio = 0,edad = 0,estrella = "none"):
		self.radio = radio
		self.edad = edad
		self.estrella = estrella

	def rotar(self):
		print("Los planetas rotan sobre su propio eje")

	def minus(self,palabra):
		self.palabra = lower(palabra)

	def biodiversidad(self):
		self.biodiversidad = input("¿El planeta tiene vida?\n")
		while self.biodiversidad != "si" and self.biodiversidad != "no":
			if self.biodiversidad == "si":
				break
			elif self.biodiversidad == "no":
				break
			else:
				print("Ingrese un argumento valido")
				print("Argumentos validos:\n'si'\n'no'")
			self.biodiversidad = input("¿El planeta tiene vida?\n")
		if self.biodiversidad == "si":
			self.biodiversidad = True
			print("El planeta tiene vida")
		elif self.biodiversidad == "no":
			self.biodiversidad = False


