
def sezar_brute_force():
    chipher_text = input("Şifreli metni giriniz: ")
    key = 1

    for key in range(1, 26): ##range 1'den başladı key numarasıyla aynı / benzer / birliktelik
        cozulmus_metin = ""

        for char in chipher_text:
            if char.isalpha():
                if char.isupper():
                    taban = ord('A')
                    cozulmus_metin += chr((ord(char) - taban - key) % 26 + taban)
                    #cozulmus_metin = cozulmus_metin +chr((ord(char) - taban - key) % 26 + taban)
                else:
                    taban = ord('a')
                    cozulmus_metin += chr((ord(char) - taban - key) % 26 + taban)
                
            else:
                cozulmus_metin += char
        print(f"Key {key}: {cozulmus_metin}")

if __name__ == "__main__":
    sezar_brute_force()