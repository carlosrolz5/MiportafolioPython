import random

nombre = input("ingresa tu nombre: ")

print(f"Bueno, {nombre}, he pensado en un numero entre 1 y 100, y tienes solo ocho intentos para adivinar cuál crees que es el número\n")
def juego(min, max):
    num = random.randint(min, max)
    i = 0

    numsIngresados = []
    while(True):
        try:
            num_adivinado = int(input("Ingresa el numero que crees que es: "))
            if (num_adivinado < min or num_adivinado > max):
                print("🚫Elegiste un número que no está permitido\n")
            elif(num_adivinado in numsIngresados):
                print("☑Ya ingresaste este numero")
            else:
                numsIngresados.append(num_adivinado)
                i += 1
                if(num_adivinado < num):
                    print("❌Adivinaste un numero muy bajo\n")
                elif(num_adivinado > num):
                    print("❌Adivinaste un numero muy alto\n")
                else:
                    print(f"✅Felicidades, te tomo {i} intentos adivinar el numero")
                    break
                if(i == 8):
                    print("⚑ Se te acabaron los intentos")
                    print(f"Numero: {num}")
                    break
        except ValueError:
            print("🚫No ingresaste un numero entero\n")
        print(f"Cantidad de intentos restantes: {8 - i}\n")
juego(1, 100)
#print(f"Partidas ganadas: {ganadas}")
#print(f"Partidas perdidas: {perdidas}")