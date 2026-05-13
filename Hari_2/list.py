nama = ["yota", "heri", "tama", "budi", "santoso"]
nilai = [80, 90, 90, 85, 80]

print(nama)
print("\n")
print(nama[1],nama[3],nama[4])
print(f"Nama {nama[1]} mendapatkan nilai sebesar {nilai[1]}")
print("\n")
for x in range(5):
    print(f"Nama {nama[1]} mendapatkan nilai sebesar {nilai[1]}")
print("\n")
for y in range(5):
    print(f"Nama {nama[y]} mendapatkan nilai sebesar {nilai[y]}")
print("\n")
for z in range(len(nama)):
    print(f"Nama {nama[z]} mendapatkan nilai sebesar {nilai[z]}")

print(nama[-1])
print(nama[-2])

print(nama[1:3])

nama[1] = "Herii"
print(nama)

nama.insert(0, "yoga")
print(nama)

nama.append("purwanto")
print(nama)

nama.sort()
print(nama)

nama.pop(-1)
print(nama)

nama.reverse()
print(nama)

nama.remove("Herii")
print(nama)

nama.insert(2,"heri")
print(nama)