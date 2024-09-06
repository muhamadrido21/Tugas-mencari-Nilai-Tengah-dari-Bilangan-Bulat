a = int(input("pertama: "))
b = int(input("kedua: "))
c = int(input("ketiga: "))


if (a > b and a < c) or (a < b and a > c):
    print("Nilai Tengah", a)

elif (b > a and b < c) or (b < a and b > c):
    print("Nilai Tengah", b)

else:
    print("Nilai Tengah", c)