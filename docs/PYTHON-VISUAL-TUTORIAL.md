# Tutorial Python Visual untuk Pemula: Dasar hingga Analisis Data

**Prasyarat:** tidak perlu pengalaman pemrograman.  
**Lingkungan:** Python 3.11 atau lebih baru pada komputer; Pydroid 3/Termux dapat digunakan untuk latihan tertentu di Android.  
**Catatan:** contoh utama adalah Python desktop. Kode MicroPython untuk ESP32 diberi label terpisah.

## Cara memakai tutorial

Untuk setiap bab: pahami masalah → baca blok → susun algoritma → prediksi output → ketik kode → jalankan → ubah nilai → kerjakan latihan. Jangan hanya menyalin.

## Bab 1. Program dan output

**Cerita:** komputer perlu diberi instruksi yang jelas untuk menampilkan pesan.

**Visual block**
```text
[MULAI] → [OUTPUT: Halo!] → [SELESAI]
```

**Kode**
```python
print("Halo!")
```

**Bedah kode:** `print` adalah perintah untuk menampilkan informasi. Tanda kurung berisi hal yang ditampilkan. Tanda kutip menandai teks.

**Prediksi:** apa yang tampil jika teks diubah menjadi "Belajar Python"?

**Latihan:** tampilkan nama, program studi, dan tujuan belajar pada tiga baris.

## Bab 2. Variabel: tempat menyimpan nilai

**Cerita:** kita perlu menyimpan suhu sensor agar bisa digunakan lagi.

**Visual block**
```text
[INPUT/NILAI: 28.5] → [SIMPAN ke variabel suhu] → [OUTPUT suhu]
```

**Kode**
```python
suhu = 28.5
print(suhu)
```

Variabel adalah nama untuk mengakses suatu nilai. Tanda `=` berarti memberi/menetapkan nilai, bukan membandingkan dua nilai.

**Latihan:** buat variabel `kelembapan = 70` dan tampilkan nilainya.

## Bab 3. Tipe data

**Visual block**
```text
[Nilai 25.5] → [tipe angka desimal: float]
[Nilai 25]   → [tipe bilangan bulat: int]
[Nilai "ESP32"] → [tipe teks: str]
[Nilai True] → [tipe benar/salah: bool]
```

**Kode**
```python
suhu = 25.5
jumlah = 3
nama_perangkat = "ESP32"
terhubung = True

print(type(suhu))
print(type(jumlah))
print(type(nama_perangkat))
print(type(terhubung))
```

Gunakan `type()` untuk memeriksa jenis nilai. Perhatikan bahwa `"25"` adalah teks, sedangkan `25` adalah angka.

**Latihan:** simpan nama sensor, jumlah pembacaan, nilai tegangan, dan status aktif dalam tipe yang sesuai.

## Bab 4. Input pengguna

**Visual block**
```text
[MULAI] → [INPUT: nama] → [SIMPAN nama] → [OUTPUT: salam] → [SELESAI]
```

**Kode**
```python
nama = input("Masukkan nama: ")
print("Halo,", nama)
```

`input()` membaca masukan keyboard dan menghasilkan teks (`str`). Jika ingin angka, ubah secara eksplisit.

```python
umur = int(input("Masukkan umur: "))
print(umur + 1)
```

**Kesalahan umum:** memasukkan teks saat program mengharapkan angka akan menyebabkan `ValueError`. Validasi input akan dipelajari pada bab error.

## Bab 5. Operator matematika dan perbandingan

**Visual block**
```text
[angka A] + [angka B] → [PROSES penjumlahan] → [OUTPUT hasil]
[nilai suhu] > [35] → [KEPUTUSAN benar/salah]
```

**Kode**
```python
a = 10
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a > b)
```

Operator matematika: `+`, `-`, `*`, `/`, `//`, `%`, `**`. Operator perbandingan: `>`, `<`, `>=`, `<=`, `==`, `!=`.

## Bab 6. Keputusan if, elif, else

**Masalah:** klasifikasikan suhu.

**Visual block**
```text
[INPUT suhu] → ◇ suhu >= 40? ◇
 YA → [status BAHAYA]
 TIDAK → ◇ suhu >= 35? ◇
          YA → [status WASPADA]
          TIDAK → [status NORMAL]
 → [OUTPUT status]
```

