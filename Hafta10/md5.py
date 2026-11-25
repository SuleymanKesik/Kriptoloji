import hashlib

#Aşağıda binary karşılığı var#
metin1 = hashlib.md5(b'KONAK') #--> Burada b karakterini KAVRAM yazısının byte karşılığını yazabilmek için ele alıyoruz
print("Metin1")
print(metin1.digest()) #--> digest komutu Hash sonucunu binary (ikili) formatta


#Aşağıda hexidecimal karşılığı var#
metin2 = "KONAK"
result = hashlib.md5(metin2.encode()) #--> Burada metin2 değeri bir string olduğu için encode ile binary yapıyoruz
print("Metin2")
print(result.hexdigest()) #--> hexdigest komutu Hash sonucunu hexadecimal (onaltılık) formatta döndürür