from .VygenereBaseClass import VygenereBase


class VygenereCifrado(VygenereBase):

    def __init__(self, texto, clave):
        VygenereBase.__init__(self, texto, clave)

    def cifrar(self):
        self.ajustarCadenas()
        self.mostrarEstado('Ajustando  cadenas.', self.texto, self.clave)
        self.calcularCadenas()
        self.mostrarCalculos()

    def calcularCadenas(self):
        operacion = 0
        for i in range(len(self.texto)):
            a = self.buscarCaracter(self.texto[i], self.cadTexto)
            b = self.buscarCaracter(self.clave[i], self.cadClave)
            operacion = (a + b)
            modulo = operacion % len(self.caracteres)
            self.textoResultado.append(self.caracteres[modulo])
            self.formatearMuestra(a, b, operacion, modulo)
        return

    def __str__(self):
        return ''.join(self.textoResultado)
