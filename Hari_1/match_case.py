hari = input("hari apa? ")

match hari:
    case "senin" | "selasa" | "rabu" :
        print("hari kerja awal")
    case "kamis" | "jumat" :
        print("hari kerja akhir")
    case "sabtu" | "minggu" :
        print("weekend")
    case _:
        print("hari tidak valid")


hari_angka = input("hari keberapa? ")

match hari_angka:
    case "1" | "2" | "3" :
        print("hari kerja awal")
    case "4" | "5" :
        print("hari kerja akhir")
    case "6" | "7" :
        print("weekend")
    case _:
        print("hari tidak valid")