a = [1, 4, 7, 10, 13]
print(F"List a : {a} \n")

print("1. Akses list...")
print(F"element ke 3: {a[2]}")
print(F"element ke 2 sampai 4: {a[1:4]}")
print(F"element terakhir: {a[-1]} \n")

print("2. Ubah element list...")
a[3] = 11
print(F"Ubah element ke 4: {a}")
a[3:5] = [12, 15]
print(F"Ubah element ke 4 sampai element terakhir: {a} \n")

print("3. Tambah element list...")
b = a[0:2]
print(F"Ambil 2 bagian dari list a ke list b: {b}")
b.append("motor")
print(F"Tambah list b dengan nilai string: {b}")
b.extend([6, 9, 12])
print(F"Tambah list b dengan 3 nilai: {b}")
c = a + b
print(F"Gabungkan list a dan list b: {c} \n")