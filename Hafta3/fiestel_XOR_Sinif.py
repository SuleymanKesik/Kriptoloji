def F(Right, K_i):
    return (Right ^ K_i) & 0xFF # ^ ifadesi XOR operatörüdür. & 0xFF ifadesi ile sadece son 8 biti alıyoruz. Aynı bitler için 0, farklı bitler için 1 sonucunu üretir.
                          # & yani AND operatörüdür.


def AltAnahtar(UstAnahtar, i): # şifreleme key bilgisinin üretildiği fonksiyondur. Anahtarı basitçe kaydırıp tur sayısıyla XOR'luyoruz
    return ((UstAnahtar >> (i % 8)) ^ i) & 0xFF

def feistel_sifreleme(Public, ust_anahtar, tur_sayisi):
    #Feistel ağ yağısı şifreleme algoritmesıdır.
    #duz_metin: 16 bitlik düz metin (8 bitler ile rahat hareket edebilmek için 16 verildi)
    #ust_anahtar: 16 bitlik anahtar
    #tur_sayisi: tur (iterasyon) sayısı

    Left = (Public >> 8) & 0xFF  # Sol yarı (ilk 8 bit)
    #Public >> 8 --> Sağa kaydırma işlemi ile Public'in ilk 8 bitini elde ediyoruz.
    #& 0xFF --> AND operatörü ile sadece son 8 biti alıyoruz. Bu sayede sol yarıyı elde ediyoruz.
    Right = Public & 0xFF         # Sağ yarı (son 8 bit)

    #print(Left)
    #print(Right)

    print(f"Başlangıç : Left0 = {bin(Left)[2:].zfill(8)}, Right0 = {bin(Right)[2:].zfill(8)}")

    for i in range(1, tur_sayisi + 1):
        K_i = AltAnahtar(ust_anahtar, i) #i'inci alt anahtarı al
    
        Left_yeni = Right
        Right_yeni = Left ^ F(Right, K_i)

        Left = Left_yeni
        Right = Right_yeni
        print(f"Tur {i:2}    : Left{i} = {bin(Left)[2:].zfill(8)}, Right{i} = {bin(Right)[2:].zfill(8)}, K{i} = {bin(K_i)[2:].zfill(8)}")




if __name__ == "__main__":
    duz_metin = 0b0100100001100101 # Örnek 16 bitlik Düz Metin (Public) -> Örn: 0b0100100001100101 (H=72, E=101)
    ust_anahtar = 0b1010110001110011 # Örnek 16 bitlik Üst Anahtar
    tur_sayisi = 4 # Tur sayısı (T)
    
    # bin () fonksiyonu, bir sayıyı ikili (binary) biçimde temsil eden bir dize (string) döndürür.
    # zfill(8) metodu, bu ikili dizeyi 8 karakter uzunluğuna tamamlar. Eğer ikili dize 8 karakterden kısa ise, başına gerekli sayıda '0' ekler.
    # f-string formatlama yöntemi ile, Left ve Right değerlerini ikili biçimde ve 8 bitlik uzunlukta ekrana yazdırıyoruz.
    print(f"Orijinal Metin (16 bit): {bin(duz_metin)[2:].zfill(16)}\n")
    
    sifreli_metin = feistel_sifreleme(duz_metin, ust_anahtar, tur_sayisi)