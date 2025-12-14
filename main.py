from biblioteca import Biblioteca
from exceptions import UsuarioNoEncontradoError
from libros import LibroFisico
from usuarios import Estudiante, Profesor, SolicitanteProtocol

biblioteca = Biblioteca("Biblioteca Patzi")
estudiante = Estudiante("Luis", "1234546", "Sistemas")
estudiante_1 = Estudiante("Felipe", "1234548", "Salud")
profesor = Profesor("Jorge", "1234547")
mi_libro = LibroFisico("100 años de Soledad", "Gabril Garcia Marquez", "1298374")
mi_libro_no_disponible = LibroFisico("100 años de Soledad", "Gabril Garcia Marquez", "1298374", False)
otro_libro = LibroFisico("El principito", "Saint-Exupéry", "987374")

biblioteca.usuarios = [estudiante, estudiante_1, profesor]
biblioteca.libros = [mi_libro, mi_libro_no_disponible, otro_libro]

print("Bienvenido a Biblioteca Platzi")
cedula = input("Digite el numero de cedula: ")
try:
    usuario = biblioteca.buscar_usuario(cedula)
    print(usuario.cedula, usuario.nombre)
except UsuarioNoEncontradoError:
    print("Error al buscar el usuario ingresado, no se encuentra en la lista")

