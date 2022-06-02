from Personal import Personal

class PersonalApoyo(Personal):
    __categoria = ""

    def __init__(self, cuil: str, apellido: str, nombre: str, sueldoBasico: float, antiguedad: int, categoria: int) -> None:
        super().__init__(cuil, apellido, nombre, sueldoBasico, antiguedad)
        self.__categoria = categoria
    
    def getCategoria(self) -> int:
        return self.__categoria
    
    def getSueldo(self) -> float:
        sueldo = super().getSueldo()
        if 1 <= self.getCategoria() <= 10:
            sueldo += self.getSueldoBasico() * 0.1
        elif 11 <= self.getCategoria() <= 20:
            sueldo += self.getSueldoBasico() * 0.2
        elif 21 <= self.getCategoria() <= 22:
            sueldo += self.getSueldoBasico() * 0.3
        return sueldo
    

    def toJSON(self):
        d = super().toJSON()
        d["__atributos__"]["antiguedad"] = self.__antiguedad
        d["__atributos__"]["categoria"] = self.__categoria
        return d