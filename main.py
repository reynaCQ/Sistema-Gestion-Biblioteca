from biblioteca import Clase_Biblioteca
from libro import Clase_Libro
from usuario import Clase_Usuario
from funciones import mostrar_menu, separador


def main():
   biblioteca = Clase_Biblioteca()

   while True:
       mostrar_menu()
       opcion = input("Seleccione una opción: ")
       separador()
       
       if opcion == "1":
          codigo = input("Código del libro: ")

          libro_existente = biblioteca.buscar_libro(codigo)

          if libro_existente is not None:
            print("Ya existe un libro registrado con ese código.")
          else:
            titulo = input("Nombre del libro: ")
            autor = input("Nombre del autor del libro: ")
            año = input("Año de publicacion: ")

            libro = Clase_Libro(codigo, titulo, autor, año, "Disponible")
            biblioteca.agregar_libro(libro)

            separador()
            
       elif opcion == "2":
            nombre = input("Ingrese su nombre: ")
            carnet = input("Ingrese su carnet: ")
            correo = input("Ingrese su correo: ")
    
            usuario = Clase_Usuario(nombre, carnet, correo)
            biblioteca.agregar_usuario(usuario)

            separador()
    
       elif opcion == "3":
            biblioteca.mostrar_libros()
            separador()
    
       elif opcion == "4":
            biblioteca.mostrar_usuarios()

            separador()
    
       elif opcion == "5":
            carnet = input("Ingrese el carnet del usuario: ")
            usuario = biblioteca.buscar_usuario(carnet)

            if usuario is None:
                print("El usuario no existe.")
            else:
             codigo = input("Ingrese el código del libro: ")
             biblioteca.realizar_prestamo(carnet, codigo)

            separador()
    
       elif opcion == "6":
            codigo = input("Ingrese el código del libro: ")
            biblioteca.devolver_libro(codigo) 

            separador()

       elif opcion == "7":
            biblioteca.mostrar_prestamos() 

            separador()
    
       elif opcion == "8":
            codigo = input("Ingrese el código del libro: ")
            libro = biblioteca.buscar_libro(codigo)
            if libro is not None:
                libro.mostrar_info()
            else:
                print("Libro no encontrado.")  

            separador()
    
       elif opcion == "9":
            carnet =input("Ingrese el carnet del usuario: ")
            usuario = biblioteca.buscar_usuario(carnet)
            if usuario is not None:
               usuario.mostrar_info()
            else:
               print("Usuario no encontrado.")

            separador()
    
       elif opcion == "10":
            codigo = input("Ingrese el código del libro que desea eliminar: ")
            biblioteca.eliminar_libro(codigo)

            separador()

       elif opcion == "11":
            print("Adios...")
            break
       else:
            print("Opción no válida, intente de nuevo.")
       
if __name__ == "__main__":
    main()