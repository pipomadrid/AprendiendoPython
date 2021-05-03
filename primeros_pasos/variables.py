'''
Created on 3 may. 2021

@author: pedro
'''
from cmath import sqrt

'''

Lenguaje interpretado, multiplataforma
Convierte su codigo en objeto cuando se ejcuta por primera vez

'''
''' hay opción de no declarar variables, pero si hay que darles valor
 antes de usarlas
 Tiene tipado dinámico'''

nombre = "pedro"  # String
nombre = 1  # int
print(nombre)  # 1

'''Es orientado a objetos
No hay mecanismos para hacer bloques, se van creando con la
inplemtanción del código.
Los bloques como el for , if ... llevan : y se utiliza la indentación o sangrado para 
definir el bloque.
Existen varias implementaciones , Cpython --c,Jpython --Java, IronPyhton -c#
'''
if (nombre == 1):
    print("bloque if")
else:
    print("bloque else")

'''
todos los elementos para Python son objetos
Los números cuentan con un conjunto de funciones con funciones avanzadas
como sqrt o log10
'''

numero = sqrt(16)
print(numero)

'''
Los booleanos (valor true o false)
Operandos :  and,or,not,==,!=,>,>=,<,<=
'''
num = 12
num2 = 7
if (num == num2):
    print("iguales")
elif (num < num2):
    print("num2 es mayor")
else:
    print("num es mayor")

'''
Cadena
se pueden representar mediante comillas simples o dobles, pero no combinádolas
 se ussa \ para representar valores especiales.
 Tb son objetos e incporporan funciones útiles

'''

print("hola \nque tal \tyo bien, \ry tu?")
fraseminuscula = "que guay es mi primo juan , que juega al ajedrez"
frasemayuscula = fraseminuscula.capitalize()
print(frasemayuscula)  # Que guay
print(fraseminuscula.count("que"))  # 2
print(fraseminuscula.find("es"))  # 9  devuelve la posicion donde encuentra el string por 1ª vez
print(fraseminuscula.split(" "))  # separa los caracteres según el espacio
print(fraseminuscula.split(","))  # separa los caracteres según la coma
fraseConEspacio = "                     Hola que tal"
print(fraseConEspacio)
print(fraseConEspacio.strip())  # elimina el espacio en blanco antes y despues
print(fraseminuscula.upper())  # pone todas las letras en mayúscula
print(len(fraseminuscula))

'''
Existen variables globales y locales
las globales tienen un valor a lo largode todo el programa
la locales solo se pueden usar dentro del bloque en el que se inicializen
'''


def sumar():
    numeroSuma = 4  # estas variables son locales y solo las podemos usar dentro del bloque de la funcion sumar
    numeroSuma2 = 5
    print(numeroSuma + numeroSuma2)


sumar()  # 9

numeroSuma = 10  # no usa la variable de  dentro de la función, crea una variable nueva
print(numeroSuma)  # 10
sumar()  # 9

numeroResta = 10  # estas variables serian globales y las podemos usar dentro de la funcion restar
numeroResta2 = 5


def restar():
    print(numeroResta - numeroResta2)


restar()  # 5

# Como apunte , la funcion print  si separamos los valores con una "," se imprime un espacio entre ellos
print("hola soy un el numero", numeroResta2)
print("hola soy un el numero" + " cinco")  # con + hay que añadir los espacios
print("hola soy el numero", str(numeroResta2))  # para poder usar + hay que convertir a string
