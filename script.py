print("*" * 40)
print("BIENVENIDO A LA CALCULADORA DE COMISIONES")
print("*" * 40)

while True:
    try:
        venta = float(input("Ingree el monto de la venta: "))
        p_comision = float(input("Ingrese el porcentaje de la comisión: "))
        comision = (venta * p_comision) / 100
        total = comision + venta
        if(venta < 0  or p_comision < 0):
            print("No pueden ingresarse valores o menores a cero")
            continue

    except ValueError:
        print("No ingresaste un valor flotante")
        continue

    print("*" * 40)
    print("Resultados: ")
    print("*" * 40)
    print(f"Monto: ${venta:.2f}")
    print(f"Porcentaje de comision: {p_comision:.2f}%")
    print(f"Comision: ${comision:.2f}")
    print(f"Total: ${total:.2f}")
    print("*" * 40)
