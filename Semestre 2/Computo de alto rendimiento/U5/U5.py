from mpi4py import MPI
import time

start_time_parallel = time.time()
# Inicializa MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define el número de divisiones para la aproximación
precision_factor = 1000000  

# Calcula el rango de trabajo para cada proceso
chunk_size = precision_factor // size
start = rank * chunk_size
end = (rank + 1) * chunk_size

# Calcula la suma de Riemann en el rango asignado
partial_sum = 0.0
for i in range(start, end):
    x = (i + 0.5) / precision_factor
    partial_sum += 4.0 / (1.0 + x**2)

# Realiza la reducción para obtener el resultado global
total_sum = comm.reduce(partial_sum, op=MPI.SUM, root=0)

# En el proceso 0, muestra el resultado
if rank == 0:
    pi_parallel = total_sum / precision_factor
    end_time_parallel = time.time()
    print(f"Valor aproximado de π (paralelo): {pi_parallel}")
    print(f"Tiempo de ejecución (paralelo): {end_time_parallel - start_time_parallel} segundos")

start_time_serial = time.time()

# Código serial
precision_factor = 1000000
partial_sum = 0.0
for i in range(precision_factor):
    x = (i + 0.5) / precision_factor
    partial_sum += 4.0 / (1.0 + x**2)
pi_serial = partial_sum / precision_factor

# Registro del tiempo de finalización para la versión serial
end_time_serial = time.time()

print(f"Valor aproximado de π (serial): {pi_serial}")
print(f"Tiempo de ejecución (serial): {end_time_serial - start_time_serial} segundos")
