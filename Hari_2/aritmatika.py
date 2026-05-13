def add1(a,b):
    total = a + b

def add2(a,b):
    total = a + b
    return

def add(a = None,b = None):
    if a == None or b == None:
        print("parameter tidak lengkap")
        return
    total = a + b
    return total


def bmi(berat=None, tinggi=None):
    if berat==None or tinggi==None :
        print (f"Nilai yang kamu masukan tidak valid")
        return
    bmi = berat/(tinggi*tinggi)
    return bmi
    
def bmi_check(bmi):
    print(bmi)
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

