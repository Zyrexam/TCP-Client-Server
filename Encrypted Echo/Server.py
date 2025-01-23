import socket
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Load keys
def load_key(file_path):
    with open(file_path, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(), password=None
        ) if "private" in file_path else serialization.load_pem_public_key(key_file.read())

server_private_key = load_key("keys/server_private.pem")
client_public_key = load_key("keys/client_public.pem")

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(1)
    print("Server is listening...")

    while True:
        client_socket, address = server_socket.accept()
        print(f"Connection established with {address}")
        
        # Receive encrypted message
        encrypted_message = client_socket.recv(1024)
        print(f"Encrypted message from client: {encrypted_message}")

        # Decrypt the message using server's private key
        message = server_private_key.decrypt(
            encrypted_message,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        print(f"Decrypted message: {message.decode('utf-8')}")

        # Encrypt the echoed message using client's public key
        encrypted_response = client_public_key.encrypt(
            message,
            padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
        )
        client_socket.sendall(encrypted_response)
        client_socket.close()

start_server()
