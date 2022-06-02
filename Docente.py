from Personal import Personal

class Docente(Personal):
    __carrera = ""
    __cargo = ""
    __catedra = ""
    
    def __init__(self, cuil: str, apellido: str, nombre: str, sueldoBasico: float, antiguedad: int, carrera: str, cargo: str, catedra: str, **kwargs) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, **kwargs)
        self.__carrera = carrera
        self.__cargo = cargo
        self.__catedra = catedra
    

    def getCarrera(self) -> str:
        return self.__carrera
    
    def getCargo(self) -> str:
        return self.__cargo
    
    def getCatedra(self) -> str:
        return self.__catedra
    
    def getSueldo(self) -> float:
        sueldo = super().getSueldo()
        if self.getCargo().lower() == "simple":
            sueldo += self.getSueldoBasico() * 0.1
        elif self.getCargo().lower() == "semiexclusivo":
            sueldo += self.getSueldoBasico() * 0.2
        elif self.getCargo().lower() == "exclusivo":
            sueldo += self.getSueldoBasico() * 0.5
        return sueldo
    
    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["carrera"] = self.__carrera
        d["__atributos__"]["cargo"] = self.__cargo
        d["__atributos__"]["catedra"] = self.__catedra
        return d