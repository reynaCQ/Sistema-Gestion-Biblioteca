from prestamo import Clase_Prestamo

class Clase_Biblioteca:
    def __init__(self):
        self.__libros = []
        self.__usuarios = []
        self.__prestamos = []

    ##LIBROS

    def mostrar_libros(self):
        if len(self.__libros) == 0:
           print("No hay libros registrados.")
           return
        
        for libro in self.__libros:
            libro.mostrar_info()
            print()

    def buscar_libro(self, codigo):
        for l in self.__libros:
            if l.codigo == codigo:
                return l
        return None

    def agregar_libro(self, libro):
        ##comprobar si el libro ya existe
        for l in self.__libros:
            if l.codigo == libro.codigo:
                print(f"El libro {libro.titulo} ya fue registrado.")
                return
        self.__libros.append(libro)
        print(f"Libro {libro.titulo} agregado a la biblioteca.")

    def eliminar_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro is None:
           print("El libro no existe.")
           return
        if libro.estado == "Prestado":
           print("Error: El libro está prestado.")
           return
        self.__libros.remove(libro)
        print(f"Libro {libro.titulo} se eliminó de la biblioteca.")

##USUARIOS

    def agregar_usuario(self, usuario): 
        if self.buscar_usuario(usuario.carnet) is not None:
            print("Ya está registrado.")
            return
        self.__usuarios.append(usuario)
        print("Usuario agregado.")

##Comprobar si el usuario existe
    def buscar_usuario(self, carnet):
        for u in self.__usuarios:
           if u.carnet == carnet:
                return u
        return None

    def mostrar_usuarios(self):
        if len(self.__usuarios) == 0:
           print("No hay usuarios registrados.")
           return
        for usuario in self.__usuarios:
            usuario.mostrar_info()

##PRESTAMOS

    def realizar_prestamo(self, carnet, codigo ): 
        usuario = self.buscar_usuario(carnet)
        if usuario is None:
            print("El usuario no existe.")
            return

        libro = self.buscar_libro(codigo)
        if libro is None:
            print("El libro no existe.")
            return

        if libro.estado != "Disponible":
            print("El libro no está disponible.")
            return

        nuevo = Clase_Prestamo(usuario, libro)
        self.__prestamos.append(nuevo)
        usuario.agregar_prestamos(nuevo)
        libro.cambiar_estado("Prestado")
        print("Préstamo realizado.")
        return True
        

    def devolver_libro(self, codigo):
        libro = self.buscar_libro(codigo)
        if libro is None:
            print("El libro no existe.")
            return
        if libro.estado != "Prestado":
            print("Ese libro no está prestado.")
            return

        for p in self.__prestamos:
            if p.libro.codigo == codigo:
               self.__prestamos.remove(p)
               p.usuario.quitar_prestamos(p)
               libro.cambiar_estado("Disponible")
               print("Libro devuelto.")
               return True

        print("No se encontró el préstamo correspondiente.")
        return

    
    def mostrar_prestamos(self):
        if len(self.__prestamos) == 0:
            print("No hay préstamos registrados.")
            return
        for prestamo in self.__prestamos:
            prestamo.info_prestamo()