import re
from ..enumeraciones.MensajeEnum import MSG


# Class: ingreso.
# Clase que permite el ingreso de valores por teclado.
class Ingreso(object):

    def ingresaNumero(self, mensaje, minimo, maximo, patron):
        valor = 0
        if maximo == 0:
            rango = ", debe ser igual o mayor a {0}"
            rango = rango.format(str(minimo))
        else:
            rango = ", valores entre {0} y {1}"
            rango = rango.format(str(minimo), str(maximo))
        while True:
            print(mensaje, rango, end=": ")
            opcion = input()
            if not self.__validaExp(patron, opcion, MSG.NUMERO_INVALIDO):
                continue
            valor = int(opcion)
            if maximo == 0:
                if valor < minimo:
                    print(MSG.NUMERO_MENOR.format(str(minimo)))
                    continue
            else:
                if valor < minimo or valor > maximo:
                    print(MSG.NUMERO_FUERA_RANGO.format(
                        str(minimo), str(maximo)))
                    continue
            break
        return valor

    def __validaExp(self, patron, valor, msgError):
        if not patron:
            return True
        if not re.match(patron, valor):
            print(msgError)
            return False
        return True

    def ingresarCadena(self, campo, patron, requerido):
        msgError = MSG.CADENA_INVALIDA.format(campo)
        while True:
            print("Ingrese", campo, end=": ")
            cadena = input()
            if requerido and len(cadena) == 0:
                print(MSG.CADENA_VACIA.format(campo))
                continue
            if not self.__validaExp(patron, cadena, msgError):
                continue
            break
        return cadena

    def ingresarCaracter(self, campo, listaOpc):
        cadena = ""
        for clave, valor in listaOpc.items():
            cadena += "'{0}': {1}, ".format(clave, valor)
        while True:
            print("Ingrese {0} [{1}]".format(
                campo, cadena.rstrip(', ')), end=": ")
            opcion = input()
            if opcion.upper() not in listaOpc:
                print(MSG.VALOR_INVALIDO)
                print(cadena.rstrip(', '))
                continue
            break
        return opcion.upper()
