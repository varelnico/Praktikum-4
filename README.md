# Praktikum-4
 
---

# **Penjelasan / Langkah-langkah Program**

## **1. Tampilkan identitas dan judul program**

Program menampilkan informasi awal:

* Nama
* NIM
* Judul tugas

Dengan menggunakan `print()`.

---

## **2. Siapkan list kosong untuk menyimpan banyak data mahasiswa**

```python
data_mahasiswa = []
```

List ini digunakan untuk menampung setiap data mahasiswa yang dimasukkan.

---

## **3. Mulai perulangan untuk input data (while True)**

Program masuk ke loop **selama pengguna masih ingin menginput data**.

---

## **4. Minta pengguna memasukkan data mahasiswa**

Program meminta:

* Nama mahasiswa
* NIM
* Nilai Tugas
* Nilai UTS
* Nilai UAS

Nilai dibuat `float()` karena berbentuk angka desimal.

---

## **5. Hitung nilai akhir berdasarkan bobot**

Rumus:

* Tugas = 30%
* UTS = 35%
* UAS = 35%

Output disimpan sebagai `nilai_akhir`.

---

## **6. Simpan semua data ke dalam dictionary**

Data mahasiswa dimasukkan ke:

```python
data_entry = { 'nama': ..., 'nim': ..., dst }
```

Lalu ditambahkan ke list utama:

```python
data_mahasiswa.append(data_entry)
```

---

## **7. Tanyakan apakah ingin menambah data lagi**

Program menampilkan:

```
Tambah data lagi (y/t)?
```

Jika user memasukkan `t` → perulangan berhenti.
Jika `y` → kembali ke atas dan input data baru lagi.

---

## **8. Setelah loop selesai, tampilkan tabel data mahasiswa**

program menampilkan setiap mahasiswa lengkap dengan:

* Nama
* NIM
* Nilai Tugas
* Nilai UTS
* Nilai UAS
* Nilai Akhir (2 angka di belakang koma)

---

## **9. Tampilkan pesan akhir**

Program menutup dengan:

```
Program selesai.
```

---

