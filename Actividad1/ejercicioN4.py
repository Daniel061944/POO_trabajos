# con el imput se ingresa la edad para la variable fe entrada
edad_juan = int(input("Ingresa la edad de Juan: "))
# Calculamos las edades de los demás
edad_alberto = (2 / 3) * edad_juan
edad_ana = (4 / 3) * edad_juan
edad_mama = edad_juan + edad_alberto + edad_ana
#redondear
edad_alberto=round(edad_alberto)
edad_ana =round(edad_ana)
edad_mama=round(edad_mama)
# Salida
print(f"La edad de Juan es {edad_juan} años")
print(f"La edad de Alberto es {edad_alberto:.0f} años")
print(f"La edad de Ana es {edad_ana:.0f} años")
print(f"La edad de la mamá es {edad_mama:.0f} años")