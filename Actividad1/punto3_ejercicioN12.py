# Datos del ejercicio
horas = 48
sueldo = 5000
ret = 0.125 #12.5% del salario bruto
# Calculos que se pide
salarioB = horas * sueldo
retencionfuente = salarioB * ret
salarioN = salarioB - retencionfuente
# informacion que se desea saber
print("El Salario Bruto del trabajador es:", int(salarioB))
print("La Retención en la Fuente del trabajador es:", int(retencionfuente))
print("El Salario Neto del trabajador es:", int(salarioN))
