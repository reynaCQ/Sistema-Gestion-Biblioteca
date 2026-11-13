class Clase_Libro:
    def __init__(self, codigo, titulo, autor, año_de_publicacion, estado):
        self.__codigo = codigo
        self.__titulo = titulo
        self.__autor = autor
        self.__año_de_publicacion = año_de_publicacion
        self.__estado = estado

    @property
    def codigo(self):
        return self.__codigo

    @property
    def titulo(self):
        return self.__titulo

    @property
    def autor(self):
        return self.__autor

    @property
    def año_de_publicacion(self):
        return self.__año_de_publicacion

    @property
    def estado(self):
        return self.__estado

    def mostrar_info(self):
        print(f"Codigo: {self.__codigo} - Titulo: {self.__titulo} - Autor: {self.__autor}")
        print(f"Año de publicacion: {self.__año_de_publicacion} - Estado: {self.__estado}")

    def cambiar_estado(self, nuevo_estado):
      if nuevo_estado in ("Disponible", "Prestado"):
        self.__estado = nuevo_estado
      else:
           print("Estado no válido.")
    
    def consultar_estado(self):
        return self.__estado

    def consultar_codigo(self):
        return self.__codigo
             