def string_to_binary_blocks(message):
    # Metni 8 byte'lık (64 bit) bloklara böler ve binary formata çevirir
    return ["01010101..."] # Örnek 64-bit string listesi döner

def binary_to_string(binary_blocks):
    return "SifreliMetin"

def initial_permutation(block_64):
    return block_64 # 64-bit yer değiştirmiş blok döner

def split_into_two(block, length):
    return block[:length], block[length:]

def expand_to_48bit(right_32):
    return "0" * 48 # 32 biti 48 bite çıkaran E-Box işlemi

def xor_operation(bin1, bin2):
    return "".join(str(int(a) ^ int(b)) for a, b in zip(bin1, bin2))

def sbox_substitution(sonuc1_48bit):
    # 48 biti 6 bitlik 8 parçaya böler, S-Box'tan geçirip 4 bitlik 8 parça (32 bit) döner
    return "0" * 32 

def pbox_permutation(sonuc_32bit):
    return sonuc_32bit # 32-bit yer değiştirmiş P-Sonuc döner

def inverse_initial_permutation(block_64):
    return block_64 # IP^-1 işlemi

def pc1_drop_parity(key_64bit):
    return "0" * 56 # 64 bit anahtarı 56 bite düşürür (Parite bitleri atılır)

def shift_left(block_28bit, round_num):
    # Tur sayısına göre 1 veya 2 bit sola kaydırma yapar
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    s = shifts[round_num]
    return block_28bit[s:] + block_28bit[:s]

def pc2_compression(key_56bit):
    return "0" * 48 # 56 biti 48 bite düşürür


def BlokKeyFunc(key_64bit):
    round_keys = []
    
    # Adım 1, 2 ve 3: 64bitlik anahtarı 8'e böl, pariteleri at, 56 bit key ata.
    key_56bit = pc1_drop_parity(key_64bit)
    
    # Adım 4: 56bitlik keyi 28bit(sol) ve 28bit(sağ) olmak üzere iki bloğa ayır (A ve B)
    A_blok, B_blok = split_into_two(key_56bit, 28)
    
    # Adım 5: Tur bilgisini 0 olarak ata.
    tur = 0
    
    # Adım 8'deki kontrol: Tur bilgisi 16'dan küçük mü? Evet ise Adım 6'ya git (Döngü)
    while tur < 16:
        # Adım 6: 28bitlik A ve B bloklarını ayrı ayrı kaydırma işlemini gerçekleştir.
        A_blok = shift_left(A_blok, tur)
        B_blok = shift_left(B_blok, tur)
        
        # Adım 9: Kaydırılan A ve B bloklarını birleştir (Tekrar 56bitlik değer oluşuyor)
        birlesik_56bit = A_blok + B_blok
        
        # Adım 10: 56bitlik değer sıkıştırma tablosundan geçerek 48bite düşür.
        round_key_48bit = pc2_compression(birlesik_56bit)
        
        # Adım 11: Oluşan bloğu ana fonksiyona gönder (Burada listeye ekliyoruz)
        round_keys.append(round_key_48bit)
        
        # Adım 7: Tur bilgisini 1 artır.
        tur += 1
        
    return round_keys


def DES_Ana_Fonksiyon(mesaj, key_64bit):
    # Anahtar üretici fonksiyonu çağırıp 16 adet tur anahtarını alıyoruz
    tur_anahtarlari = BlokKeyFunc(key_64bit)
    
    # Adım 1: Mesajı al / gir ata publicMessage
    publicMessage = mesaj
    
    # Adım 2 & Adım 3: 8 bytelik karakter olarak ele al ve her 8 karakteri binary'e çevir
    binary_bloklar = string_to_binary_blocks(publicMessage)
    
    sifreli_bloklar = []
    
    # Adım 17: Tüm karakterlerin şifrelenmesi için döngü (Hayır ise Adım 3'e dön)
    for blok_64 in binary_bloklar:
        
        # Adım 4: İterasyon sayısını 0 olarak ata.
        iterasyon = 0
        
        # Adım 5: Adım 3'teki bilgileri permütasyon tablosuna göre dağıt.
        permute_blok = initial_permutation(blok_64)
        
        # Adım 6: Permutasyon tablosunu 32bit(sol) – 32bit(sağ) olarak 2 adet bloğa böl.
        sol_blok, sag_blok = split_into_two(permute_blok, 32)
        
        # Adım 16'daki kontrol (İterasyon sayısı 16'dan küçük mü?)
        # Not: Pseudo kodda "Evet ise Adım5'e git" yazılmış ancak DES mimarisinde iterasyon 
        # permütasyondan (Adım 5) değil, ayırma işleminden sonra (Adım 7) döngüye girer.
        while iterasyon < 16:
            # Geçici olarak mevcut sağ bloğu tutuyoruz (Adım 7 için)
            eski_sag_blok = sag_blok
            
            # Adım 8: Sağ bloğu genişlet (32'den 48 bite) ve ESonuc değişkenine ata
            ESonuc = expand_to_48bit(sag_blok)
            
            # Adım 9: KeyFunc'tan gelen bilgi ile ESonuc'u XOR'la, Sonuc1 ata
            mevcut_anahtar = tur_anahtarlari[iterasyon]
            Sonuc1 = xor_operation(ESonuc, mevcut_anahtar)
            
            # Adım 10 & Adım 11: Sonuc1'i 8 eş parçaya böl, SBox'lardan geçir, decimal yapıp birleştir
            sbox_sonucu = sbox_substitution(Sonuc1)
            
            # Adım 12: Yeni oluşan Sonuc[i]'leri birleştir ve PSonuc değişkenine ata (P-Box permütasyonu)
            PSonuc = pbox_permutation(sbox_sonucu)
            
            # Adım 13: Sonuc2 = PSonuc XOR Sol Blok
            Sonuc2 = xor_operation(PSonuc, sol_blok)
            
            # Adım 7 & Adım 14: Değişkenleri yeni tur için güncelle
            # Sağ bloğu bir sonraki iterasyonun Sol bloğu olarak ata (Adım 7)
            sol_blok = eski_sag_blok 
            # Sağ blok = Sonuc2 (Adım 14)
            sag_blok = Sonuc2
            
            # Adım 15: İterasyon sayısını 1 artır.
            iterasyon += 1
            
        # 16 tur bittikten sonra sol ve sağ bloğu birleştiriyoruz (Ters olarak birleşir)
        son_blok = sag_blok + sol_blok 
        
        # Adım 18: Adım 5'teki permütasyonun tersini alarak şifreli metini oluştur.
        sifreli_blok = inverse_initial_permutation(son_blok)
        sifreli_bloklar.append(sifreli_blok)
        
    return binary_to_string(sifreli_bloklar)


anahtar = "0101010101010101010101010101010101010101010101010101010101010101" # 64-bit rastgele key
mesaj = "KonakMYO35" # Şifrelenecek mesaj
sifreli_mesaj = DES_Ana_Fonksiyon(mesaj, anahtar)
print("Şifreli Mesaj:", sifreli_mesaj)