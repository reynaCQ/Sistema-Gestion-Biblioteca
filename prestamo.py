class  Clase_Prestamo:
  def __init__(self, usuario, libro):
    self.__usuario = usuario
    self.__libro = libro

  @property
  def usuario(self):
    return self.__usuario

  @property
  def libro(self):
    return self.__libro

  def info_prestamo(self):
   print(f"Usuario: {self.__usuario.nombre} - Carnet: {self.__usuario.carnet}")
   print(f"Titulo: {self.__libro.titulo} - Codigo: {self.__libro.codigo}")