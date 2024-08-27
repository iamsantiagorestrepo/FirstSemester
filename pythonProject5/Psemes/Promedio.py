nota1 = float(input("Ingrese la primer calificacion: "))
nota2 = float(input("Ingrese la segunda calificacion "))
nota3 = float(input("Ingrese la tercera calificacion "))

promedio=(nota1+nota2+nota3)/3

if promedio>= 5:
    print("Aprobaste con un promedio de:", promedio)
else:
    print("Reprobraste con un promedio de", promedio)



