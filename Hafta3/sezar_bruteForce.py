def sezar_brute_force():
    # Adım 2: Şifreli metni (CipherText) gir.
    cipher_text = input("Şifreli metni giriniz: ")
    
    # Adım 3 ve 4: Anahtar değerini 1 olarak ata ve 25'e kadar (25 dahil) döngüye sok.
    for key in range(1, 26):
        # Adım 4.1: Boş bir “ÇözülmüşMetin” (DecryptedText) oluştur.
        decrypted_text = ""
        
        # Adım 4.2: Her bir karakter için işlemleri yap
        for char in cipher_text:
            # Karakter harf mi?
            if char.isalpha():
                # a) Eğer büyük harfse taban = 'A', küçükse taban = 'a'
                if char.isupper():
                    taban = ord('A')
                else:
                    taban = ord('a')
                
                # b) Harfi, (ASCII - taban - anahtar) mod 26 + taban formülüne göre çöz
                # ord(): Karakterin ASCII değerini verir. chr(): ASCII değerini karaktere çevirir.
                cozulmus_harf_ascii = (ord(char) - taban - key) % 26 + taban
                
                # c) Çözülmüş harfi “ÇözülmüşMetin”e ekle
                decrypted_text += chr(cozulmus_harf_ascii)
            else:
                # Hayır ise: Karakteri aynen “ÇözülmüşMetin”e ekle (Boşluk, sayı veya noktalama işaretleri)
                decrypted_text += char
                
        # Adım 4.3: Anahtar ve “ÇözülmüşMetin”i ekrana yaz
        print(f"Anahtar {key:2}: {decrypted_text}")

# Adım 1 ve Adım 6: Programı başlat ve bitir
if __name__ == "__main__":
    sezar_brute_force()