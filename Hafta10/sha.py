import hashlib

def sha_ailesi_analiz(mesaj):

   
    # Veriyi byte formatına çevir
    veri = mesaj.encode('utf-8')

    sha1 = hashlib.sha1(veri).hexdigest()
    print(f"Uzunluk    : 160 bit ({len(sha1)} karakter)"),
    print(f"karakter dizisi: {sha1[0]} ")
    print(f"karakter dizisi: {sha1[1]} ")
    print(f"karakter dizisi: {sha1[2]} ")
    print(f"karakter dizisi: {sha1[3]} ")
    print(f"karakter dizisi: {sha1[4]} ")
    print(f"karakter dizisi: {sha1[5]} ")
    print(f"karakter dizisi: {sha1[6]} ")
    print(f"karakter dizisi: {sha1[7]} ")
    print(f"karakter dizisi: {sha1[8]} ")
    print(f"karakter dizisi: {sha1[9]} ")
    print(f"karakter dizisi: {sha1[10]} ")
    print(f"Özet       : {sha1}")
    

    sha256 = hashlib.sha256(veri).hexdigest()
    print(f"Uzunluk    : 256 bit ({len(sha256)} karakter)")
    print(f"Özet       : {sha256}")
    
    sha512 = hashlib.sha512(veri).hexdigest()
    print(f"Uzunluk    : 512 bit ({len(sha512)} karakter)")
    print(f"Özet       : {sha512}")
    print("-" * 60)

sha_ailesi_analiz("Merhaba Konak")
sha_ailesi_analiz("Merhaba KOnak")