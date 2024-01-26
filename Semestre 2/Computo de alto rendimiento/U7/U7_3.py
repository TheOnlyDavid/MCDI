import threading
import sys

def contar_palabras(nombre_archivo):
    try:
        with open(nombre_archivo, 'r') as archivo:
            contenido = archivo.read()
            palabras = len(contenido.split())
            print(f"{nombre_archivo}: {palabras} palabras")
            return palabras
    except FileNotFoundError:
        print(f"¡Error! El archivo {nombre_archivo} no fue encontrado.")
        return 0

def contar_palabras_concurrente(archivos):
    hilos = []
    resultados = []

    # Crear un hilo por cada archivo
    for archivo in archivos:
        hilo = threading.Thread(target=lambda a: resultados.append(contar_palabras(a)), args=(archivo,))
        hilos.append(hilo)

    # Iniciar los hilos
    for hilo in hilos:
        hilo.start()

    # Esperar a que todos los hilos terminen
    for hilo in hilos:
        hilo.join()

    # Imprimir el total de palabras
    total_palabras = sum(resultados)
    print(f"Total: {total_palabras} palabras")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Por favor, proporciona al menos un nombre de archivo como parámetro.")
    else:
        archivos_a_contar = sys.argv[1:]
        contar_palabras_concurrente(archivos_a_contar)
