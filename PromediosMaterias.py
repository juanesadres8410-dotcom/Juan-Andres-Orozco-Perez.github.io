"""
Project: Academic Grades Average Calculator
Author: Juan
Description: Computes distinct sub-weighted averages for Mathematics, Physics, and Chemistry 
             based on custom exam/homework weights, and calculates the overall general average.
Usage: python "Promedio Materias.py"
"""

exMat = float(input("Examen Matemáticas: "))
t1 = float(input("Tarea 1 Matemáticas: "))
t2 = float(input("Tarea 2 Matemáticas: "))
t3 = float(input("Tarea 3 Matemáticas: "))

mat = (exMat * 0.90) + ((t1 + t2 + t3) / 3 * 0.10)

exFis = float(input("Examen Física: "))
f1 = float(input("Tarea 1 Física: "))
f2 = float(input("Tarea 2 Física: "))

fis = (exFis * 0.80) + ((f1 + f2) / 2 * 0.20)

exQui = float(input("Examen Química: "))
q1 = float(input("Tarea 1 Química: "))
q2 = float(input("Tarea 2 Química: "))
q3 = float(input("Tarea 3 Química: "))

qui = (exQui * 0.85) + ((q1 + q2 + q3) / 3 * 0.15)

promedioGeneral = (mat + fis + qui) / 3

print("Promedio Matemáticas:", mat)
print("Promedio Física:", fis)
print("Promedio Química:", qui)
print("Promedio General:", promedioGeneral)