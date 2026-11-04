import os
def otp_sifrele(mesaj):
    metin_byte = mesaj.encode('utf-8')
    anahtar = os.urandom(len(metin_byte))
    sifreli_metin = bytes([c ^k for c,k in zip(metin_byte, anahtar)])
    return sifreli_metin, anahtar


def otp_desifreleme(sifreli_metin, anahtar):
    desifreli_metin = bytes([c ^ k for c, k in zip(sifreli_metin, anahtar)])
    return desifreli_metin.decode('utf-8')


def bayes_teoremi(olasilikDegeri):
    anahtar_uzayim = 256 # ==> 0-255
    olabilirlik = 1 / anahtar_uzayim

    toplam_kanit_olasilik = 1 / anahtar_uzayim
    sonsal_olasilik = (olabilirlik * olasilikDegeri) / toplam_kanit_olasilik
    return sonsal_olasilik

orj_mesaj = "Bu bir test mesajıdır."
print("Orijinal Mesaj:", orj_mesaj)

#şifreleme bloğu
sifreli_veri, uretilen_anahtar = otp_sifrele(orj_mesaj)
print(f"{sifreli_veri.hex()}")
print(f"{uretilen_anahtar.hex()}")
print("Desifrelenmis Mesaj:", otp_desifreleme(sifreli_veri, uretilen_anahtar))
baslangic_olasilik = 0.10
yeni_tahmin = bayes_teoremi(baslangic_olasilik)

print(f"{baslangic_olasilik} başlangıç olasılığı ile {yeni_tahmin} yeni tahmin elde edildi.")

if baslangic_olasilik == yeni_tahmin:
    print("Tahmin değişmedi.")