#Funciones

#Crear una rutina que mediante una funcion nos indique 
#cual es el numero mayor

def comparar(n1, n2):
    if n1 < n2:
        print (n2)
    elif n2 < n1:
        print (n1)
    else:
        print ("Son iguales")
comparar(30, 8)

def comparar_3(num1, num2, num3):
    if num1>num2 and num1>num3:
        print(num1)
    elif num2>num1 and num2>num3:
        print(num2)
    elif num3>num1 and num3>num2:
        print(num3)
    else:
        print("Son iguales")
        
comparar_3(2, 2, 2)

#Funcion que calcule la longitud o la cantidad de una lista o cadena.

def largo(lista):
    cont = 0
    for i in lista:
        cont += 1
    return cont

print(largo("Hola"))
print(largo([1,2,3,4,5]))


#Función que nos indique True si encuentra una vocal

def vocales(x):
    if x == "a" or x == "e" or x == "i" or x == "o" or x == "u":
        return True
    elif x == "A" or x == "E" or x == "I" or x == "O" or x == "U":
        return True
    else:
        return False
    
print(vocales("p"))