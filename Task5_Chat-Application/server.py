import socket
import threading

# Server details
host = '127.0.0.1'
port = 55555

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        try:
            client.send(message)
        except:

            remove_client(client)

def remove_client(client):
    if client in clients:
        index = clients.index(client)
        nickname = nicknames[index]
        clients.remove(client)
        nicknames.remove(nickname)
        client.close()
        broadcast(f'{nickname} has left the chat!'.encode('utf-8'))

def handle_client(client):
    while True:
        try:
           
            message = client.recv(1024)
            if not message:
                raise Exception("Client disconnected")
            broadcast(message)
        except Exception as e:
           
            print(f"Error: {e}")
            remove_client(client)
            break


def receive_clients():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running...")
receive_clients()
