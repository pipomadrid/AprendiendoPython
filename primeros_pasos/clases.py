class Aula:
    def __init__(self, tipo):  # Constructor de la clase
        self.tipo = tipo

    def getTipo(self):  # Getter
        return self.tipo

    def setTipo(self, tipo):  # Setter
        self.tipo = tipo


x = Aula("grande")  # isntanciamos la clase con el parámetro requerido

print(x.getTipo())  # Imprimimos usando el getter

x.setTipo("mediana")  # usamos el setter para cambiar el parámetro

print(x.getTipo())  # imprimimos el nuevo valor
