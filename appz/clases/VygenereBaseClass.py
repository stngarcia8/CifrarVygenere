import abc
from abc import ABCMeta


class VygenereBase(object):
    __metaclass__ = ABCMeta

    # Atributos de la clase.
    texto = ''
    clave = ''
    caracteres = 'abcdefghijklmnñopqrstuvwxyz ABCDEFGHIJKLMNÑOPQRSTUVWXYZ0123456789@#$%&.,;:-+*/'
    textoResultado = []

    # Variables para mostrar el estado de los calculos.
    cadTexto = []
    cadClave = []
    cadOperacion = []
    cadModulo = []

    def __init__(self, texto, clave):
        self.texto = texto
        self.clave = clave
        self.textoResultado = []

    @abc.abstractmethod
    def getTextoResultado(self):
        return ''.join(self.textoResultado)

    @abc.abstractmethod
    def ajustarCadenas(self):
        if len(self.texto) < len(self.clave):
            self.__normalizaLargoMensajeConClave()
        if len(self.texto) > len(self.clave):
            self.__normalizaLargoClaveConMensaje()
        return

    def __normalizaLargoMensajeConClave(self):
        self.clave = self.clave[:len(self.texto)]

    def __normalizaLargoClaveConMensaje(self):
        ciclos = int(len(self.texto) / len(self.clave)) + 1
        aux = self.clave * ciclos
        self.clave = aux[:len(self.texto)]

    @abc.abstractmethod
    def calcularCadenas(self):
        pass

    @abc.abstractmethod
    def buscarCaracter(self, caracter, cadenaMuestra):
        valor = self.caracteres.find(caracter)
        return valor

    @abc.abstractmethod
    def mostrarEstado(self, estado, texto, clave):
        print(estado)
        print('Texto: ', texto)
        print('Clave: ', clave)

    @abc.abstractmethod
    def mostrarCalculos(self, esCifrado=True):
        print()
        print('Calculando...')
        print('Texto: ', ''.join(self.cadTexto))
        print('Clave: ', ''.join(self.cadClave))
        print('Suma:  ' if esCifrado else 'Resta: ', ''.join(self.cadOperacion))
        print('Modulo:', ''.join(self.cadModulo))

    @abc.abstractmethod
    def formatearMuestra(self, valTexto, valClave, valOperacion, valModulo):
        self.cadTexto.append(self.__concatenar(valTexto))
        self.cadClave.append(self.__concatenar(valClave))
        self.cadOperacion.append(self.__concatenar(valOperacion))
        self.cadModulo.append(self.__concatenar(valModulo))

    def __concatenar(self, valor):
        return (' ' if valor < 10 else '') + str(valor) + ' '
