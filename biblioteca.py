from exceptions import UsuarioNoEncontradoError
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []
        self.usuarios = []

    def libros_disponibles(self):
        return [libro.titulo for libro in self.libros if libro.disponible]
    
    def buscar_usuario(self, cedula):
        for usuario in self.usuarios:
            if usuario.cedula == cedula:
                return usuario
        raise UsuarioNoEncontradoError(f"El usuario con la cedula {cedula} no fue encontrado")

