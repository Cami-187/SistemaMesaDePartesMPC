import os

# --- VARIABLES GLOBALES (Listas Paralelas) ---
# Almacenarán la información de cada expediente en memoria
codigos = []
dnis = []
nombres = []
direcciones = []
referencias = []
cumple_tupa = []

# Archivo de persistencia
ARCHIVO_DATOS = "expedientes.txt"

# --- FUNCIONES DE ALMACENAMIENTO (Persistencia) ---

def cargar_expedientes():
    """Carga los datos del archivo a las listas paralelas al iniciar el sistema."""
    if not os.path.exists(ARCHIVO_DATOS):
        return # Si el archivo no existe, no hace nada

    try:
        with open(ARCHIVO_DATOS, 'r', encoding='utf-8') as archivo:
            for linea in archivo:
                # Quitamos el salto de línea y dividimos por un separador, ej: "|"
                datos = linea.strip().split('|')
                if len(datos) == 6:
                    codigos.append(datos[0])
                    dnis.append(datos[1])
                    nombres.append(datos[2])
                    direcciones.append(datos[3])
                    referencias.append(datos[4])
                    cumple_tupa.append(datos[5])
        print("Datos cargados exitosamente desde el archivo.")
    except Exception as e:
        print(f"Error al cargar los datos: {e}")

def guardar_expedientes():
    """Guarda los datos de las listas paralelas en el archivo de texto."""
    try:
        with open(ARCHIVO_DATOS, 'w', encoding='utf-8') as archivo:
            for i in range(len(codigos)):
                # Guardamos cada registro separado por "|"
                linea = f"{codigos[i]}|{dnis[i]}|{nombres[i]}|{direcciones[i]}|{referencias[i]}|{cumple_tupa[i]}\n"
                archivo.write(linea)
        print("Datos guardados en el archivo correctamente.")
    except Exception as e:

        print(f"Error al guardar los datos: {e}")

    # --- FUNCIONES DE VALIDACIÓN ---

def validar_dni(dni):
    """Valida que el DNI tenga exactamente 8 dígitos numéricos."""
    if len(dni) == 8 and dni.isdigit():
        return True
    return False

def generar_codigo():
    """Genera un código correlativo automático (ej. EXP-001)."""
    if len(codigos) == 0:
        return "EXP-001"
    else:
        # Extrae el número del último código, lo incrementa y formatea
        ultimo_codigo = codigos[-1]
        numero = int(ultimo_codigo.split('-')[1])
        nuevo_numero = numero + 1
        return f"EXP-{nuevo_numero:03d}"

# --- FUNCIONES PRINCIPALES ---

def registrar_expediente():
    print("\n--- REGISTRO DE NUEVO EXPEDIENTE ---")
    
    # Ingreso y validación de DNI
    dni = input("Ingrese el DNI (8 dígitos): ")
    if not validar_dni(dni):
        print("Error: El DNI debe contener exactamente 8 dígitos numéricos.")
        return # Sale de la función si el DNI no es válido

    # Ingreso de datos obligatorios
    nombre = input("Ingrese los Nombres y Apellidos completos: ").strip()
    direccion = input("Ingrese la Dirección actual: ").strip()
    
    # Ingreso de datos opcionales
    referencia = input("Ingrese una Referencia de dirección (Opcional, presione Enter para omitir): ").strip()
    if referencia == "":
        referencia = "Sin referencia"

    # Verificación de requisitos TUPA
    print("¿El expediente cumple con todos los requisitos del TUPA correspondientes al trámite?")
    tupa_input = input("(Escriba 'SI' para continuar o 'NO' si faltan requisitos): ").strip().upper()

    if tupa_input == "SI":
        # Generación de código
        nuevo_codigo = generar_codigo()
        
        # Guardar en las listas paralelas
        codigos.append(nuevo_codigo)
        dnis.append(dni)
        nombres.append(nombre)
        direcciones.append(direccion)
        referencias.append(referencia)
        cumple_tupa.append(tupa_input)
        
        # Guardar cambios en el archivo
        guardar_expedientes()
        
        print(f"\n¡Registro Exitoso!")
        print(f"Se ha generado el cargo de recepción. Código único del expediente: {nuevo_codigo}")
    else:
        print("\nAtención: El expediente no cuenta con todos los requisitos del TUPA.")
        print("Según el procedimiento, el ciudadano tiene un plazo (ej. 2 días) para subsanar los documentos faltantes.")
        print("El expediente NO ha sido ingresado al sistema para su derivación final.")

