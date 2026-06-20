"""
Project: Logistics Zone Freight Calculator
Author: Juan
Description: Calculates cargo shipping costs across Colombian regions, applying targeted 
             weight-based surcharge increments and adding standard 19% IVA tax.
Usage: python "Transporte ABC.py"
"""

nombre = input("Ingrese el nombre del cliente: ")
zona = input("Ingrese la zona (Andina, Caribe, Orinoquia, Amazonica, Pacifica): ")
peso = float(input("Ingrese el peso del paquete en kilos: "))

costos = {
    "Andina": 5000,
    "Caribe": 7500,
    "Orinoquia": 10000,
    "Amazonica": 9000,
    "Pacifica": 8500
}

costo_kilo = costos.get(zona, 0)
subtotal = peso * costo_kilo
incremento = 0

if zona == "Andina" and peso > 10:
    incremento = 0.05
elif zona == "Caribe" and peso > 10:
    incremento = 0.07
elif zona == "Orinoquia" and peso > 10:
    incremento = 0.10
elif zona == "Amazonica" and peso > 10:
    incremento = 0.15
elif zona == "Pacifica" and peso > 10:
    incremento = 0.125

subtotal += subtotal * incremento
iva = subtotal * 0.19
total = subtotal + iva

print("----- FACTURA -----")
print("Cliente:", nombre)
print("Zona:", zona)
print("Peso:", peso)
print("Subtotal:", subtotal)
print("IVA (19%):", iva)
print("Total a pagar:", total)