**Kode**
```python
suhu = 37.2

if suhu >= 40:
    status = "BAHAYA"
elif suhu >= 35:
    status = "WASPADA"
else:
    status = "NORMAL"

print(status)
```

Indentasi (spasi di awal baris) menandai blok instruksi. Uji nilai 34.9, 35.0, 39.9, dan 40.0.

## Bab 7. Perulangan for

**Visual block**
```text
[angka mulai 1] → [SELAMA angka <= 5]
       ↑                 ↓ YA
       └── [angka + 1] ← [OUTPUT angka]
                         ↓ TIDAK
                      [SELESAI]
```

**Kode**
```python
for angka in range(1, 6):
    print(angka)
```

`range(1, 6)` menghasilkan 1 sampai 5. Batas akhir 6 tidak ikut dimasukkan.

## Bab 8. Perulangan while

```python
hitung = 1
while hitung <= 3:
    print(hitung)
    hitung += 1
```

Perulangan berjalan selama kondisi benar. Jika nilai `hitung` tidak pernah berubah, program dapat berulang tanpa akhir. Selalu pastikan ada kondisi berhenti.

## Bab 9. List

**Analogi:** daftar beberapa pembacaan sensor.

```python
suhu = [28.1, 29.0, 30.2]
print(suhu[0])
suhu.append(31.0)
print(suhu)
```

Indeks list dimulai dari 0. `append` menambahkan item ke akhir.

## Bab 10. Dictionary

Dictionary menyimpan pasangan kunci dan nilai.

```python
sensor = {
    "id": "ESP32-01",
    "suhu": 28.5,
    "online": True
}
print(sensor["suhu"])
```

Cocok untuk merepresentasikan satu paket data sensor dengan nama field.

## Bab 11. Fungsi

**Visual block**
```text
[INPUT nilai suhu] → [PANGGIL fungsi klasifikasi]
                         ↓
                  [PROSES kondisi]
                         ↓
                  [KEMBALIKAN status]
```

```python
def klasifikasi_suhu(suhu):
    if suhu >= 40:
        return "BAHAYA"
    if suhu >= 35:
        return "WASPADA"
    return "NORMAL"

print(klasifikasi_suhu(37.2))
```

Fungsi adalah kumpulan instruksi bernama. Parameter menerima data; `return` mengirim hasil kembali ke pemanggil.

## Bab 12. Menangani kesalahan input

```python
try:
    suhu = float(input("Suhu: "))
    print(f"Suhu: {suhu:.1f} C")
except ValueError:
    print("Masukkan angka yang valid.")
```

`try` menjalankan kode yang mungkin gagal. `except` menangani jenis kesalahan tertentu. Jangan menutupi semua error dengan `except:` kosong.

## Bab 13. Membaca file teks dan CSV

```python
with open("catatan.txt", "w", encoding="utf-8") as file:
    file.write("Belajar Python\n")
```

Mode `w` menulis dan dapat mengganti isi file lama. Gunakan mode `a` untuk menambahkan. Untuk CSV:

```python
import csv

with open("sensor.csv", newline="", encoding="utf-8") as file:
    pembaca = csv.DictReader(file)
    for baris in pembaca:
        print(baris)
```

## Bab 14. JSON

JSON adalah format teks untuk bertukar data terstruktur.

```python
import json

data = {"device": "ESP32-01", "temperature": 28.5}
teks = json.dumps(data)
print(teks)

data_kembali = json.loads(teks)
print(data_kembali["temperature"])
```

## Bab 15. Modul dan virtual environment

Modul memungkinkan kode digunakan kembali. Virtual environment memisahkan paket antarproyek.

```bash
python -m venv .venv
# Windows:
.venv\Scripts\activate
# macOS/Linux:
source .venv/bin/activate
python -m pip install pandas matplotlib
```

## Bab 16. Pemrograman berorientasi objek dasar

```python
class Sensor:
    def __init__(self, sensor_id, suhu):
        self.sensor_id = sensor_id
        self.suhu = suhu

    def tampilkan(self):
        print(self.sensor_id, self.suhu)

sensor1 = Sensor("ESP32-01", 28.5)
sensor1.tampilkan()
```

