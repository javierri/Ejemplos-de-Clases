# Metodo de Clase Ascensor
# Observación: Ver en https://repl.it/CBkF/0
# Autor: Javier Rivera (UNEFA Mérida)
# Observación: Para poder correrlo y que funcione, deben implementarse los métodos vácios

class Ascensor:

	# Atributos
	encendido=False 
	puerta_cerrada=False
	cantidad_piso=10
	numero_piso=0
	capacidad=5
	nro_personas=0
	
	# Métodos
	def encender (self):
		if (self.encendido==False):
			self.encendido=True
			
	def apagar (self):
		if (self.encendido==True):
			self.encendido=False

	def abrir_puerta(self):
		if (self.encendido and self.puerta_cerrada==True):
			self.puerta_cerrada=False
			print "Abriendo puerta"

	def cerrar_puerta(self):
		if (self.encendido and self.puerta_cerrada==False):
			self.puerta_cerrada=True
			print "Cerrando puerta"

	def subir (self):
		if(self.puerta_cerrada and self.encendido):
			if (self.numero_piso < self.cantidad_piso):
				self.numero_piso = self.numero_piso+1
				print "sube", self.numero_piso
			else:
				print "No puede subir, ultimo piso"
		else:
			print "Error al subir"

	def bajar (self):
		if(self.puerta_cerrada and self.encendido):
			if (self.numero_piso > 0):
				self.numero_piso = self.numero_piso-1
				print "baja", self.numero_piso
			else:
				print "No puede bajar, ultimo piso"
		else:
			print "Error al bajar"
	
	def enviar (self, piso):
		if (piso < 0) or (piso > self.cantidad_piso):
			print "Error al enviar a piso"
			return
		
		if (self.nro_personas > self.capacidad):
			print "Exceso de personas"
			return
		
		if (self.nro_personas == 0):
			print "Envio incorrecto, el ascensor esta vacio"
			return
		
		self.cerrar_puerta()
		
		if (self.numero_piso < piso):
			for i in range (piso-self.numero_piso):
				self.subir()
				
		if (self.numero_piso > piso):
			for i in range (self.numero_piso-piso):
				self.bajar()
				
		self.abrir_puerta()
		
	def llamar(self, piso):
		pass
	
	def ingresa_persona(self, nro_personas = 1):
		pass
	
	def sale_persona(self, nro_personas = 1):
		pass
		

#PRINCIPAL

a = Ascensor()
a.encender()

# PISOS
a.ingresa_persona(1)
a.enviar (7)
a.sale_persona(1)
a.ingresa_persona(2)
a.enviar (3)
a.sale_persona(2)
