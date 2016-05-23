
from Animal import *

class Gato(Animal):
	def __init__(self, raza = None, color = None, sexo = 'M', peso = 0):
		Animal.__init__(self,raza,color,sexo,peso)
		self.tipo_especie("Gato",9,5)
		self.asigna_sonido("Miau Miau")
		
		
class Perro(Animal):
	def __init__(self, raza = None, color = None, sexo = 'M', peso = 0):
		Animal.__init__(self,raza,color,sexo,peso)
		self.tipo_especie("Perro",9,10)
		self.asigna_sonido("Guau Guau")
		
        
# PRINCIPAL
# Con gatos ..

marie = Gato ("Angora","marron","F")
peter = Gato ("Bengala","gris","M")

print marie
print peter

peter.cita(marie)
print "Marie Embarazada: ", marie.embarazada()

for i in range(9):
	marie.cumple_sem_gestacion()
	
gaticos = marie.parir()

print "Muestra hijos ..."
for gatico in gaticos:
	print gatico

print "Marie Embarazada: ", marie.embarazada()

### Con perros

doki = Perro("Pastor","Marron","M")
susi = Perro("Negro","Marron","F")

print doki
print susi

susi.cita(peter)
print "Susi Embarazada: ", susi.embarazada()

susi.cita(doki)
print "Susi Embarazada: ", susi.embarazada()

for i in range(9):
	susi.cumple_sem_gestacion()
	
perritos = susi.parir()

print "Muestra hijos ..."
for perrito in perritos:
	print perrito
