import threading
import time

# Definir semáforos para cada tenedor
tenedor_sem = [threading.Semaphore(1) for _ in range(5)]

def filosofo(id):
    while True:
        # Pensar
        print(f"Filósofo {id} está pensando")

        # Tomar tenedores
        tenedor_sem[id].acquire()
        tenedor_sem[(id + 1) % 5].acquire()

        # Comer
        print(f"Filósofo {id} está comiendo")
        time.sleep(2)  # Simular el tiempo que tarda en comer

        # Soltar tenedores
        tenedor_sem[id].release()
        tenedor_sem[(id + 1) % 5].release()

        # Repetir el ciclo

# Crear hilos para cada filósofo
filosofos = [threading.Thread(target=filosofo, args=(i,)) for i in range(5)]

# Iniciar los hilos
for filosofo_thread in filosofos:
    filosofo_thread.start()

# Esperar a que todos los hilos terminen (esto no debería ocurrir)
for filosofo_thread in filosofos:
    filosofo_thread.join()
