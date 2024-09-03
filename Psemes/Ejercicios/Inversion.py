monto = float(input("Ingrese el monto a invertir: "))
tanual = float(input("Ingrese la tasa anual: "))
tiempoi=float(input("Ingrese el tiempo de la inversion"))

isimple = monto * tanual/100 * tiempoi
montototal = isimple + monto

print(f"El interes simple es: {isimple}")
print(f"La ganancia total es: {montototal}")
