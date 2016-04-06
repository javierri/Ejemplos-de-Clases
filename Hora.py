# Clase Hora
# Observación: Ver en http://www.codeskulptor.org/#user41_uZ4edE60x04OkXF.py
# Autor: Javier Rivera (UNEFA Mérida)

class Hora:
    
    def __init__ (self, hora=12, minutos=0, militar=False, turno="AM"):
        self.__hora_militar = militar
        self.__turno = turno # AM o PM
        self.asigna_hora (hora)
        self.asigna_min (minutos)
        
    def asigna_hora (self, h, turno="AM"):
        
        if (0 <= h < 24 and self.__hora_militar):
            self.__hora = h
            return 
        
        if (1 <= h <= 12 and not(self.__hora_militar)):
            self.__hora = h
            self.__turno = turno
            return 
            
        print "Error en asignacion de hora"
        
    def asigna_min (self, m):
        if (0 <= m < 60):
            self.__min = m
        else:
            print "Error en asignacion de minutos"
            
    def suma_min (self, m):
        mint = self.__min + m
        self.__min = mint % 60
        horas = mint / 60
        
        if (not self.__hora_militar and self.__turno == "PM"):
            self.__hora = self.__hora + 12
            
        self.__hora = (self.__hora + horas) % 24
        
        if (not self.__hora_militar):
            if (self.__hora > 12):
                self.__hora = self.__hora - 12
                self.__turno = "PM"
            else:
                if (self.__hora == 0):
                    self.__hora = 12
                self.__turno = "AM"
        
    def mostrar (self):
        print self.__hora, ":", self.__min,
        if (not self.__hora_militar):
            print self.__turno,
        print
        
#PRINCIPAL

h = Hora(militar = True)
h.asigna_hora(23)
h.asigna_min(55)
h.mostrar()
h.suma_min(10)
h.mostrar()

h1 = Hora(12,58)
h1.mostrar()
h1.suma_min(10)
h1.mostrar()
