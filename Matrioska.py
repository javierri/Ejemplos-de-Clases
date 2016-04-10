# UNEFA Merida
# Autor: Javier Rivera

class Matrioska:
	
	def __init__(self, tam):
		self.__adentro = False
		self.__tam = tam
		self.__matrioska = None
		
	def cambia_tam(self, tam):
		self.__tam = tam
		
	def cons_tam(self):
		return self.__tam
		
	def meter (self, matrioska):
		if (self.__adentro == True):
			print "La matrioska esta adentro, no puede meterle una matrioska"
			return
		
		if (self.__matrioska != None):
			print "La matrioska esta llena, no puede meterle una matrioska"
			return
			
		if (matrioska.cons_tam() < self.__tam):
			matrioska.__adentro = True
			self.__matrioska = matrioska;
		else:
			print "No puede meterle una matrioska mas grande"
			
	def sacar (self):
		if (self.__adentro == True):
			print "La matrioska esta adentro, no puede sacarle una matrioska"
			return
		
		if (self.__matrioska == None):
			print "La matrioska esta vacia, no puede sacarle una matrioska"
			return None
			
		objeto_aux = self.__matrioska
		objeto_aux.__adentro = False
		self.__matrioska = None
		
		print "Sacando matrioska ",objeto_aux.cons_tam() 
		return objeto_aux
		
	def __ver (self):
		print self.__tam, 
		if (self.__matrioska != None):
			self.__matrioska.__ver()
	
	def mostrar(self):
		if (self.__adentro == True):
			print "La matrioska esta adentro, no puede mostrarla"
			return
			
		self.__ver()
		print
			
#PRINCIPAL
 
muygrande = Matrioska(4) 
grande = Matrioska(3)
mediano = Matrioska(2)
chico = Matrioska(1)

chico.meter(mediano)
mediano.meter(chico)
grande.meter(mediano)
grande.meter(chico)
muygrande.meter(grande)

muygrande.mostrar()
grande.mostrar()

grande.sacar()
muygrande.sacar()

muygrande.mostrar()
grande.mostrar()

grande.sacar()
grande.sacar()

chico.sacar()


