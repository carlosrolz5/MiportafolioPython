import random

#Este es un juego donde se debe adivinar un numero aleatorio entre 1 y 100, con siete intentos y pistas de "muy bajo" o "muy alto"


#ingresar nombre usuario
nombre = input("ingresa tu nombre: ")
#generar numero entre 1 y 100

print(f"Bueno, {nombre}, he pensado en un numero entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número\n")


#funcion de juego con parametros entre el rango de min y max
def juego(min, max):
    num = random.randint(min, max)
    i = 0
#lista de nums ingresados
    numsIngresados = []
    while(True):
        #try/except mientras true sea cierto
        try:
            #ingresar numero a adivinar
            num_adivinado = int(input("Ingresa el numero que crees que es: "))
            #si se ingresa un numero fuera del rango permitido
            if (num_adivinado < min or num_adivinado > max):
                print("🚫Elegiste un número que no está permitido\n")
            #si se ingresa un numero ya ingresado antes
            elif(num_adivinado in numsIngresados):
                print("☑Ya ingresaste este numero")
            else:
                #si se ingresa un numero valido se agrega a la lista y la cantidad de intentos restantes (i) decrece
                numsIngresados.append(num_adivinado)
                i += 1
                #si se adivina un numero menor al generado
                if(num_adivinado < num):
                    print("❌Adivinaste un numero muy bajo\n")
                #si se adivina un numero mayor al generado
                elif(num_adivinado > num):
                    print("❌Adivinaste un numero muy alto\n")
                else:
                    #si se adivina el numero se imprime esto y el ciclo se rompe
                    print(f"✅Felicidades, te tomo {i} intentos adivinar el numero")
                    break
                if(i == 8):
                    #si se llega a 8 intentis se acaba el juego y se muestra el numero
                    print("⚑ Se te acabaron los intentos")
                    print(f"Numero: {num}")
                    break
        #por si no se ingresa un numero entero
        except ValueError:
            print("🚫No ingresaste un numero entero\n")
        #se muestra la cantidad de intentos que le quedan al usuario
        print(f"Cantidad de intentos restantes: {8 - i}\n")
#se invoca el metodo con los parametros 1 y 100
juego(1, 100)


