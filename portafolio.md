# Hola 
## Soy Carlos

Esta es una serie de algoritmos creados en Python

Espero que los disfrutes

---
texto = input("Ingresa un texto: ")

l1 = input("Ingresa una letra: ").lower()

l2 = input("Ingresa una letra: ").lower()

l3 = input("Ingresa una letra: ").lower()



cuenta_caracteres = 0

cuenta_palabras = 0

cuenta_l1 = texto.lower().count(l1)

cuenta_l2 = texto.lower().count(l2)

cuenta_l3 = texto.lower().count(l3)



for letra in texto:

    cuenta_caracteres += 1
    
for palabra in texto.split():

    cuenta_palabras += 1

print(f"Cantidad de veces que aparece la letra {l1}: {cuenta_l1}")

print(f"Cantidad de veces que aparece la letra {l2}: {cuenta_l2}")

print(f"Cantidad de veces que aparece la letra {l3}: {cuenta_l3}")

print("Cuenta de palabras:", cuenta_palabras)

print("Cuenta de caracteres:", cuenta_caracteres)

print("Primera letra del texto:", texto[0].upper())

print("Ultima letra del texto:", texto[-1].upper())

texto2 = texto.split()[::-1]

print("Texto con las palabras invertidas:", " ".join(texto2))

diccionario = {True: "Si", False: "No"}

contiene_python = "python" in texto.lower()

print("Python en el texto: ", diccionario[contiene_python])
