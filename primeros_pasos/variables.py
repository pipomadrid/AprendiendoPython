'''
Created on 3 may. 2021

@author: pedro
'''
from cmath import sqrt

'''

Lenguaje interpretado, multiplataforma
Convierte su codigo en objeto cuando se ejcuta por primera vez

'''

#hy opción de no declarar variables, pero si hy que darles valor
#ntes de usarlas
#Tiene tipdo dinámico
nombre  = "pedro" #String
nombre = 1#int
print(nombre) # 1

'''Es orientado a objetos
No hay mecanismos para hacer bloques, se van creando con la
inplemtanción del código.
Los bloques como el for , if ... llevan : y se utiliza la indentación o sangrado para 
definir el bloque.
Existen varias implementaciones , Cpython --c,Jpython --Java, IronPyhton -c#
'''
if(nombre==1):
    print("bloque if")
else:
    print("bloque else")
    
'''
todos los elementos para Python son objetos
Los números cuentan con un conjunto de funciones con funciones avanzadas
como sqrt o log10
'''
    

numero =sqrt(16)
print(numero)

'''
Los booleanos (valor true o false)
Operandos :  and,or,not,==,!=,>,>=,<,<=
'''
num = 12
num2 =7
if(num == num2):
    print("iguales")
elif(num< num2):
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
frasemayuscula =  fraseminuscula.capitalize()
print(frasemayuscula) #Que guay
print(fraseminuscula.count("que")) #2
print(fraseminuscula.find("es")) # 9
print(fraseminuscula.split(" ")) #separa los caracteres según el espacio
print(fraseminuscula.split(","))# separa los caracteres según la coma 

