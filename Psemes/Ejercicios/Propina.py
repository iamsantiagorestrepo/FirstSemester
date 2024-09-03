calificacion = input("Ingrese su calificacion:")
totalcuenta = input("Total cuenta:")


if calificacion in ("Excelente"):
    propina = totalcuenta * 0.20
elif calificacion in ("Bueno"):
    propina = totalcuenta * 0.15
elif calificacion in ("Regular"):
    propina = totalcuenta * 0.10

