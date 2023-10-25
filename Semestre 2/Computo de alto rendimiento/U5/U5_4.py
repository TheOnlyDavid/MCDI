from mpi4py import MPI
import time
import numpy as np

# Inicializa MPI
comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

# Definir el tamaño de la matriz
N = size  # Asumiendo que el número de filas de la matriz es igual al número de procesos

# Registro del tiempo de inicio para la versión paralela
start_time_parallel = time.time()

# Generar matriz A y vector x en el proceso 0
if rank == 0:
    matrix_A = np.random.rand(N, N)
    vector_x = np.random.rand(N, 1)
else:
    matrix_A = None
    vector_x = None

# Distribuir la matriz A y difundir el vector x
matrix_A = comm.scatter(matrix_A, root=0)
vector_x = comm.bcast(vector_x, root=0)

# Realizar la multiplicación de matriz-vector local
local_result = np.dot(matrix_A, vector_x)

# Recopilar los resultados locales en el proceso 0
global_result = comm.gather(local_result, root=0)

# Registro del tiempo de finalización para la versión paralela
end_time_parallel = time.time()

# Comparación de métricas de desempeño
if rank == 0:
    result_vector = np.sum(global_result, axis=0)
    print(f"Resultado de la multiplicación (paralelo):")
    print(result_vector)
    print(f"Tiempo de ejecución (paralelo): {end_time_parallel - start_time_parallel} segundos")

# Registro del tiempo de inicio para la versión serial
start_time_serial = time.time()

# Código serial
if rank == 0:
    serial_result = np.dot(matrix_A, vector_x)
else:
    serial_result = None

# Recopilar los resultados locales en el proceso 0 (serial)
serial_result = comm.gather(serial_result, root=0)

# Registro del tiempo de finalización para la versión serial
end_time_serial = time.time()

# Comparación de métricas de desempeño
if rank == 0:
    result_vector = np.sum(serial_result, axis=0)
    print(f"Resultado de la multiplicación (serial):")
    print(result_vector)
    print(f"Tiempo de ejecución (serial): {end_time_serial - start_time_serial} segundos")

# Finaliza MPI
MPI.Finalize()
