import threading

# Crear semáforos para cada hilo
sem_quijote = threading.Semaphore(1)
sem_romeo = threading.Semaphore(0)
sem_julieta = threading.Semaphore(0)

# Función que simula la escritura en el fichero
def escribir_en_fichero(mensaje, sem_actual, sem_siguiente, nombre_hilo):
    global fichero
    for linea in mensaje:
        sem_actual.acquire()  # Esperar su turno
        fichero.write(linea + '\n')
        sem_siguiente.release()  # Liberar al siguiente hilo
        print(f"{nombre_hilo}: escribió una línea")

# Crear el fichero compartido
fichero = open('historias.txt', 'w')

# Crear los hilos
hilo_quijote = threading.Thread(target=escribir_en_fichero, args=(
    ["En un lugar de la Mancha de cuyo nombre no quiero",
     "acordarme, no ha mucho tiempo que vivía un hidalgo de",
     "los de lanza en astillero, adarga antigua, rocín flaco y galgo",
     "corredor.", "Una olla de algo mas vaca que carnero, salpicón las más",
     "noches, duelos y quebrantos los sábados, lentejas los vier-",
     "nes..."], sem_quijote, sem_romeo, "Quijote"))

hilo_romeo = threading.Thread(target=escribir_en_fichero, args=(
    ["- Habla. ¡Oh! ¡Habla otra vez angel resplandeciente!. . .",
     "Porque esta noche apareces tan esplendorosa sobre mi",
     "cabeza como un alado mensajero celeste ante los ojos",
     "estáticos y maravillados de los mortales, que se inclinan",
     "hacia atrás para verle, cuando él cabalga sobre las tardas",
     "perezosas nubes y navega en el seno del aire."], sem_romeo, sem_julieta, "Romeo"))

hilo_julieta = threading.Thread(target=escribir_en_fichero, args=(
    ["¡Oh Romeo, Romeo! ¿Por qué eres tú Romeo? Niega a tu",
     "padre y rehúsa tu nombre; o, si no quieres, jurame tan",
     "sólo que me amas, y dejaré yo de ser una",
     "Capuleto."], sem_julieta, sem_quijote, "Julieta"))

# Iniciar los hilos
hilo_quijote.start()
hilo_romeo.start()
hilo_julieta.start()

# Esperar a que todos los hilos terminen
hilo_quijote.join()
hilo_romeo.join()
hilo_julieta.join()

# Cerrar el fichero
fichero.close()
print("Programa completado")
