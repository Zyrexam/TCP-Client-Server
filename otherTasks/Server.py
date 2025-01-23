import socket

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1) 
    print("Server is listening for connections...")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection established with {address}")
        client_socket.sendall(b"Hello, Client!")
        message = client_socket.recv(1024).decode('utf-8')
        print(f"Message from client: {message}")
        client_socket.close()

start_server()

def echo_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening...")
    
    while True:
        client_socket, address = server_socket.accept()
        print(f"Connected to {address}")
        data = client_socket.recv(1024)
        print(f"Received: {data.decode('utf-8')}")
        client_socket.sendall(data)  # Echo back the data
        client_socket.close()

echo_server()


def uppercase_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is running...")
    
    while True:
        client_socket, address = server_socket.accept()
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {data}")
        client_socket.sendall(data.upper().encode('utf-8'))  # Send uppercase response
        client_socket.close()

uppercase_server()

def reverse_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is running...")
    
    while True:
        client_socket, address = server_socket.accept()
        data = client_socket.recv(1024).decode('utf-8')
        print(f"Received: {data}")
        reversed_data = data[::-1]
        client_socket.sendall(reversed_data.encode('utf-8'))  # Send reversed message
        client_socket.close()

reverse_server()
