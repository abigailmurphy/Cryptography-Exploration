import random
import math
import sys

def is_prime(num):
    if num < 2 :
        return False
    
    for i in range (2, num // 2 +1):
        if num % i == 0:
            return False
        
    return True 

def generate_secret_numbers(min_val, max_val):
    prime = random.randint(min_val, max_val)
    checkpoint = False
    while not is_prime(prime): 
        prime = random.randint(min_val, max_val)

    return prime

def mod_inverse(e, phi):
    for d in range(3, phi):
        if (d*e) % phi == 1:
            return d
        
    raise ValueError("mod invese does not exist")

def generate_public(phi_n):
    e = random.randint(3, phi_n -1)
    while math.gcd(e, phi_n) != 1:
        e = random.randint(3, phi_n -1)
    return e

def generate_private(e, phi_n):
    return mod_inverse(e, phi_n)
    
def encrypt(message, e, n):
    encoded = [ord(c) for c in message]
    ciphertext = [pow(c, e, n) for c in encoded]
    return ciphertext

def decrypt(cipher, d, n):
    encoded = [pow(c, d,n) for c in cipher]
    message = "".join(chr(c) for c in encoded)
    return message



def main(message):
    p = generate_secret_numbers(1000, 5000)
    q = generate_secret_numbers(1000, 5000)
    n = p * q
    phi_n = (p -1) * (q-1)

    public = generate_public(phi_n)
    private = generate_private(public, phi_n)


    ciphertext = encrypt(message, public, n)
    print(ciphertext)
    message2 = decrypt(ciphertext, private, n)
    print(message2)

if __name__ == "__main__":
    inputArgs = sys.argv
    message = ""

    for i in inputArgs[1:]:
        message = message + " " + i
    
    main(message)



    

    





