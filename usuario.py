class Clase_Usuario:
 def __init__(self, nombre, carnet, correo):
    self.__nombre = nombre
    self.__carnet = carnet
    self.__correo = correo
    self.__prestamos = []

 @property
 def nombre (self):
    return self.__nombre

 @property
 def carnet(self):
      return self.__carnet

 @property
 def correo(self):
      return self.__correo

 def mostrar_info(self):
   print(f"Nombre: {self.__nombre} - Carnet:{self.__carnet} - Correo: {self.__correo}")

 def consultar_carnet(self):
   return self.__carnet

 def consultar_nombre(self):
   return self.__nombre

 def agregar_prestamos(self, prestamo):
   self.__prestamos.append(prestamo)

 def quitar_prestamos(self, prestamo):
    if prestamo in self.__prestamos:
       self.__prestamos.remove(prestamo)