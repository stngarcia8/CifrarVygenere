import os
from .IngresoClass import Ingreso
from ..clases.VygenereCifradoClass import VygenereCifrado
from ..clases.VygenereDescifradoClass import VygenereDescifrado


class Util(object):

    def cls(self):
        if os.name in ("ce", "nt", "dos"):
            os.system("cls")
        else:
            os.system("clear")
        return

    def mostrarTitulo(self, titulo):
        self.cls()
        if not titulo:
            return
        print("{0:^80}".format(titulo.upper()))
        print("{0:^80}".format("-".rjust(len(titulo), '-')))
        print()
        return

    def presionarEnter(self, mensaje=""):
        print()
        if len(mensaje) > 0:
            print(mensaje)
        print("Presione <ENTER> para continuar...", end="")
        input()
        return

    def leerNumero(self, campo, minVal, maxVal):
        miIngreso = Ingreso()
        return miIngreso.ingresaNumero(campo, minVal, maxVal, "^[0-9]{1,}$")

    def ingresarValores(self, texto):
        self.mostrarTitulo('Ingresar valores')
        self.__ingresarCadenas(texto)
        self.presionarEnter('Valores ingresados.')
        return

    def __mostrarCabecera(self, texto, titulo, mostrarClave):
        self.mostrarTitulo(titulo)
        print('Valores iniciales')
        print('Texto: ', texto.getCadenaCifrar())
        if mostrarClave:
            print('Clave: ', texto.getCadenaClave())
        print()
        return

    def __ingresarCadenas(self, texto):
        miIngreso = Ingreso()
        texto.setCadenaCifrar(
            miIngreso.ingresarCadena('texto a cifrar', '', True))
        texto.setCadenaClave(
            miIngreso.ingresarCadena('clave', '', True))
        texto.setCadenaVygenere('')
        return

    def cifrarVygenere(self, texto):
        self.__mostrarCabecera(texto, 'Cifrar con metodo Vygenere', True)
        if len(texto.getCadenaClave()) == 0:
            self.presionarEnter('No hay valores ingresados para cifrar.')
            return
        myVygenere = VygenereCifrado(texto.getCadenaCifrar(),
                                     texto.getCadenaClave())
        myVygenere.cifrar()
        texto.setCadenaVygenere(myVygenere.getTextoResultado())
        print()
        print('Texto cifrado: ', myVygenere)
        self.presionarEnter()
        return

    def descifrarVygenere(self, texto):
        self.__mostrarCabecera(texto, 'Descifrar con metodo Vygenere', False)
        if len(texto.getCadenaVygenere()) == 0:
            self.presionarEnter(
                'Debe cifrar un texto antes de usar el descifrado.')
            return
        print('Texto cifrado: ', texto.getCadenaVygenere())
        miIngreso = Ingreso()
        myClave = miIngreso.ingresarCadena('clave', '', True)
        myVygenere = VygenereDescifrado(texto.getCadenaVygenere(), myClave)
        myVygenere.descifrar()
        print()
        print('Texto descifrado: ', myVygenere)
        self.presionarEnter()
        return
