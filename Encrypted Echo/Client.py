import socket
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes

# Load keys
def load_key(file_path):
    with open(file_path, "rb") as key_file:
        return serialization.load_pem_private_key(
            key_file.read(), password=None
        ) if "private" in file_path else serialization.load_pem_public_key(key_file.read())

client_private_key = load_key("keys/client_private.pem")
server_public_key = load_key("keys/server_public.pem")

def start_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 12345))

    # Message to send
    message = "Hello, Secure Server!"
    print(f"Original message: {message}")

    # Encrypt the message using the server's public key
    encrypted_message = server_public_key.encrypt(
        message.encode('utf-8'),
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    print("\n")
    print(f"Encrypted message: {encrypted_message}")

    # Send the encrypted message
    client_socket.sendall(encrypted_message)

    # Receive and decrypt the response
    encrypted_response = client_socket.recv(1024)
    print(f"Encrypted response from server: {encrypted_response}")

    # Decrypt the response using the client's private key
    decrypted_response = client_private_key.decrypt(
        encrypted_response,
        padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(), label=None)
    )
    print("\n")
    # Print the decrypted response as a string
    print(f"Decrypted response: {decrypted_response.decode('utf-8')}")
    client_socket.close()

start_client()
