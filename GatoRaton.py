from Animal import *

class Raton(Animal):
	def __init__(self, raza = None, color = None, sexo = 'M', peso = 0):
		Animal.__init__(self,raza,color,sexo,peso)
		self.tipo_especie("Raton",3,12)
		

class Gato(Animal):
	def __init__(self, raza = None, color = None, sexo = 'M', peso = 0):
		Animal.__init__(self,raza,color,sexo,peso)
		self.tipo_especie("Gato",9,5)
		self.asigna_sonido("Miau Miau")
		
	def cazar(self, raton):
		if (raton.especie() == "Raton"):
			self.comer(raton.peso())
			raton.morir()
		else:
			print "Gaucatela"
		
		
        
# PRINCIPAL
# Con gatos ..

marie = Gato ("Angora","marron","F")
Miki = Raton ("Comun","gris","M",0.5)

print marie
print Miki

marie.cazar(Miki)

print marie
print Miki
