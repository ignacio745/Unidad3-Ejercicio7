from Personal import Personal

class Investigador(Personal):
    __areaInvestigacion = ""
    __tipoInvestigacion = ""

    def __init__(self, cuil: str, apellido: str, nombre: str, sueldoBasico: float, antiguedad: int, areaInvestigacion: str, tipoInvestigacion: str, **kwargs) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad, **kwargs)
        self.__areaInvestigacion = areaInvestigacion
        self.__tipoInvestigacion = tipoInvestigacion
    

    def getAreaInvestigacion(self) -> str:
        return self.__areaInvestigacion
    
    def getTipoInvestigacion(self) -> str:
        return self.__tipoInvestigacion
    
    def getSueldo(self) -> float:
        return super().getSueldo()
    
    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["areaInvestigacion"] = self.__areaInvestigacion
        d["__atributos__"]["tipoInvestigacion"] = self.__tipoInvestigacion
        return d
    

    def __str__(self):
        cadena = super().__str__()
        cadena += "Area de investigacion: {0}\n".format(self.getAreaInvestigacion())
        cadena += "Tipo de investigacion: {0}\n".format(self.getTipoInvestigacion())
        return cadena
    

    def getTipo(self) -> str:
        return "Investigador"