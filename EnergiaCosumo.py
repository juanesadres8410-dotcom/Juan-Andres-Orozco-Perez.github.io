"""
Project: Electricity Consumption Invoice Generator
Author: Juan
Description: Computes accurate electricity bills using an exact unit rate per watt (750 COP), 
             applies social stratum discounts, and prints a structured receipt.
Usage: python EnergiaCosumo.py
"""

nombre = input("Ingrese su nombre: ")
estrato = int(input("Ingrese su estrato (1-5): "))
consumo = int(input("Ingrese su consumo en watts: "))

tarifas = {
    1: 80000,
    2: 100000,
    3: 150000,
    4: 180000,
    5: 200000
}

tarifa = tarifas.get(estrato, 0)
valor_consumo = consumo * 750

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

total = valor_consumo - (valor_consumo * descuento)

print("\n----- FACTURA -----")
print("Nombre:", nombre)
print("Estrato:", estrato)
print("Tarifa básica:", tarifa)
print("Valor por consumo:", valor_consumo)
print("Descuento aplicado:", descuento * 100, "%")
print("Total a pagar:", total)