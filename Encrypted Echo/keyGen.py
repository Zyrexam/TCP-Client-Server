import os
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization

def generate_key_pair():
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()
    return private_key, public_key

def save_keys(private_key, public_key, private_file, public_file):

    if not os.path.exists("keys"):
        os.makedirs("keys")

    with open(private_file, "wb") as priv_file:
        priv_file.write(
            private_key.private_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PrivateFormat.TraditionalOpenSSL,
                encryption_algorithm=serialization.NoEncryption()
            )
        )


    with open(public_file, "wb") as pub_file:
        pub_file.write(
            public_key.public_bytes(
                encoding=serialization.Encoding.PEM,
                format=serialization.PublicFormat.SubjectPublicKeyInfo
            )
        )


server_private, server_public = generate_key_pair()
save_keys(server_private, server_public, "keys/server_private.pem", "keys/server_public.pem")


client_private, client_public = generate_key_pair()
save_keys(client_private, client_public, "keys/client_private.pem", "keys/client_public.pem")