Class adalah rancangan; object adalah contoh yang dibuat dari rancangan itu. Jangan gunakan class hanya karena bisa. Untuk program kecil, fungsi dan dictionary sering lebih sederhana.

## Bab 17. NumPy dan Pandas

```python
import numpy as np
import pandas as pd

nilai = np.array([28.0, 29.0, 30.0])
print(np.mean(nilai))

df = pd.DataFrame({
    "suhu": [28.0, 29.0, 30.0],
    "debit": [10.2, 11.0, 10.8]
})
print(df.describe())
```

NumPy membantu komputasi numerik. Pandas membantu mengelola data tabel. Mulai dengan data kecil agar hasil mudah diperiksa.

## Bab 18. Visualisasi data

```python
import matplotlib.pyplot as plt

waktu = [1, 2, 3, 4]
suhu = [28.0, 28.5, 29.1, 30.0]

plt.plot(waktu, suhu, marker="o")
plt.xlabel("Urutan pembacaan")
plt.ylabel("Suhu (C)")
plt.title("Perubahan Suhu")
plt.grid(True)
plt.show()
```

Sumbu X menunjukkan urutan/waktu; sumbu Y menunjukkan nilai suhu. Grafik membantu melihat pola, tetapi tidak otomatis membuktikan penyebab perubahan.

## Bab 19. Mini proyek: analisis data sensor

1. Siapkan CSV dengan kolom `timestamp`, `device_id`, `temperature`.
2. Baca dengan Pandas.
3. Periksa nilai kosong dan nilai di luar rentang masuk akal.
4. Hitung rata-rata, minimum, maksimum.
5. Buat grafik suhu.
6. Tulis kesimpulan berdasarkan data, bukan dugaan.

## Peta ke kurikulum 28 hari

| Hari | Fokus | Bukti belajar |
|---:|---|---|
| 1 | Instalasi, editor, menjalankan program | Program pertama berjalan |
| 2 | Output, input, komentar | Program salam |
| 3 | Variabel | Menyimpan data sensor |
| 4 | Tipe data | Memilih tipe nilai |
| 5 | Konversi | Mengubah teks menjadi angka |
| 6 | Operator | Kalkulator sederhana |
| 7 | Kuis dan proyek mini | Program input dan hitung |
| 8 | Boolean dan perbandingan | Uji kondisi |
| 9 | If/elif/else | Alarm suhu |
| 10 | For | Cetak pembacaan berulang |
| 11 | While | Pengulangan dengan kondisi berhenti |
| 12 | List dan tuple | Menyimpan beberapa pembacaan |
| 13 | Set dan dictionary | Data unik dan paket sensor |
| 14 | Fungsi | Fungsi klasifikasi |
| 15 | Modul dan import | Memisahkan fungsi |
| 16 | File teks | Simpan catatan |
| 17 | CSV | Baca data tabel |
| 18 | JSON | Serialisasi data |
| 19 | Exception | Validasi input |
| 20 | venv dan pip | Lingkungan proyek |
| 21 | Kuis dan mini proyek | Program baca data |
| 22 | OOP dasar | Model objek sensor |
| 23 | NumPy | Operasi numerik |
| 24 | Pandas | DataFrame |
| 25 | Pembersihan data | Missing/invalid values |
| 26 | Matplotlib | Grafik data |
| 27 | Statistik dasar | Mean, median, outlier |
| 28 | Proyek dan evaluasi | Laporan analisis sederhana |

## Tes pemahaman akhir Python

1. Apa perbedaan teks `"30"` dan angka `30`?
2. Mengapa `range(1, 6)` hanya menghasilkan lima angka?
3. Apa yang terjadi jika kondisi `if suhu >= 35` bernilai salah?
4. Mengapa fungsi menggunakan `return`?
5. Bagaimana menangani file CSV yang tidak ditemukan?
6. Apa bedanya data kosong dengan nilai sensor 0?
7. Buat flowchart alarm suhu sebelum menulis kode.

**Kriteria penguasaan:** peserta mampu menyusun alur, memprediksi output, menulis modifikasi kecil tanpa menyalin, dan menjelaskan kesalahan yang ditemukan.
