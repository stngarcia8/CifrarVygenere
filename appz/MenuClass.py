from .utils.UtilClass import Util
from .clases.TextoClass import Texto


class Menu(object):

    util = Util()
    texto = Texto()

    def __opciones(self):
        self.util.mostrarTitulo('opciones de cifrado')
        print("1. Ingresar valores.")
        print('2. Cifrar por metodo de Vygenere.')
        print('3. Descifrar por metodo de Vygenere.')
        print("0. Salir")
        print()
        return

    def mostrarMenu(self):
        opcion = 1
        while opcion:
            self.__opciones()
            opcion = self.util.leerNumero("Ingrese su opción", 0, 3)
            if opcion == 1:
                self.util.ingresarValores(self.texto)
            if opcion == 2:
                self.util.cifrarVygenere(self.texto)
            if opcion == 3:
                self.util.descifrarVygenere(self.texto)
            if opcion == 0:
                print("Eso fue todo, chao!")
                break
        return
