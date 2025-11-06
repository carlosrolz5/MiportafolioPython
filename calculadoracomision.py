#titulo con cuarenta asteriscos
print("*" * 40)
print("BIENVENIDO A LA CALCULADORA DE COMISIONES")
print("*" * 40)

#ingresar datos de la venta y el porcentaje de la comision
venta = float(input("Ingrese el monto de la venta: "))
p_comision = float(input("Ingrese el porcentaje de la comisión: "))
#calculos
comision = (venta * p_comision) / 100
total = comision + venta




#Mostrar resultados rondeados a dos decimales
print("*" * 40)
print("Resultados: ")
print("*" * 40)
print(f"Monto: ${venta:.2f}")
print(f"Porcentaje de comision: {p_comision:.2f}%")
print(f"Comision: ${comision:.2f}")
print(f"Total: ${total:.2f}")
print("*" * 40)
