import socket
import threading

def handle_client(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(f"Received: {message}")
            # Send message to all clients
        except:
            client_socket.close()
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 5555))
server.listen(5)

print("Server started, waiting for clients...")
while True:
    client_socket, addr = server.accept()
    print(f"Connection from {addr}")
    threading.Thread(target=handle_client, args=(client_socket,)).start()
