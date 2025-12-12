class Usuario:
    def __init__(self, nombre, cedula):
        self.nombre = nombre
        self.cedula = cedula
        self.libros_prestados = []

    def solicitar_libro(self, titulo):
        return f"Solicitud de libro '{titulo}' realizada"
    
    def devolver_libro(self, titulo):
        if titulo in self.libros_prestados:
            self.libros_prestados.remove(titulo)
            return f"Devolucion del libro {titulo} realizada correctamente"
        else: 
            return f"El libro '{titulo}' no se encuentra en tu lista de libros prestados"

class Estudiante(Usuario):
    def __init__(self, nombre, cedula, carrera):
        super().__init__(nombre, cedula)
        self.carrera = carrera
        self.limite_libros = 3

    def solicitar_libro(self, titulo):
        if len(self.libros_prestados) < self.limite_libros:
            self.libros_prestados.append(titulo)
            return f"Prestamo del libro: {titulo} autorizado"
        else:
            return f"No puedes prestar mas libros, Limite alcanzado: {self.limite_libros}"
        
class Profesor(Usuario):
    def __init__(self, nombre, cedula):
        super().__init__(nombre, cedula)
        self.limite_libros = None

    def solicitar_libro(self, titulo):
        self.libros_prestados.append(titulo)
        return f"Prestamo del libro: {titulo} autorizado"
    

estudiante = Estudiante("Luis", "1234546", "Sistemas")
profesor = Profesor("Jorge", "1234547")

print(profesor.solicitar_libro("Python Basico"))
print(profesor.solicitar_libro("Python Intermedio"))
print(profesor.solicitar_libro("Python Avanzado"))
print(profesor.solicitar_libro("Python Django"))
print(profesor.solicitar_libro("Python FastApi"))
print(profesor.devolver_libro("Python Basico"))