class Texto(object):
    __cadenaCifrar = ''
    __cadenaClave = ''
    __cadenaVygenere = ''

    def __init__(self):
        self.__cadenaCifrar = ''
        self.__cadenaClave = ''
        self.__cadenaVygenere = ''

    def getCadenaCifrar(self):
        return self.__cadenaCifrar

    def getCadenaClave(self):
        return self.__cadenaClave

    def getCadenaVygenere(self):
        return self.__cadenaVygenere

    def setCadenaCifrar(self, cadenaCifrar):
        self.__cadenaCifrar = cadenaCifrar

    def setCadenaClave(self, cadenaClave):
        self.__cadenaClave = cadenaClave

    def setCadenaVygenere(self, cadena):
        self.__cadenaVygenere = cadena

    def __str__(self):
        return self.__cadenaCifrar
