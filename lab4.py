print("Nama : Varel Nico Ramadhan")
print("NIM : 312510156")
print()
print("-TUGAS PERULANGAN-")
print()
print("=== Program Nilai Mahasiswa ===")
print()
# Siapkan list kosong untuk menampung data

data_mahasiswa = []

while True:
    nama = input("Nama Mahasiswa : ")
    nim = input("NIM Mahasiswa  : ")
    tugas = float(input("Nilai Tugas    : "))
    uts = float(input("Nilai UTS      : "))
    uas = float(input("Nilai UAS      : "))

    nilai_akhir = (tugas * 0.30) + (uts * 0.35) + (uas * 0.35)

    # Simpan sebagai list biasa
    data_mahasiswa.append([nama, nim, tugas, uts, uas, nilai_akhir])

    lanjut = input("Tambah data lagi (y/t)? ")
    if lanjut.lower() == "t":
        break

print("\n=== Daftar Nilai ===")

i = 1
for mhs in data_mahasiswa:
    print(f"\nData ke-{i}")
    print("Nama        :", mhs[0])
    print("NIM         :", mhs[1])
    print("Nilai Tugas :", mhs[2])
    print("Nilai UTS   :", mhs[3])
    print("Nilai UAS   :", mhs[4])
    print("Nilai Akhir :", round(mhs[5], 2))
    i += 1
