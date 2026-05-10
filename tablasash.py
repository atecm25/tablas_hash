# =========================================
# TABLAS HASH - ANALIZADOR DE TOKENS
# =========================================

# Tabla hash usando diccionario
tabla_hash = {}

# Símbolos permitidos
simbolos = ['=', '+', '-', '*', '/', ';', ',', '(', ')']

# Cantidad de líneas
n = int(input("Cantidad de lineas de codigo: "))

print("\nIngrese el codigo:")

lineas = []

for i in range(n):
    linea = input()
    lineas.append(linea)

# =========================================
# ANALISIS DE TOKENS
# =========================================

for fila in range(len(lineas)):

    linea = lineas[fila]
    i = 0

    while i < len(linea):

        # Ignorar espacios
        if linea[i].isspace():
            i += 1
            continue

        columna = i
        token = ""

        # ---------------------------------
        # Identificadores o palabras
        # ---------------------------------
        if linea[i].isalpha() or linea[i] == '_':

            while i < len(linea) and \
                  (linea[i].isalnum() or linea[i] == '_'):

                token += linea[i]
                i += 1

        # ---------------------------------
        # Números enteros o decimales
        # ---------------------------------
        elif linea[i].isdigit():

            decimal = False

            while i < len(linea) and \
                  (linea[i].isdigit() or linea[i] == '.'):

                if linea[i] == '.':

                    if decimal:
                        break

                    decimal = True

                token += linea[i]
                i += 1

        # ---------------------------------
        # Símbolos
        # ---------------------------------
        elif linea[i] in simbolos:

            token += linea[i]
            i += 1

        else:
            i += 1
            continue

        # Generar clave hash
        clave = f"{fila},{columna}"

        # Insertar en tabla hash
        tabla_hash[clave] = token

# =========================================
# MOSTRAR TABLA HASH
# =========================================

print("\n===== TABLA HASH =====")

print("\nClave\t\tToken")

for clave, token in tabla_hash.items():
    print(f"{clave}\t\t{token}")

# =========================================
# BUSQUEDA
# =========================================

buscar = input("\nIngrese la clave a buscar (fila,columna): ")

if buscar in tabla_hash:
    print("Token encontrado:", tabla_hash[buscar])
else:
    print("Clave no encontrada")