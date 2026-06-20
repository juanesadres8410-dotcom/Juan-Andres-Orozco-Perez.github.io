"""
Project: Electricity Base Rate Utility Calculator
Author: Juan
Description: Looks up flat-rate residential electricity base fees based on social stratum (1-5) 
             and subtracts a usage-cap discount if the total consumption is low.
Usage: python EnergiaBasica.py
"""

nombre = input("Ingrese su nombre: ")
estrato = int(input("Ingrese su estrato (1-5): "))
consumo = int(input("Ingrese su consumo en watts: "))

tarifas = {1: 10000, 2: 15000, 3: 30000, 4: 50000, 5: 65000}
tarifa = tarifas.get(estrato, 0)

descuento = 0
if estrato == 1 and consumo < 100:
    descuento = 0.05
elif estrato == 2 and consumo < 200:
    descuento = 0.03
elif estrato == 3 and consumo < 300:
    descuento = 0.02
elif estrato == 4 and consumo < 400:
    descuento = 0.01
elif estrato == 5 and consumo < 500:
    descuento = 0.005

total = tarifa - (tarifa * descuento)

print("Nombre:", nombre)
print("Estrato:", estrato)
print("Tarifa básica:", tarifa)
print("Valor a pagar:", total)