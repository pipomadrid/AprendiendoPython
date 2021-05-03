'''
Listas
Son modificables, puede haber duplicados
'''

# lista 1
realMadrid = ["Sergio Ramos", "Marcelo", "Isco", "Rodrigo", "kroos"]
# lista2
realMadridB = ["Antonio Blanco", "Miguel Gutierrez", "Arribas"]

print(realMadrid)
print(realMadrid[3])  # rodrigo
realMadrid.pop(1)  # eliminamos Marcelo
print(realMadrid)
realMadrid.append("Vinicius")  # Añadimos  un elemento
print(realMadrid)
realMadrid.insert(1, "Modric")  # Insertamos Modric en pos 1
print(realMadrid)
realMadrid.extend(realMadridB)  # extendemos la lista 1 con la lista 2
print(realMadrid)
realMadrid.remove("Isco")  # Eliminamos la primera vez que aparece el elemento
print(realMadrid)
print(realMadrid[-1])  # en python lso indices pueden ser negativos, -1 corresponde al ultimo elemento
print(realMadrid[-2])
print(realMadrid.index('Rodrigo'))  # para saber que indice ocupa
print(realMadrid[0:3])  # recorremos la lista hasta el elemento 3 no incluido
'''
Diccionarios
estructuras clave - valor
'''

alineacion = {'Sergio Ramos': 'defensa', 'Modric': 'centrocampista', 'Rodrigo': 'delantero'}
print(alineacion.get('Sergio Ramos'))  # obtenemos el valor correspondiente a la clave introducida
print(alineacion.pop(
    'Modric'))  # Devuelve el valor que corresponde con la key introducida, y luego borra la key y el valor.
print(alineacion)
alineacion.update({'kroos': 'centrocampista'})  # inserta clave-valor o actualiza el valor si ya existe
print(alineacion)
print("kroos" in alineacion)  # Devuelve booleano
print("delantero" in alineacion.values())  # Devuelve booleano si el valor existe en el diccionario
alineacion['Cortois'] = 'portero'  # añadimos un elemento con la clave pasada
print(alineacion)

'''
Tuplas
No se pueden modificar
Son mas ligeras y eficientes
'''

miTupla = (2, 5, 7, 8)
print(miTupla[1])
# miTupla[1] = 2   # No se puede realizar, lanza excepcion ya que la stuplas son inmutables
print(miTupla.index(7))  # devuelve la posicion del 7
