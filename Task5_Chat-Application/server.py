import socket
import threading

host = '127.0.0.1'
port = 55555        

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle_client(client):
    while True:
        try:
            # Receive a message from the client
            message = client.recv(1024)
            # Broadcast the message to other clients
            broadcast(message)
        except:
            # Remove and close the client
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} has left the chat!'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive_clients():
    while True:
        client, address = server.accept()
        print(f'Connected with {str(address)}')

        # Request and store the nickname
        client.send('NICK'.encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        # Start handling the client
        thread = threading.Thread(target=handle_client, args=(client,))
        thread.start()

print("Server is running...")
receive_clients()
