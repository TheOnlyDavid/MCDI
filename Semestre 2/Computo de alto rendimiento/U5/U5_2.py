from mpi4py import MPI
import time

# Registro del tiempo de inicio para la versión paralela
start_time_parallel = time.time()

# Inicializa MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Definir el mensaje inicial
message = f"Mensaje de proceso {rank}"

# Enviar y recibir mensajes encadenados
for dest in range(1, size):
    if rank == dest:
        received_message = comm.recv(source=rank - 1)
        print(f"Soy el proceso {rank} y he recibido: {received_message}")
    elif rank == dest - 1:
        comm.send(message, dest=dest)

# Registro del tiempo de finalización para la versión paralela
end_time_parallel = time.time()

# Comparación de métricas de desempeño
if rank == 0:
    print(f"Tiempo de ejecución (paralelo): {end_time_parallel - start_time_parallel} segundos")

# Registro del tiempo de inicio para la versión serial
start_time_serial = time.time()

# Código serial
for i in range(size - 1):
    message = f"Mensaje de proceso {i}"
    print(f"Soy el proceso {i} y he recibido: {message}")

# Registro del tiempo de finalización para la versión serial
end_time_serial = time.time()

# Comparación de métricas de desempeño
if rank == 0:
    print(f"Tiempo de ejecución (serial): {end_time_serial - start_time_serial} segundos")

# Finaliza MPI
MPI.Finalize()
