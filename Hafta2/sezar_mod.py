def sezar_sifreli(metin:str, anahtar:int):
    sifreli_metin = ""
    for karakter in metin:
        if karakter.isupper():
            sifreli_metin = sifreli_metin + chr((ord(karakter) - 65 + anahtar) % 26 + 65)
        elif karakter.islower():
            sifreli_metin = sifreli_metin + chr((ord(karakter) - 97 + anahtar) % 26 + 97)
        else:
            sifreli_metin = sifreli_metin + karakter
    return sifreli_metin


metin = "BERIL"
anahtar = 5
sifreli_metin = sezar_sifreli(metin, anahtar)
print(sifreli_metin)

sifresiz_metin = sezar_sifreli(sifreli_metin, -anahtar)
print(sifresiz_metin)