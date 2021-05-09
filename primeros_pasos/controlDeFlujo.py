# Estructura IF-ELIF-ELSE
from cmath import sqrt

num = 2

if num == 1:
    print("uno")
elif num == 2:
    print("dos")
else:
    print("Distinto de uno")

'''
Existe una estructura parecida al operador  elvis de Kotlin (  ?:  )
'''

valor = 0
print("cero") if (valor == 0) else "Distinto de cero"

#  NO EXISTE LA ESTRUCTURA SWITCH

'''
BUCLE FOR
'''
tValor = (1, 2, 3, 4, 5)
for ele in tValor:  # se muestran los elementos pares
    if ele % 2 == 0: print(str(ele) + " el elemento es par")

for ele in range(5,25):
    print("el valor es: ", ele)


'''
BUCLE WHILE
solo se puede usar una condición, ni do-while
'''

valor1 = 0
while(valor <20):
    print("Valor:",valor)
    valor+=1

print ("FIN")


valor2 = ""
while(True):
    valor2 =input("ADIOS>")
    if valor2=="adios":
        break
