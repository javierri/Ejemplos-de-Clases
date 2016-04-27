class Gato:
    def __init__ (self, raza = None, color = None, sexo = 'M', peso = 0):
        self.__edad = 0
        self.__color = color 
        self.__raza = raza
        self.__vivo = True
        self.__sexo = sexo
        if (peso > 0 and peso < 0.5):
            self.__peso = peso
        else:
            self.__peso = 0.1
            
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
            
    def __str__(self):
        cad = self.__raza + ', ' + self.__color + ', ' + str(self.__sexo) + ', ' + str(self.__peso) 
        return cad
        
# PRINCIPAL

marie = Gato ("Angora","marron","F")
peter = Gato ("Bengala","gris","M")

print marie
print peter
