def ksa(anahtar): #Key Scheduling Algorithm
    anahtar_uzunlugu = len(anahtar)
    S = list(range(256))  # ==> 0-255 arası değerler için

    j=0
    for i in range(256):
        j = (j + S[i] + (anahtar[i % anahtar_uzunlugu])) % 256
        S[i], S[j] = S[j], S[i]
    return S

def prga(S, mesaj_uzunlugu): #Pseudo-Random Generation Algorithm
    i =0
    j=0
    anahtar_akisi = []
    for _ in range(mesaj_uzunlugu):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        K = S[(S[i] + S[j]) % 256]
        anahtar_akisi.append(K)
    return anahtar_akisi


def rc4_sifrele_desifrele(mesaj, anahtar):
    anahtar = [ord(c) for c in anahtar]
    S = ksa(anahtar) #S vektörünü oluşturuyoruz
    anahtar_akisi = prga (S, len(mesaj)) #PRGA ile anahtar akışını oluşturuyoruz
    sonuc = bytearray()
    for v, k in zip(mesaj, anahtar_akisi):
        sonuc.append(v ^ k) #XOR işlemi ile şifreleme/desifreleme
    return bytes(sonuc)


orj_mesaj = "Bu bir test mesajıdır."
anahtar = "gizli"

print("Orijinal Mesaj:", orj_mesaj)
print("Anahtar:", anahtar)

orjinal_mesaj_bytes = orj_mesaj.encode('utf-8')
sifreli_byte = rc4_sifrele_desifrele(orjinal_mesaj_bytes, anahtar)
print("Şifreli Mesaj (Hex):", sifreli_byte.hex())

cozulmus_bytes = rc4_sifrele_desifrele(sifreli_byte, anahtar)
print("Çözülmüş Mesaj (Bytes):", cozulmus_bytes)
cozulmus_mesaj = cozulmus_bytes.decode('utf-8')
print("Çözülmüş Mesaj:", cozulmus_mesaj)