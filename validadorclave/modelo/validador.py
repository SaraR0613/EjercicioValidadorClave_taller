# TODO: Implementa el código del ejercicio aquí

from abc import ABC, abstractmethod
from validadorclave.modelo.errores import NoCumpleLongitudMinimaError


class ReglaValidacion(ABC):

    @abstractmethod

    def es_valida(self):
        ...

    def __init__(self, longitud_esperada: int, ) :
        self.longitud_esperada: int = longitud_esperada


    def _validar_longitud(self, clave: str):
        self.longitud_esperada: int

        if not self.longitud_esperada >= 8:
            raise NoCumpleLongitudMinimaError(" La clave debe tener una longitud de más de 8 caracteres")

    def _contiene_mayuscula(self, clave: str) -> bool:
        self.letra_mayuscula: str
        self.clave: str = clave

        return any(self.letra_mayuscula.isupper() for self.letra_mayuscula in self.clave)


    def _contiene_minuscula(self, clave: str) -> bool:
        self.clave: str = clave
        self.letra_miniscula: str

        return any(self.letra_miniscula.islower() for self.letra_miniscula in self.clave)

    def _contiene_numero(self, clave: str) -> bool:
        self. clave: str = clave
        self.numero: int

        return any(self.numero.isdigit() for self.numero in self.clave)


class Validador(ReglaValidacion):

    def __init__(self, regla: ReglaValidacion, longitud_esperada: int):
        super().__init__(longitud_esperada)
        self.regla: ReglaValidacion = regla

    def es_valida(self, clave: str) -> bool:
        ...


class ReglaValidacionGanimedes (ReglaValidacion):

    def contiene_caracter_especial(self):
        pass

class ReglaValidacionCalisto
