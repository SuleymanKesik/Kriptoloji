# Öklid algoritması ile EBOB hesaplama
A = int(input("A değerini girin: "))
B = int(input("B değerini girin: "))
while A != B:
    if A > B:
        A = A - B
    else:
        B = B - A
print("EBOB:", A)