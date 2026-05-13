hitung = -10

while hitung <= 10:
    print("perulangan ke ", hitung)
    hitung +=1 # hitung (variabel baru) = hitung (variabel lama) + 1

nilai = int(input("nilai (0-100): "))
while nilai < 0 or nilai > 100:
    print("nilai tidak valid")
    nilai = int(input("coba lagi: "))

