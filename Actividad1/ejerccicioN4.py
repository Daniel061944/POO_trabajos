# Ingresamos la edad de Juan
edad_juan = int(input("Ingresa la edad de Juan: "))

# Calculamos las edades de los demás
edad_alberto = (2 / 3) * edad_juan
edad_ana = (4 / 3) * edad_juan
edad_mama = edad_juan + edad_alberto + edad_ana

# Mostramos las edades
print(f"La edad de Juan es: {edad_juan} años")
print(f"La edad de Alberto es: {edad_alberto:.1f} años")
print(f"La edad de Ana es: {edad_ana:.1f} años")
print(f"La edad de la mamá es: {edad_mama:.1f} años")