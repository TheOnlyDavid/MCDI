# server.py

import socket
import threading

def handle_client(client_socket, address):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            message = f"[{address[0]}:{address[1]}] {data.decode()}"
            print(message)
            broadcast(message)
        except:
            break

def broadcast(message):
    for client in clients:
        try:
            client.send(message.encode())
        except:
            continue

# Configuración del servidor
host = "0.0.0.0"
port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(5)

print(f"[*] Escuchando en {host}:{port}")

# Lista para almacenar clientes
clients = []

while True:
    client, address = server.accept()
    print(f"[*] Conexión aceptada de {address[0]}:{address[1]}")

    # Iniciar un hilo para manejar al cliente
    client_handler = threading.Thread(target=handle_client, args=(client, address))
    client_handler.start()

    # Agregar el cliente a la lista
    clients.append(client)
