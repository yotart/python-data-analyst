import aritmatika as a

BB = float(input("Masukan Berat badan (Kg): "))
TB = float(input("Masukan Tinggi Badan (m): "))

bmi = a.bmi(BB, TB)
print("BMI kamu adalah", bmi)
a.bmi_check(bmi)