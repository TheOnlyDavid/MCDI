from mpi4py import MPI

# Inicializa MPI
comm = MPI.COMM_WORLD

# Obtiene el número de procesos en el comunicador
size = comm.Get_size()

# Imprime el número de procesos
print(f"Número de procesos en el comunicador: {size}")
