





import random
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
palabras = ["banana", "naranja", "bicicleta", "manzana", "tijeras", "zanahoria", "lechuga", "cebolla", "remolacha", "tomate", "perro", "serpiente", "avestruz", "lagartija", "ardilla", "armadillo", "gorila", "hormiga", "mariposa", "libelula", "lombriz", "pavorreal", "aguila", "gaviota", "cangrejo", "langosta", "dinosaurio", "iguana", "renacuajo", "tiburon", "tortuga", "mantarraya", "escarabajo", "ciempies", "camaleon", "escorpion", "herizo"]
palabra = random.choice(palabras)
espacios = ""
for letra in palabra:
    espacios += "-"
letras_adivinadas = []
intentos_restantes = 7
print(espacios)
#print(list(palabra)[0])
while True:
    letra = input("Ingresa una letra: ")
    condicion1 = len(letra) == 1
    condicion2 = letra.upper() in letras
    condicion3 = letra.upper() not in letras_adivinadas
    if(condicion1 and condicion2 and condicion3):
        letras_adivinadas.append(letra.upper())
        if letra.lower() not in list(palabra):
            intentos_restantes -= 1
            print(f"Te queda(n) {intentos_restantes} intento(s)")
            print(espacios)

        else:
            palabra = list(palabra)
            espacios = list(espacios)
            for i in range(len(palabra)):
                if(palabra[i] == letra.lower()):
                    espacios[i] = letra.lower()
            espacios = "".join(espacios)
            print(espacios)l
            print(f"Te queda(n) {intentos_restantes} intento(s)")


    else:
        print("Solamente se puede ingresar una letra que no se haya ingresado antes")
    perdido = intentos_restantes == 0
    ganado = list(espacios) == list(palabra)
    if(ganado or perdido):
        break
print("".join(palabra))

if(ganado):
    print("🎉Felicidades, ganaste")

else:
    print("👎Lo siento, perdiste")
