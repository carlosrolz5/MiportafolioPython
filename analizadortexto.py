# Hola 
## Soy Carlos

#Este es un analizador de texto que realiza acciones como contar la cantidad de letras

---
#Deja ingresar un texto y lo convierte a minuscula
texto = input("Ingresa un texto: ")

#ingresar tres letras
l1 = input("Ingresa una letra: ").lower()

l2 = input("Ingresa una letra: ").lower()

l3 = input("Ingresa una letra: ").lower()


#Variables que cuentan los caracteres y palabras del texto
cuenta_caracteres = 0

cuenta_palabras = 0

#Variables que cuentan la cantidad de veces que cada letra ingresada aparece en el texto

cuenta_l1 = texto.lower().count(l1)

cuenta_l2 = texto.lower().count(l2)

cuenta_l3 = texto.lower().count(l3)

#Contar cada letra y cada palabra

for letra in texto:

    cuenta_caracteres += 1
    
for palabra in texto.split():

    cuenta_palabras += 1
#Mostrar los contadores de las letras, las palabras y los caracteres
print(f"Cantidad de veces que aparece la letra {l1}: {cuenta_l1}")

print(f"Cantidad de veces que aparece la letra {l2}: {cuenta_l2}")

print(f"Cantidad de veces que aparece la letra {l3}: {cuenta_l3}")

print("Cuenta de palabras:", cuenta_palabras)

print("Cuenta de caracteres:", cuenta_caracteres)
#Mostrar la primera y ultima letra del texto en mayuscula

print("Primera letra del texto:", texto[0].upper())

print("Ultima letra del texto:", texto[-1].upper())
#Mostrar el texto en reversa, primero como una lista, y luego unido
texto2 = texto.split()[::-1]

print("Texto con las palabras invertidas:", " ".join(texto2))
#Verificar si contiene "python" el texto (se muestra "si" si lo contiene y "no" si no)
diccionario = {True: "Si", False: "No"}

contiene_python = "python" in texto.lower()

print("Python en el texto: ", diccionario[contiene_python])
