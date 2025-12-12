from typing import Protocol

class LibroProtocol(Protocol):
    def prestar(self) -> str:
        """Metodo que se implementara para prestar libros"""
        ...

    def duracion_prestamo(self) -> str:
        """Mtodo que se utilizara para definir la duracion del prestamo"""
        ...


class Libro:
    def __init__(self, titulo, autor, isbn, disponible):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible
        self.__conteo = 0 # Convertir variable en privada

    def __str__(self):
        return f"Titulo: {self.titulo}, Autor: {self.autor}, ISBN: {self.isbn}, Disponible: {self.disponible}"

    def prestar(self):
        if self.disponible:
            self.disponible = False
            self.__conteo += 1
        return f"{self.titulo} Prestado correctamente"

    def devolver(self):
        self.disponible = True
        return f"{self.titulo} Devuelto correctamente"
    
    def es_popular(self):
        if self.__conteo > 5:
            return f"{self.titulo} Es un libro popular"
        return f"{self.titulo} Aun no es un libro popular"
    
    #Getter para variable conteo
    def get_conteo(self):
        return self.__conteo
    
    #Setter para variable conteo
    def set_conteo(self, conteo):
        self.__conteo = conteo
    
class LibroFisico(Libro):
    def calcular_duracion(self):
        return "7 días"
    
class LibroDigital(Libro):
    def calcular_duracion(self):
        return "14 días"