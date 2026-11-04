# rsa_lab_demo.py
# -------------------------
# Bu dosya, klasik sayılar teorisi algoritmalarını ve RSA şifreleme sistemini
# öğretim amaçlı olarak Python'da uygulamalı şekilde göstermektedir.
# Fonksiyonların hepsi küçük ve eğitim amaçlıdır; gerçek dünyada güvenlik için
# büyük anahtar boyutları ve güvenli kütüphaneler kullanılmalıdır.

import random
from math import gcd

# 1) Euclid algoritması: gcd hesaplama
# Amaç: a ve b'nin en büyük ortak bölenini bulmak.
def euclid_with_steps(a, b):
    print(f"Euclid steps for gcd({a}, {b}):")
    step = 1
    while b != 0:
        q = a // b
        r = a % b
        print(f" Step {step}: {a} = {q}*{b} + {r}")
        a, b = b, r
        step += 1
    print(f" gcd = {a}\n")
    return a

# 2) Extended Euclid algoritması
# Amaç: gcd ile birlikte (x,y) katsayılarını da bulmak ki a*x + b*y = gcd.
# Bu, modüler ters hesaplamak için temel adımdır.
def extended_gcd(a, b):
    old_r, r = a, b
    old_s, s = 1, 0
    old_t, t = 0, 1
    while r != 0:
        q = old_r // r
        old_r, r = r, old_r - q * r
        old_s, s = s, old_s - q * s
        old_t, t = t, old_t - q * t
    return old_r, old_s, old_t  # gcd, x, y

# 3) Modüler ters fonksiyonu
# Amaç: b mod n için çarpma tersini bulmak (eğer gcd(b,n)=1 ise).
# RSA'da özel anahtar d'nin hesaplanmasında kullanılır.
def modinv(b, n):
    g, x, _ = extended_gcd(b, n)
    if g != 1:
        return None
    return x % n

# 4) Fermat küçük teoremi demosu
# Amaç: a^(p-1) mod p = 1 (p asal, gcd(a,p)=1 iken) özelliğini göstermek.
def fermat_demo(a, p):
    val = pow(a, p-1, p)
    print(f"Fermat demo: {a}^(p-1) mod {p} = {val}")

# 5) Miller–Rabin primality testi
# Amaç: büyük sayılar için olasılıksal asal testi yapmak.
def is_probable_prime(n, k=5):
    if n < 2:
        return False
    # küçük asal kontrolü
    for p in [2,3,5,7,11,13,17,19,23,29]:
        if n % p == 0:
            return n == p
    # n-1 = 2^s * d şeklinde yaz
    d = n - 1
    s = 0
    while d % 2 == 0:
        d //= 2
        s += 1
    def trial(a):
        x = pow(a, d, n)
        if x in (1, n-1):
            return True
        for _ in range(s-1):
            x = pow(x, 2, n)
            if x == n-1:
                return True
        return False
    for _ in range(k):
        a = random.randrange(2, n-1)
        if not trial(a):
            return False
    return True

# 6) RSA anahtar üretimi
# Amaç: p ve q asal sayılarını seçmek, n=pq, phi=(p-1)(q-1) hesaplamak,
# e seçmek, d = e^(-1) mod phi hesaplamak.
def generate_prime(bits=16):
    while True:
        cand = random.getrandbits(bits) | 1
        if is_probable_prime(cand):
            return cand

def rsa_keygen(bits=32):
    p = generate_prime(bits//2)
    q = generate_prime(bits//2)
    n = p * q
    phi = (p-1)*(q-1)
    e = 65537
    if gcd(e, phi) != 1:
        e = 3
        while gcd(e, phi) != 1:
            e += 2
    d = modinv(e, phi)
    return (n, e), (n, d)

# 7) RSA şifreleme / deşifreleme
# Amaç: m -> c = m^e mod n, c -> m = c^d mod n dönüşümlerini yapmak.
def rsa_encrypt(m, pub):
    n, e = pub
    return pow(m, e, n)

def rsa_decrypt(c, priv):
    n, d = priv
    return pow(c, d, n)

# 8) Küçük demo
if __name__ == "__main__":
    # Euclid gösterimi
    euclid_with_steps(240, 46)

    # Extended Euclid ve modinv gösterimi
    g, x, y = extended_gcd(3, 26)
    print(f"Extended gcd(3,26): gcd={g}, x={x}, y={y}")
    print("Inverse of 3 mod 26 =", modinv(3, 26))

    # Fermat demosu
    fermat_demo(2, 11)
    fermat_demo(3, 7)

    # Miller–Rabin testi
    print("Is 31 prime?", is_probable_prime(31))
    print("Is 561 prime?", is_probable_prime(561))  # Carmichael sayı

    # RSA demo
    pub, priv = rsa_keygen(32)  # küçük bit uzunluğu (öğretim amaçlı)
    print("Public key:", pub)
    print("Private key:", priv)
    m = 42
    c = rsa_encrypt(m, pub)
    m_rec = rsa_decrypt(c, priv)
    print(f"Message {m} -> Cipher {c} -> Decrypted {m_rec}")
