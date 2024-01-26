# cliente.py

import socket
import threading

def enviar_mensajes(client_socket):
    while True:
        mensaje = input()
        client_socket.send(mensaje.encode())

# Configuración del cliente
host = "127.0.0.1"
port = 9999

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

# Iniciar un hilo para enviar mensajes
enviar_hilo = threading.Thread(target=enviar_mensajes, args=(client,))
enviar_hilo.start()

# Recibir mensajes del servidor
while True:
    data = client.recv(1024)
    print(data.decode())
