import random
from math import gcd

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if ____ % ____ == 0:
            return False
    return True

def generate_prime(start=50, end=100):
    while True:
        p = random.randint(start, end)
        if ____:
            return p

def modinv(a, m):
    # Inverse modulaire via l'algorithme d’Euclide étendu
    for x in range(1, m):
        if (a * x) % m == ____:
            return x
    return None

# Choisir deux nombres premiers p et q
p = generate_prime()
q = generate_prime()

n = p * q
phi = (p - 1) * (q - 1)

# Choisir e tel que 1 < e < phi et gcd(e, phi) == 1
e = 3
while gcd(e, phi) != 1:
    e += 2

# Calculer la clé privée d
d = modinv(e, phi)

print("Clé publique : (e =", e, ", n =", n, ")")
print("Clé privée : (d =", ____, ", n =", n, ")")





# Chiffrement

def chiffrement(message, e, n):
    chiffre = [pow(ord(car), ____, ____ ) for car in message]
    return chiffre

message = "HELLO"
chiffre = chiffrement(message, e, n)
print("Message chiffré :", chiffre)






# Déchiffrement

def dechiffrement(chiffre, d, n):
    clair = [chr(pow(car, ____, ____)) for car in chiffre]
    return ''.join(clair)

clair = dechiffrement(chiffre, d, n)
print("Message déchiffré :", clair)




