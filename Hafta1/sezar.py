def sezar_sifreli(gelen_metin, gelen_anahtar):
    alfabe = list("ABCÇDEFGĞHIİJKLMNOÖPRSŞTUÜVYZ")
    sifreli_alfabe = alfabe[gelen_anahtar:] + alfabe[:gelen_anahtar]
    gelen_metin = gelen_metin.upper()
    sifreli_metin = ""
    for karakter in gelen_metin:
        if karakter in alfabe:
            index = alfabe.index(karakter)
            sifreli_metin = sifreli_metin + sifreli_alfabe[index]
        else:
            sifreli_metin = sifreli_metin + karakter
    return sifreli_metin

##TODO: Şifrelenmiş olan sezar algoritmasının çözümünü öğrenci arkadaşlar gerçekleştirecektir.


metin = "Hello World!"
anahtar = 3
sifreli_metin = sezar_sifreli(metin, anahtar)
print(sifreli_metin)