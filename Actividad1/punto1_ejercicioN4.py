edadjuan = int(input("Ingresa la edad de Juan: "))
edadalberto = (2 / 3) * edadjuan
edadana = (4 / 3) * edadjuan
edadmama = edadjuan + edadalberto + edadana
edadalberto=round(edadalberto)
edadana =round(edadana)
edadmama=round(edadmama)
print(f"La edad de Juan es {edadjuan} años")
print(f"La edad de Alberto es {edadalberto:.0f} años")
print(f"La edad de Ana es {edadana:.0f} años")
print(f"La edad de la mamá es {edadmama:.0f} años")
