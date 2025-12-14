class BibliotecaError(Exception):
    pass


class TituloInvalidoError(BibliotecaError):
    pass


class LibroNoDisponibleError(BibliotecaError):
    pass


class LimitePrestamosError(BibliotecaError):
    pass


class UsuarioNoEncontradoError(BibliotecaError):
    pass
