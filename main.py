from biblioteca import Biblioteca
from libros import LibroFisico
from usuarios import Estudiante, Profesor, SolicitanteProtocol

biblioteca = Biblioteca("Biblioteca Patzi")

estudiante = Estudiante("Luis", "1234546", "Sistemas")
estudiante_1 = Estudiante("Felipe", "1234548", "Salud")
profesor = Profesor("Jorge", "1234547")
usuarios: list[SolicitanteProtocol] = [estudiante, estudiante_1, profesor]


mi_libro = LibroFisico("100 años de Soledad", "Gabril Garcia Marquez", "1298374", True)
mi_libro_no_disponible = LibroFisico("100 años de Soledad", "Gabril Garcia Marquez", "1298374", False)
otro_libro = LibroFisico("El principito", "Saint-Exupéry", "987374", True)

biblioteca.libros = [mi_libro, mi_libro_no_disponible, otro_libro]
print(biblioteca.libros)
print(biblioteca.libros_disponibles())