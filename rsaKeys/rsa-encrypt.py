import sys
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding


def load_public_key(filename):
    with open(filename, "rb") as key_file:
        public_key = serialization.load_pem_public_key(
            key_file.read(),
         
        )
    return public_key

def encrypt_file(filename, public_key):
    with open(filename, "rb") as f:
        plaintext = f.read()
    
    ciphertext = public_key.encrypt(
        plaintext,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    with open("encrypted.bin", "wb") as f:
        f.write(ciphertext)

if __name__ == "__main__":

    filename = sys.argv[1]
    public_key = load_public_key("rsa-key.pub")
    encrypt_file(filename, public_key)

