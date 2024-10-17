# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoCumpleLongitudMinimaError, NoTieneLetraMayusculaError, \
    NoTieneLetraMinusculaError, NoTieneNumeroError


class ReglaValidacion(ABC):

    @abstractmethod

    def es_valida(self, clave: str) -> bool:
        ...

    def __init__(self, longitud_esperada: int, ) :
        self.longitud_esperada: int = longitud_esperada


    def _validar_longitud(self, clave: str):
        self.longitud_esperada: int

        if not self.longitud_esperada >= 8:
            raise NoCumpleLongitudMinimaError(" La clave debe tener una longitud de más de 8 caracteres")


    def _contiene_mayuscula(self, clave: str) -> bool:
        self.clave: str = clave

        if not clave.isupper():
            raise NoTieneLetraMayusculaError

        return True


    def _contiene_minuscula(self, clave: str) -> bool:
        self.clave: str = clave
        self.letra_miniscula: str

        if not clave.islower():
            raise NoTieneLetraMinusculaError

        return True

    def _contiene_numero(self, clave: str) -> bool:
        self. clave: str = clave
        self.numero: int

        if not clave.isdigit():
            raise NoTieneNumeroError

        return True






