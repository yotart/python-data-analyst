berat = float(input("Masukan Berat Badan (kg) : "))
tinggi = float(input("Masukan Tinggi Badan (cm) : "))

bmi = berat/(tinggi*tinggi)
print("Nilai BMI kamu adalah", bmi)

if bmi < 18.5:
    print ("Berat Badan Kurang")
elif bmi <= 22.9:
    print ("Normal/Ideal")
elif bmi <= 24.9:
    print ("Berat badan berlebih")
elif bmi <= 29.9:
    print ("Obesitas Tingkat 1")
else:
    print ("Obesitas Tingkat 2")