def buscar_expediente():
    print("\n--- BÚSQUEDA DE EXPEDIENTE ---")
    codigo_buscar = input("Ingrese el código único del expediente (ej. EXP-001): ").strip().upper()
    
    # Búsqueda secuencial (Cross-Referencing)
    encontrado = False
    for i in range(len(codigos)):
        # Ignoramos mayúsculas/minúsculas para una búsqueda más robusta
        if codigos[i].upper() == codigo_buscar:
            print("\n--- EXPEDIENTE ENCONTRADO ---")
            print(f"Código:     {codigos[i]}")
            print(f"Ciudadano:  {nombres[i]}")
            print(f"DNI:        {dnis[i]}")
            print(f"Dirección:  {direcciones[i]}")
            print(f"Referencia: {referencias[i]}")
            print(f"Revisión:   Cumplió requisitos TUPA")
            encontrado = True
            break # Detenemos el bucle al encontrarlo
            
    if not encontrado:
        print("Error: No se encontró ningún expediente con ese código.")

def ordenar_expedientes():
    print("\n--- ORDENAR EXPEDIENTES ---")
    cantidad = len(codigos)
    if cantidad == 0:
        print("No hay expedientes registrados para ordenar.")
        return

    # Adaptación del algoritmo de Burbuja para ordenar por código (A-Z)
    for i in range(cantidad - 1):
        for j in range(cantidad - 1 - i):
            # Compara usando el valor numérico del código para ordenar correctamente
            num_j = int(codigos[j].split('-')[1])
            num_siguiente = int(codigos[j+1].split('-')[1])
            
            if num_j > num_siguiente:
                # Intercambio (Swap) en TODAS las listas paralelas para no perder coherencia
                codigos[j], codigos[j+1] = codigos[j+1], codigos[j]
                dnis[j], dnis[j+1] = dnis[j+1], dnis[j]
                nombres[j], nombres[j+1] = nombres[j+1], nombres[j]
                direcciones[j], direcciones[j+1] = direcciones[j+1], direcciones[j]
                referencias[j], referencias[j+1] = referencias[j+1], referencias[j]
                cumple_tupa[j], cumple_tupa[j+1] = cumple_tupa[j+1], cumple_tupa[j]
    
    # Guardar la lista ya ordenada
    guardar_expedientes()
    print("Expedientes ordenados por código correctamente.")
    
    # Mostrar la lista ordenada brevemente
    print(f"\nTotal registrados: {cantidad}")
    for i in range(cantidad):
        print(f"{codigos[i]} - {nombres[i]} - DNI: {dnis[i]}")
# --- MENÚ PRINCIPAL ---

def mostrar_menu():
    cargar_expedientes() # Cargar datos al iniciar
    
    while True:
        print("\n" + "="*40)
        print("  SISTEMA DE MESA DE PARTES DIGITAL")
        print("  Municipalidad Provincial de Cajamarca")
        print("="*40)
        print("1. Registrar nuevo expediente")
        print("2. Buscar expediente")
        print("3. Ordenar expedientes")
        print("4. Salir del sistema")
        print("="*40)
        
        opcion = input("Seleccione una opción (1-4): ")
        
        # Uso de match-case (requiere Python 3.10 o superior)
        match opcion:
            case "1":
                registrar_expediente()
            case "2":
                buscar_expediente()
            case "3":
                ordenar_expedientes()
            case "4":
                print("Guardando datos y saliendo del sistema. ¡Hasta luego!")
                break # Rompe el ciclo while
            case _:
                print("Opción no válida. Por favor, ingrese un número del 1 al 4.")

# --- PUNTO DE ENTRADA ---
if __name__ == "__main__":
    mostrar_menu()