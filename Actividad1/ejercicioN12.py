# Datos del ejercicio
horas_trabajadas = 48
pago_por_hora = 5000
porcentaje_retencion = 0.125

# Cálculo del salario bruto
salario_bruto = horas_trabajadas * pago_por_hora

# Cálculo de la retención en la fuente
retencion_fuente = salario_bruto * porcentaje_retencion

# Cálculo del salario neto
salario_neto = salario_bruto - retencion_fuente

# Mostrar los resultados
print("Salario Bruto:", salario_bruto)
print("Retención en la Fuente:", retencion_fuente)
print("Salario Neto:", salario_neto)
