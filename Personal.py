from abc import ABC
import abc

class Personal(ABC):
    __cuil = ""
    __apellido = ""
    __nombre = ""
    __sueldoBasico = 0
    __antiguedad = 0

    def __init__(self, cuil: str, apellido: str, nombre: str, sueldoBasico: float, antiguedad: int, **kwargs) -> None:
        self.__cuil = cuil
        self.__apellido = apellido
        self.__nombre = nombre
        self.__sueldoBasico = sueldoBasico
        self.__antiguedad = antiguedad
    

    def getCuil(self) -> str:
        return self.__cuil
    
    def getApellido(self) -> str:
        return self.__apellido
    
    def getNombre(self) -> str:
        return self.__nombre
    
    def getSueldoBasico(self) -> float:
        return self.__sueldoBasico
    
    def getAntiguedad(self) -> int:
        return self.__antiguedad
    
    @abc.abstractmethod
    def getSueldo(self) -> float:
        sueldo = self.getSueldoBasico() + self.getSueldoBasico() * 0.01 * self.getAntiguedad()
        return sueldo
    
    @abc.abstractmethod
    def toJSON(self):
        d = dict(
            __class__ = self.__class__.__name__,
            __atributos__ = dict(
                cuil = self.__cuil,
                apellido = self.__apellido,
                nombre = self.__nombre,
                sueldoBasico = self.__sueldoBasico,
                antiguedad = self.__antiguedad                
            )
        )
        return d