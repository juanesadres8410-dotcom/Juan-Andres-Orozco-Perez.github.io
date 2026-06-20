"""
Project: Teacher Monthly Fees Payroll Processor
Author: Juan
Description: Collects identity metrics for an arbitrary count of teachers, validates hourly rates 
             according to system categories (A, B, C), and yields an aggregate financial summary.
Usage: python liquidacion_docente.py
"""

def validar_categoria():
    while True:
        cat = input("Categoría (A, B o C): ").strip().upper()
        if cat in ['A', 'B', 'C']:
            return cat
        else:
            print("❌ Error: La categoría debe ser A, B o C. Intente nuevamente.")

def validar_horas():
    while True:
        try:
            horas = int(input("Horas laboradas en el mes: "))
            if horas > 0:
                return horas
            else:
                print("❌ Error: Las horas deben ser mayores a 0.")
        except ValueError:
            print("❌ Error: Ingrese un número entero válido.")

# ====================== MENÚ PRINCIPAL ======================
def menu_principal():
    while True:
        print("\n" + "="*55)
        print("     LIQUIDACIÓN DE HONORARIOS DOCENTES")
        print("="*55)
        print("1. Procesar liquidación de docentes")
        print("2. Salir")
        print("="*55)
        
        opcion = input("Seleccione una opción (1-2): ").strip()
        
        if opcion == "1":
            procesar_liquidacion()
        elif opcion == "2":
            print("\n¡Gracias por usar el sistema! Hasta pronto.")
            break
        else:
            print("❌ Opción inválida. Por favor seleccione 1 o 2.")

# ====================== PROCESAR LIQUIDACIÓN ======================
def procesar_liquidacion():
    print("\n--- INGRESO DE DATOS DE DOCENTES ---")
    try:
        N = int(input("Ingrese la cantidad de docentes a procesar: "))
        if N <= 0:
            print("❌ Error: La cantidad debe ser mayor a 0.")
            return
    except ValueError:
        print("❌ Error: Ingrese un número entero válido.")
        return

    # Acumuladores y contadores
    total_pagar = 0
    cont_A = cont_B = cont_C = 0

    for i in range(1, N + 1):
        print(f"\n📌 Docente {i} de {N}")
        documento = input("Documento de identidad: ").strip()
        nombre = input("Nombre completo: ").strip()
        
        categoria = validar_categoria()
        horas = validar_horas()

        # Determinar valor por hora
        if categoria == "A":
            valor_hora = 25000
            cont_A += 1
        elif categoria == "B":
            valor_hora = 35000
            cont_B += 1
        else:  # C
            valor_hora = 50000
            cont_C += 1

        pago_docente = valor_hora * horas
        total_pagar += pago_docente

        print(f"✅ Valor a pagar a {nombre}: ${pago_docente:,.0f}")

    # ====================== RESUMEN FINAL ======================
    print("\n" + "="*60)
    print("                   RESUMEN FINAL")
    print("="*60)
    print(f"Total de docentes procesados     : {N}")
    print(f"Docentes Categoría A             : {cont_A}")
    print(f"Docentes Categoría B             : {cont_B}")
    print(f"Docentes Categoría C             : {cont_C}")
    print(f"VALOR TOTAL A PAGAR              : ${total_pagar:,.0f}")
    print("="*60)

# ====================== INICIO DEL PROGRAMA ======================
if __name__ == "__main__":
    menu_principal()