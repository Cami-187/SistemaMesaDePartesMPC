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
=======
        print(f"Error al guardar los datos: {e}")
>>>>>>> eb143490ddb71ef6d2a6af3fe17fb19664f49631
