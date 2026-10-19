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
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 09df31d165647615446371bc532ce0899eafbffa
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
<<<<<<< HEAD

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


=======
=======
        print(f"Error al guardar los datos: {e}")
>>>>>>> eb143490ddb71ef6d2a6af3fe17fb19664f49631
>>>>>>> 09df31d165647615446371bc532ce0899eafbffa
