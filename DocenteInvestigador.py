from Docente import Docente
from Investigador import Investigador

class DocenteInvestigador(Docente, Investigador):
    __categoriaIncentivos = ""
    __importeExtra = 0

    def __init__(self, cuil: str, apellido: str, nombre: str, sueldoBasico: float, antiguedad: int, carrera: str, cargo: str, catedra: str, areaInvestigacion: str, tipoInvestigacion: str, categoriaIncentivos: str, importeExtra: float,**kwargs) -> None:
        super().__init__(cuil=cuil, apellido=apellido, nombre=nombre, sueldoBasico=sueldoBasico, antiguedad=antiguedad, carrera=carrera, cargo=cargo, catedra=catedra, areaInvestigacion=areaInvestigacion, tipoInvestigacion=tipoInvestigacion, **kwargs)
        self.__categoriaIncentivos = categoriaIncentivos
        self.__importeExtra = importeExtra
    

    def getCategoriaIncentivos(self) -> str:
        return self.__categoriaIncentivos
    
    def getImporteExtra(self) -> float:
        return self.__importeExtra
    
    def getSueldo(self) -> float:
        sueldo = Docente.getSueldo(self)
        sueldo += self.getImporteExtra()
        return sueldo
    

    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["categoriaIncentivos"] = self.getCategoriaIncentivos()
        d["__atributos__"]["importeExtra"] = self.getImporteExtra()
        return d
    

    def __str__(self):
        cadena = super().__str__()
        cadena += "Categoria de incentivos: {0}\n".format(self.__categoriaIncentivos)
        cadena += "Importe extra: {0:.2f}\n".format(self.__importeExtra)
        return cadena 