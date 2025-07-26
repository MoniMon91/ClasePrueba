# texto_variado = "Palabra 123 + * #"
# print (type(texto_variado))

# Podemos utilizar comillas triples para que el texto se muestre como la cadena que hemos escrito
# print(""" 
# Funcionamiento de \
# programa: (opciones)
#        -1 Para acceder a opciones
#        -2 Para salir
#  """)

####################################################################################
# Subscripting e indexado

# texto = "Python"

# print (texto [0]) #Imprime la primera letra de Python
# print (texto [5])
# print (texto [-1]) #Empieza a contar a partir de la n
# print (texto [-6]) #No puede hacer impresión de un número mayor a los caracteres que tiene la palabra

# print (texto [6]) #Error! No podemos acceder a una posición que no existe
# print (texto [-7]) #Error! No podemos acceder a una posición que no existe

# letra = texto [0]
# print(letra)

# #texto [0] = "p" #error! No podemos modificar una cadena

# letra = "p"
# print (letra)

#texto_compuesto = letra + texto[1] #concatenación
#print (texto_compuesto)

######################################################################

# Slicing o Substringing
#texto = "Python"

#print(texto[0:3]) #Se imprimen los primeros 3
#print(texto[0:-3])
#print(texto[0:-2])
#print(texto[2:])
#print(texto[0:])
#print(texto[:3])

#print (texto [-3::-1])
#print (texto [::-1]) #Va de reversa, el resultado es nohtyP
#print (texto[1:50])
#print (texto[2:2])

######################################################################
#Cadenas y formatos

texto = "Hola mundo! Buenastardes"
#print(texto.lower()) #Letras minúsculas
#print(texto.upper()) #Letras mayúsculas
#print (texto.capitalize()) #solo la primera letra de la frase será Mayúscula
#print (texto.title()) #la inicial de cada palabra sea mayúscula
#print (texto.swapcase()) #intercambia las mayúsculas con las minúsculas
#texto =texto.upper() #Se reasigno el valor de la variable
#print(texto)

print ("{} + {} = {}" .format (2, 3, 2+3))
print ("{} + {} = {}" .format ("Hola", "mundo", "Hola mundo"))
print ("{:.3f} + {:.4f} = {}" .format (2, 3, 2+3))
print ("{1} + {0} = {2}" .format (2, 3, 2+3))
print ("{2} + {0} = {1}" .format ("Hola", "mundo", "Hola mundo"))
print ("{:d} = {:b} = {:o} = {:x}" .format (15, 15, 15, 15))
