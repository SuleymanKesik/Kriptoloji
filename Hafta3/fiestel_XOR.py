from django.db.models.sql import AND

def F(R, K): #temsili bir F fonksiyonu (dokümandaki genişleme yani E fonksiyonu, yer değiştirme yani S-Box, permütasyon vb. diyebiliriz)
    return (R ^ K) & 0xFF # ^ ifadesi XOR operatörüdür. & 0xFF ifadesi ile sadece son 8 biti alıyoruz. Aynı bitler için 0, farklı bitler için 1 sonucunu üretir.
                          # & yani AND operatörüdür. 
    
def AltAnahtar(UstAnahtar, i): # şifreleme key bilgisinin üretildiği fonksiyondur. Anahtarı basitçe kaydırıp tur sayısıyla XOR'luyoruz
    return ((UstAnahtar >> (i % 8)) ^ i) & 0xFF

def feistel_sifreleme(Public, UstAnahtar, T): #Asıl fonksiyon burası...
    #    Feistel Ağ Yapısı Şifreleme Algoritması
    #    Public: 16 bitlik Düz Metin (8 bitler ile rahat hareket edebilmek için 16 verildi)
    #    UstAnahtar: 16 bitlik Anahtar 
    #    T: Tur (İterasyon) Sayısı

    # Adım 3: Public bloğunu ikiye böl (16 biti 8'er bitlik iki parçaya ayırıyoruz)
    # 0xFF (255) maskesi ile sadece son 8 biti almayı garantiliyoruz.
    Left = (Public >> 8) & 0xFF  # Sol yarı (ilk 8 bit) >> yada << ifadeleri shifting yani kaydırma işlemi yapar. >> sağa kaydırır, << sola kaydırır.
                         # AND operatörü kullanılarak fazlalık bitlerin kırpılması ve tam olarak 8 bitlik (1 byte) verilerin garantiye alınması sağlanır.
    Right = Public & 0xFF         # Sağ yarı (son 8 bit)

# 10101100 01010011 (Public)

#   00000000 10101100  (Kaydırılmış Public)
# & 00000000 11111111  (0xFF Maskesi)
#   00000000 10101100  -> Sol Yarı (Left) = 10101100       
    
#   10101100 01010011  (Public)
# & 00000000 11111111  (0xFF Maskesi)
#   00000000 01010011  -> Sağ Yarı (Right) = 01010011

    
    print(f"Başlangıç : Left0 = {bin(Left)[2:].zfill(8)}, Right0 = {bin(Right)[2:].zfill(8)}")
    
    # Adım 4 ve 5: i = 1'den T'ye kadar döngü (T dahil)
    for i in range(1, T + 1):
        # Adım 5.1: i'inci alt anahtarı al
        K_i = AltAnahtar(UstAnahtar, i)
        
        # Adım 5.2 ve 5.3: Geçici değişkenlerle (veya çapraz atamayla) yeni değerleri hesapla
        Left_yeni = Right
        # F fonksiyonundan çıkan sonuç ile bir önceki turun sol yarısı XOR'lanır (^)
        Right_yeni = Left ^ F(Right, K_i)
        
        # Değerleri bir sonraki tur için güncelle
        Left = Left_yeni
        Right = Right_yeni
        
        print(f"Tur {i:2}    : Left{i} = {bin(Left)[2:].zfill(8)}, Right{i} = {bin(Right)[2:].zfill(8)}, K{i} = {bin(K_i)[2:].zfill(8)}")
        
    # Adım 6: Döngü bitince şifreli blok C = birleştir(RT, LT)
    # Feistel şemalarında son çıkış ters sırada alınır. RT'yi 8 bit sola kaydırıp LT ile birleştiriyoruz.
    Cipher = (Right << 8) | Left
    
    # Adım 7: C'yi çıktı olarak ver
    return Cipher

# --- Adım 1 ve 8: Başla ve Dur ---
if __name__ == "__main__":
    duz_metin = 0b0100100001100101 # Örnek 16 bitlik Düz Metin (P) -> Örn: 0b0100100001100101 (H=72, E=101)
    ust_anahtar = 0b1010110001110011 # Örnek 16 bitlik Üst Anahtar
    tur_sayisi = 4 # Tur sayısı (T)

    # bin () fonksiyonu, bir sayıyı ikili (binary) biçimde temsil eden bir dize (string) döndürür.
    # zfill(8) metodu, bu ikili dizeyi 8 karakter uzunluğuna tamamlar. Eğer ikili dize 8 karakterden kısa ise, başına gerekli sayıda '0' ekler.
    # f-string formatlama yöntemi ile, Left ve Right değerlerini ikili biçimde ve 8 bitlik uzunlukta ekrana yazdırıyoruz.
    print(f"Orijinal Metin (16 bit): {bin(duz_metin)[2:].zfill(16)}\n")
    
    sifreli_metin = feistel_sifreleme(duz_metin, ust_anahtar, tur_sayisi)
    
    print(f"\nŞifreli Metin  (16 bit): {bin(sifreli_metin)[2:].zfill(16)}")