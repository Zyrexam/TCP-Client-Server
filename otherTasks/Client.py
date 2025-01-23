import socket

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    print(client_socket.recv(1024).decode('utf-8'))
    client_socket.sendall(b"Hello, Server!")
    client_socket.close()


start_client()


def echo_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    message = "Hello, Server!"
    client_socket.sendall(message.encode('utf-8'))
    response = client_socket.recv(1024)
    print(f"Echoed from server: {response.decode('utf-8')}")
    client_socket.close()

echo_client()


def uppercase_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    message = "hello server"
    client_socket.sendall(message.encode('utf-8'))
    response = client_socket.recv(1024)
    print(f"Response from server: {response.decode('utf-8')}")
    client_socket.close()

uppercase_client()

def reverse_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))
    message = "hello server"
    client_socket.sendall(message.encode('utf-8'))
    response = client_socket.recv(1024)
    print(f"Reversed message: {response.decode('utf-8')}")
    client_socket.close()

reverse_client()
