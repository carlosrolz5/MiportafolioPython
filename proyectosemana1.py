
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

nom_completo = nombre + " " + apellido
print("Tu nombre es: " + nom_completo)
print("Tus iniciales son: " + nombre[0] + ". " + apellido[0])
print("Una version divertida de tu nombre es: " + nombre[::-1] + " " + apellido[::-1])
nom_mayuscula = ""
for letra in nom_completo:
    nom_mayuscula += letra.upper()
print("Nombre en mayusculas :", nom_mayuscula)
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cant_letras = 0
for nom in nom_completo:
    for letra in nom:
        if letra.upper() in letras:
            cant_letras += 1
print("Cantidad de letras en tu nombre: ", cant_letras)
""""
def contar_letras(nombre, cant_letras):
    for letra in nombre:
        if (letra.upper() in letras):
            cant_letras += 1
    return cant_letras
"""
#print(f"Cantidad de letras de tu nombre : {contar_letras(nombre, cant_letras) + contar_letras(apellido, cant_letras)}")

print("Apellido y nombre: " + apellido + ", " + nombre)

