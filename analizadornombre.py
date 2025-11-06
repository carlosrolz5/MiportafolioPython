
#Este es un programa donde se ingresa el nombre y el apellido y se hacen acciones como mostrar una version divertida 


#ingresar nombre y apellido
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")
#registrar nombre completo
nom_completo = nombre + " " + apellido
#imprimir nombre completo
print("Tu nombre es: " + nom_completo)}
#imprimir iniciales
print("Tus iniciales son: " + nombre[0] + ". " + apellido[0])
#version divertida (nombre invertido y apellido invertido)
print("Una version divertida de tu nombre es: " + nombre[::-1] + " " + apellido[::-1])
"inicializar variable de nombre en mayuscula
nom_mayuscula = ""
#recorrer nombre completo y agregar cada letra en mayuscula a la variable nom_mayuscula
for letra in nom_completo:
    nom_mayuscula += letra.upper()
#imprimir nombre en mayuscula
print("Nombre en mayusculas :", nom_mayuscula)
#variable con todas las letras del abecedario
letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#contador que cuenta la cantidad de letras del nombre completo
cant_letras = 0
#se recorre cada letra del nombre, se convierte a mayuscula para compararla con la variable de letras y se incrementa el contador
for nom in nom_completo:
    for letra in nom:
        if letra.upper() in letras:
            cant_letras += 1

print("Cantidad de letras en tu nombre: ", cant_letras)



