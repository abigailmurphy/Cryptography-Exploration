import sys
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def load_private_key(filename, password=None):
    with open(filename, "rb") as key_file:
        private_key = serialization.load_pem_private_key(
            key_file.read(),
            password=None,
           
        )
    return private_key

def decrypt_file(filename, private_key):
    with open(filename, "rb") as f:
        ciphertext = f.read()
    
    plaintext = private_key.decrypt(
        ciphertext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    print(plaintext.decode(), end='')
    


if __name__ == "__main__":

    filename = sys.argv[1]
    private_key = load_private_key("rsa-key.priv")
    decrypt_file(filename, private_key)
