# Autor: Javier Rivera (UNEFA)
# 

import random

class Animal:
    def __init__ (self, raza = None, color = None, sexo = 'M', peso = 0):
        self.__edad = 0
        self.__color = color 
        self.__raza = raza
        self.__vivo = True
        self.__sexo = sexo
        
        self.__embarazada = False
        self.__sem_gestacion = 0
        self.__genes_padre = None
        
        # atributos para herencia
        self.__especie = None
        self.__total_gestacion = None
        self.__crias = None
        self.__sonido = None
        #
        
        if (peso > 0 and peso < 0.5):
            self.__peso = peso
        else:
            self.__peso = 0.1
 
 
    # Funciones para Herencia       
    def tipo_especie(self, tipo_especie, semana_gestacion, max_crias):
		self.__especie = tipo_especie
		self.__total_gestacion = semana_gestacion 
		self.__crias = max_crias
     
    def asigna_sonido(self, sonido):
		self.__sonido = sonido      
    #        
            
    def comer (self,comida=5):
        if (comida > 0 and comida < 10):
            self.__peso = self.__peso + comida / 4.0
            
    def jugar (self, tiempo=0.5):
        if (tiempo > 0 and tiempo < 1):
            self.__peso = self.__peso - tiempo / 6.0
            
    def cumpleano(self):
        if (sel.__edad < 15):
            self.__edad = self.__edad + 1
        else:
            self.__vivo = true
            
    def edad(self):
        return self.__edad
        
    def cita(self, pareja):
		
		if (self.__especie != pareja.__especie):
			return
		
		if (self.__sexo == pareja.__sexo):
			return
		
		if (self.__sexo == "F" and self.__embarazada == False):
			self.__embarazada = True
			self.__sem_gestacion = 0
			self.__genes_padre = pareja
		elif (pareja.__sexo == "F" and pareja.__embarazada == False) :
			pareja.__embarazada = True
			pareja.__sem_gestacion = 0
			pareja.__genes_padre = self
			
		print self.__sonido
		
    def embarazada(self):
		return self.__embarazada
		
    def cumple_sem_gestacion (self):
		if (self.__embarazada == True):
			self.__sem_gestacion = self.__sem_gestacion + 1
			
    def parir(self):
		genes = (self,self.__genes_padre)
		hijos = []
		
		if (self.__embarazada == True and self.__sem_gestacion >= self.__total_gestacion):
			nro_hijos = random.randint(2, self.__crias)
	
			for i in range(nro_hijos):
				# Crea hujo con genes aleatorios de los padres
				h_raza = random.randint(0, 1) # Herencia Raza
				h_color = random.randint(0, 1) # Herencia Color
				h_sexo = random.randint(0, 1) # Herencia Sexo
				hijo = Animal(genes[h_raza].__raza, genes[h_color].__color, genes[h_sexo].__sexo)
				hijos.append(hijo)
				
			self.__embarazada = False
			self.__sem_gestacion = 0
			self.__genes_padre = None

		return hijos
            
    def __str__(self):
        cad = self.__raza + ', ' + self.__color + ', ' + str(self.__sexo) + ', ' + str(self.__peso) 
        return cad
