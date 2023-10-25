from mpi4py import MPI
import time

# Registro del tiempo de inicio para la versión paralela
start_time_parallel = time.time()

# Inicializa MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Define los vectores de prueba (completos)
vector_a = [1, 2, 3, 4]
vector_b = [5, 6, 7, 8]

# Realiza el producto escalar local
local_result = sum(a * b for a, b in zip(vector_a, vector_b))

# Reduce los resultados locales para obtener el resultado global
global_result = comm.reduce(local_result, op=MPI.SUM, root=0)

# Registro del tiempo de finalización para la versión paralela
end_time_parallel = time.time()

# Comparación de métricas de desempeño
if rank == 0:
    print(f"Resultado del producto escalar (paralelo): {global_result}")
    print(f"Tiempo de ejecución (paralelo): {end_time_parallel - start_time_parallel} segundos")

# Registro del tiempo de inicio para la versión serial
start_time_serial = time.time()

# Código serial
serial_result = sum(a * b for a, b in zip(vector_a, vector_b))

# Registro del tiempo de finalización para la versión serial
end_time_serial = time.time()

# Comparación de métricas de desempeño
if rank == 0:
    print(f"Resultado del producto escalar (serial): {serial_result}")
    print(f"Tiempo de ejecución (serial): {end_time_serial - start_time_serial} segundos")

# Finaliza MPI
MPI.Finalize()

