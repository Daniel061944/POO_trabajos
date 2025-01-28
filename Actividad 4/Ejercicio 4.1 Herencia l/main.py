from CuentaAhorros import CuentaAhorros
saldo_inicial = 100000
tasa_interes = 0.1
cuenta_ahorros = CuentaAhorros(saldo_inicial, tasa_interes)
print("=== Cuenta de ahorros ===")
cuenta_ahorros.consignar(50000)
cuenta_ahorros.retirar(70000)    
cuenta_ahorros.extracto_mensual()
cuenta_ahorros.imprimir()  