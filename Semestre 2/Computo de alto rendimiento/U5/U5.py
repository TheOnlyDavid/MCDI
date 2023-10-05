from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

if rank == 0:
    data = {'a': 7, 'b': 3.14}
    for dest_rank in range(1, 4):  # Send data to ranks 1, 2, and 3
        comm.send(data, dest=dest_rank, tag=11)
elif rank in [1, 2, 3]:  # Receive data from rank 0
    data = comm.recv(source=0, tag=11)

print(f"Rank {rank}: Data received: {data}")
