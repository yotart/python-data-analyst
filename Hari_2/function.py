def sapa():
    print("Hai yota")

sapa()

def sapa1(sapa):
    print(f"selamat datang {sapa}")

sapa1("di dunia")


def sapa2(x):
    print(f"siapkan seluruh kemampuan anda untuk {x}")

sapa2("menghadapi semua rintangan")

def sapa3(x=None):
    if x is None:
     print("anda harus memberikan alasan/tujuan")
    return

sapa3()

#date time
from datetime import datetime

now = datetime.now()
print(f"dimulai pada {now}")