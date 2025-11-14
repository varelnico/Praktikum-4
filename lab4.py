print("Nama : Varel Nico Ramadhan")
print("NIM : 312510156")
print()
print("-TUGAS PERULANGAN-")
print()
# Siapkan list kosong untuk menampung data
data_mahasiswa = []

while True:
    # Meminta input data dari pengguna
    nama = input("Nama Mahasiswa : ")
    nim = input("NIM Mahasiswa  : ")
    
    try:
        nilai_tugas = float(input("Nilai Tugas    : "))
        nilai_uts = float(input("Nilai UTS      : "))
        nilai_uas = float(input("Nilai UAS      : "))
    except ValueError:
        print("\nERROR: Nilai harus berupa angka. Silakan ulangi.")
        continue # Mengulangi loop dari awal

    # 2. Menghitung Nilai Akhir sesuai bobot (Tugas: 30%, UTS: 35%, UAS: 35%)
    nilai_akhir = (0.30 * nilai_tugas) + (0.35 * nilai_uts) + (0.35 * nilai_uas)

    # 3. munculkan data hasil
    data_entry = {
        'nama': nama,
        'nim' : nim,
        'tugas': nilai_tugas,
        'uts': nilai_uts,
        'uas': nilai_uas,
        'nilai_akhir': nilai_akhir
    }

    # 4. Tambahkan dictionary data ke dalam list utama
    data_mahasiswa.append(data_entry)

    # 5. Tampilkan pertanyaan untuk menambah data lagi
    print("---------------------------------")
    tambah_lagi = input("Tambah data lagi (y/t)? ")
    
    # Jika jawaban 't' (atau 'T'), hentikan perulangan
    if tambah_lagi.lower() == 't':
        break

# Setelah perulangan selesai, tampilkan semua data
print("\n=========================================")
print("       Daftar Nilai Mahasiswa")
print("=========================================")

if not data_mahasiswa:
    # Jika list kosong
    print("Tidak ada data untuk ditampilkan.")
else:
    # Tampilkan data satu per satu
    for i, data in enumerate(data_mahasiswa):
        print(f"\nData ke-{i + 1}")
        print(f"  Nama        : {data['nama']}")
        print(f"  NIM         : {data['nim']}")
        print(f"  Nilai Tugas : {data['tugas']}")
        print(f"  Nilai UTS   : {data['uts']}")
        print(f"  Nilai UAS   : {data['uas']}")
        # Tampilkan nilai akhir dengan 2 angka di belakang koma
        print(f"  Nilai Akhir : {data['nilai_akhir']:.2f}")

print("\n=========================================")
print("Program selesai.")
