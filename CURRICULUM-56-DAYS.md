# Panduan Lengkap 56 Hari: Python, Rust, dan IoT

**Level:** Pemula | **Durasi:** 8 minggu | **Waktu:** 1–2 jam/hari | **IDE:** VS Code

## Pola belajar harian
- 15–20 menit: baca konsep.
- 35–60 menit: ketik, jalankan, dan ubah contoh.
- 15–25 menit: tantangan mandiri.
- 5–10 menit: catatan dan evaluasi.

Jangan sekadar menyalin kode. Ketik sendiri, ubah nilai, uji input batas, baca error, dan jelaskan kembali konsep.

---

## Hari 01: Setup Python dan VS Code

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Instal Python 3.11+, VS Code, extension Python, pilih interpreter, dan gunakan terminal.

### Contoh kode
```python
print('Halo, Python!')
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 02: Output, input, dan komentar

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Pelajari IPO, print, input, komentar, dan f-string untuk program interaktif.

### Contoh kode
```python
nama = input('Nama: ')\nprint(f'Halo, {nama}!')
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 03: Variabel dan tipe data

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan assignment, int, float, str, bool, dan type untuk data.

### Contoh kode
```python
debit = 12.5\naktif = True\nprint(type(debit), type(aktif))
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 04: Operator aritmetika

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan operator aritmetika, modulo, pangkat, pembagian, dan prioritas operasi.

### Contoh kode
```python
volume = 12.5 * 4\nprint(f'{volume:.2f} liter')
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 05: Konversi dan validasi input

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Konversi input ke angka, tangani ValueError, dan periksa rentang nilai sensor.

### Contoh kode
```python
try:\n    suhu = float(input('Suhu: '))\n    print(-10 <= suhu <= 80)\nexcept ValueError:\n    print('Input harus angka')
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 06: String dan formatting

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan indexing, slicing, strip, lower, replace, dan f-string.

### Contoh kode
```python
kode = ' ESP32-CAM '\nprint(kode.strip().lower())
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 07: Boolean dan operator logika

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Bangun ekspresi boolean dengan perbandingan, and, or, dan not.

### Contoh kode
```python
tegangan = 3.2\naktif = True\nprint(tegangan >= 3 and aktif)
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 08: Percabangan if elif else

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Buat keputusan dengan if, elif, else, indentasi, dan kondisi bertingkat.

### Contoh kode
```python
nilai = 38\nif nilai >= 40: status='Bahaya'\nelif nilai >= 35: status='Waspada'\nelse: status='Normal'\nprint(status)
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 09: Perulangan for dan range

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan for, range, enumerate, dan akumulator untuk memproses data.

### Contoh kode
```python
total = 0\nfor x in range(1, 6): total += x\nprint(total)
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 10: Perulangan while dan kontrol

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan while, break, continue, dan kondisi berhenti yang aman.

### Contoh kode
```python
i = 0\nwhile i < 3:\n    print(i)\n    i += 1
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 11: List dan operasi koleksi

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Buat list, akses elemen, append, remove, sort, len, min, max.

### Contoh kode
```python
data = [12.1, 12.4, 11.9]\ndata.append(12.6)\nprint(min(data), max(data))
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 12: Tuple, set, dan unpacking

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Bedakan tuple immutable, set unik, operasi set, dan unpacking.

### Contoh kode
```python
konfig = ('flow', 'L/min')\njenis = {'flow','pressure','flow'}\nprint(konfig, jenis)
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 13: Dictionary dan data terstruktur

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan dictionary key-value, get, update, items, dan nested dictionary.

### Contoh kode
```python
sensor = {'id':'S1','debit':12.4}\nsensor['debit'] = 13.0\nprint(sensor.get('debit'))
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 14: Fungsi dan return

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Tulis fungsi dengan def, parameter, return, docstring, dan scope.

### Contoh kode
```python
def debit(volume, menit):\n    return volume / menit\nprint(debit(50, 4))
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 15: Parameter dan modularisasi

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan default argument, keyword argument, import, dan pemisahan modul.

### Contoh kode
```python
def status(nilai, batas=10):\n    return 'tinggi' if nilai > batas else 'normal'\nprint(status(12))
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 16: File teks dan pathlib

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Baca/tulis file teks dengan pathlib, encoding, dan context manager.

### Contoh kode
```python
from pathlib import Path\np=Path('log.txt')\np.write_text('sensor aktif', encoding='utf-8')\nprint(p.read_text(encoding='utf-8'))
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 17: CSV untuk data sensor

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Baca/tulis CSV menggunakan csv.DictReader dan DictWriter.

### Contoh kode
```python
import csv\nwith open('sensor.csv','w',newline='') as f:\n    w=csv.writer(f); w.writerow(['waktu','debit']); w.writerow(['08:00',12.4])
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 18: JSON untuk pertukaran data

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Serialisasi dictionary menjadi JSON dan parse kembali dengan json.

### Contoh kode
```python
import json\nobj={'device':'S1','value':12.5}\nprint(json.loads(json.dumps(obj)))
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 19: Exception dan debugging

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Kelola kegagalan dengan try/except/else/finally dan debugging.

### Contoh kode
```python
try:\n    nilai=float('abc')\nexcept ValueError as err:\n    print('Data tidak valid:', err)
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 20: Virtual environment dan pip

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Isolasi dependency dengan venv, pip, dan requirements.txt.

### Contoh kode
```python
# python -m venv .venv\n# python -m pip install pandas matplotlib
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 21: Datetime dan timestamp

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan datetime, timezone UTC, parsing, dan format ISO 8601.

### Contoh kode
```python
from datetime import datetime, timezone\nprint(datetime.now(timezone.utc).isoformat())
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 22: OOP dasar dengan class

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Buat class, instance, attribute, method, dan constructor __init__.

### Contoh kode
```python
class Sensor:\n    def __init__(self, nama): self.nama=nama\n    def baca(self): return 12.5\ns=Sensor('flow')\nprint(s.nama, s.baca())
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 23: NumPy untuk komputasi numerik

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan NumPy array, dtype, shape, operasi vektor, mean, min, max.

### Contoh kode
```python
import numpy as np\nx=np.array([10.,12.,11.])\nprint(x.mean(), x.max())
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 24: Pandas DataFrame

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan Pandas Series, DataFrame, read_csv, head, info, describe.

### Contoh kode
```python
import pandas as pd\ndf=pd.DataFrame({'debit':[10,12,11]})\nprint(df.describe())
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 25: Data cleaning dengan Pandas

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Tangani missing values, filtering, sorting, transformasi, dan outlier.

### Contoh kode
```python
import pandas as pd\ndf=pd.DataFrame({'x':[10,None,14]})\ndf['x']=df['x'].fillna(df['x'].median())\nprint(df)
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 26: Matplotlib time-series

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Buat grafik garis time-series dengan label, satuan, grid, savefig.

### Contoh kode
```python
import matplotlib.pyplot as plt\nplt.plot([0,1,2],[10,12,11], marker='o')\nplt.xlabel('Menit'); plt.ylabel('Debit (L/min)'); plt.grid()\nplt.savefig('grafik.png')
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 27: Statistik dan deteksi outlier

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Hitung mean, median, standar deviasi, kuartil, dan IQR.

### Contoh kode
```python
import pandas as pd\ns=pd.Series([10,11,10,12,11,50])\nq1,q3=s.quantile(.25),s.quantile(.75)\niqr=q3-q1\nprint(s[(s<q1-1.5*iqr)|(s>q3+1.5*iqr)])
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 28: Mini proyek analisis sensor

**Fase:** Python | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gabungkan pembacaan CSV, validasi, statistik, grafik, dokumentasi.

### Contoh kode
```python
# Baca CSV, validasi rentang, hitung statistik, simpan grafik.
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh menjadi program mini terkait pembacaan sensor. Pastikan satuan dan tipe data konsisten.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 29: Instalasi Rust dan Cargo

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Pasang rustup, rustc, Cargo, buat project, dan jalankan cargo run.

### Contoh kode
```rust
fn main() { println!("Halo, Rust!"); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 30: Variabel dan mutability

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan let, mut, shadowing, const, dan inferensi tipe.

### Contoh kode
```rust
fn main(){ let mut x=10; x+=1; println!("{x}"); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 31: Tipe scalar dan compound

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Pelajari integer, float, bool, char, tuple, array, dan anotasi tipe.

### Contoh kode
```rust
fn main(){ let t:(i32,f64,bool)=(1,2.5,true); let a=[1,2,3]; println!("{} {}",t.1,a[0]); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 32: Operator dan ekspresi

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan operator aritmetika, perbandingan, boolean, dan casting.

### Contoh kode
```rust
fn main(){ let v=12.5_f64*4.0; let ok=v>0.0; println!("{v} {ok}"); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 33: if, loop, dan kontrol alur

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan if sebagai ekspresi, loop, while, for, dan break.

### Contoh kode
```rust
fn main(){ let x=17; let s=if x>15 {"tinggi"} else {"normal"}; println!("{s}"); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 34: Fungsi dan return type

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Tulis fn dengan parameter bertipe dan return type eksplisit.

### Contoh kode
```rust
fn rata(total:f64,n:f64)->f64 { total/n }\nfn main(){ println!("{}",rata(50.0,4.0)); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 35: String, String, dan &str

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Bedakan String yang dimiliki dan &str yang dipinjam.

### Contoh kode
```rust
fn main(){ let nama:&str="LoRa"; let mut s=String::from("Sensor "); s.push_str(nama); println!("{s}"); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 36: Vector dan iterasi

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan Vec<T>, push, len, get, indexing, dan iterasi referensi.

### Contoh kode
```rust
fn main(){ let mut v=vec![10,12,11]; v.push(13); for x in &v { println!("{x}"); } }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 37: Ownership dan move

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Pahami owner tunggal, move, Copy, clone, dan aturan kepemilikan.

### Contoh kode
```rust
fn main(){ let a=String::from("sensor"); let b=a; println!("{b}"); }
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 38: Borrowing dan references

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan &T dan &mut T serta pahami aturan aliasing dan mutability.

### Contoh kode
```rust
fn panjang(s:&String)->usize{s.len()}\nfn main(){let n=String::from("LoRa");println!("{}",panjang(&n));}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 39: Slices dan lifetime pengantar

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan string slice, array slice, referensi valid, dan lifetime dasar.

### Contoh kode
```rust
fn pertama(s:&str)->&str{s.split_whitespace().next().unwrap_or("")}\nfn main(){println!("{}",pertama("sensor air"));}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 40: Struct dan impl

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Kelompokkan data dengan struct dan tambahkan method melalui impl.

### Contoh kode
```rust
struct Sensor{debit:f64}\nimpl Sensor{fn status(&self)->&'static str{if self.debit>12.0{"tinggi"}else{"normal"}}}\nfn main(){let s=Sensor{debit:13.0};println!("{}",s.status());}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 41: Enum, Option, dan match

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Modelkan status dengan enum, Option, Some, None, dan match exhaustive.

### Contoh kode
```rust
fn baca(v:Option<f64>){match v{Some(x)=>println!("{x}"),None=>println!("kosong")}}\nfn main(){baca(Some(12.5));baca(None);}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 42: HashMap dan koleksi

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan HashMap untuk penyimpanan key-value dan lookup.

### Contoh kode
```rust
use std::collections::HashMap;\nfn main(){let mut m=HashMap::new();m.insert("debit",12.5);println!("{:?}",m.get("debit"));}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 43: Traits dan generics pengantar

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Kenali trait sebagai kontrak perilaku dan generic untuk kode reusable.

### Contoh kode
```rust
trait Identitas{fn id(&self)->&str;}\nstruct Sensor{nama:String}\nimpl Identitas for Sensor{fn id(&self)->&str{&self.nama}}\nfn tampil<T:Identitas>(x:&T){println!("{}",x.id());}\nfn main(){let s=Sensor{nama:"S1".into()};tampil(&s);}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 44: Result dan error handling

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Kelola hasil dengan Result, Ok, Err, ?, dan error propagation.

### Contoh kode
```rust
fn parse(s:&str)->Result<f64,std::num::ParseFloatError>{s.parse()}\nfn main(){println!("{:?}",parse("12.5"));}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 45: Modul dan visibility

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Pisahkan kode dengan mod, pub, use, dan struktur file crate.

### Contoh kode
```rust
mod sensor{pub fn valid(x:f64)->bool{x>=0.0}}\nfn main(){println!("{}",sensor::valid(12.0));}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 46: File I/O dan JSONL

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Tulis file dengan std::fs, Write, Result, dan format JSONL.

### Contoh kode
```rust
use std::{fs::File,io::Write};\nfn main()->std::io::Result<()>{let mut f=File::create("data.jsonl")?;writeln!(f,"{{\\\"value\\\":12.5}}")?;Ok(())}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 47: Serde JSON serialisasi

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Gunakan Serde Serialize/Deserialize dan serde_json.

### Contoh kode
```rust
// Cargo.toml: serde = { version="1", features=["derive"] }; serde_json="1"\nuse serde::Serialize;\n#[derive(Serialize)] struct R{value:f64}\nfn main(){let r=R{value:12.5};println!("{}",serde_json::to_string(&r).unwrap());}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 48: Unit testing dan cargo fmt

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Tulis unit test, assert, cargo test, cargo fmt, dan baca compiler diagnostics.

### Contoh kode
```rust
fn valid(x:f64)->bool{(0.0..=100.0).contains(&x)}\n#[cfg(test)] mod tests{use super::*;#[test]fn batas(){assert!(valid(100.0));}}\nfn main(){}
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 49: Mini proyek Rust collector

**Fase:** Rust | **Durasi:** 60–120 menit

### Tujuan dan konsep
Bangun collector yang memvalidasi data dan menghasilkan JSONL.

### Contoh kode
```rust
// Buat generator 30 record JSONL; validasi rentang dan gunakan Result.
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Kembangkan contoh dengan tipe eksplisit, penanganan error, dan pengujian. Jangan mengatasi error compiler dengan mematikan pemeriksaan.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 50: Desain arsitektur dan kontrak data

**Fase:** Integrasi | **Durasi:** 60–120 menit

### Tujuan dan konsep
Tetapkan kontrak field JSONL dan tanggung jawab Rust vs Python.

### Contoh kode
```text
// Record JSON: timestamp, device, sensor, value, unit.\n// Rust mengumpulkan dan memvalidasi; Python menganalisis.
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Terapkan konsep pada pipeline Rust → JSONL → Python. Dokumentasikan apakah data simulasi atau perangkat nyata.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 51: Generator data sensor dengan Rust

**Fase:** Integrasi | **Durasi:** 60–120 menit

### Tujuan dan konsep
Bangkitkan data simulasi dengan timestamp dan variasi sensor.

### Contoh kode
```text
// Hasilkan 100 record dengan timestamp dan variasi pembacaan sensor.
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Terapkan konsep pada pipeline Rust → JSONL → Python. Dokumentasikan apakah data simulasi atau perangkat nyata.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 52: Validasi dan serialisasi JSONL

**Fase:** Integrasi | **Durasi:** 60–120 menit

### Tujuan dan konsep
Validasi nilai, tolak data invalid, serialisasi dan catat alasan penolakan.

### Contoh kode
```text
// Tolak nilai NaN/di luar rentang; catat alasan ke stderr.
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Terapkan konsep pada pipeline Rust → JSONL → Python. Dokumentasikan apakah data simulasi atau perangkat nyata.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 53: Membaca JSONL dengan Python

**Fase:** Integrasi | **Durasi:** 60–120 menit

### Tujuan dan konsep
Baca JSONL per baris, parse JSON, dan tangani baris rusak.

### Contoh kode
```text
import json\nfor line in open('readings.jsonl', encoding='utf-8'):\n    try: row=json.loads(line)\n    except json.JSONDecodeError: continue\n    print(row)
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Terapkan konsep pada pipeline Rust → JSONL → Python. Dokumentasikan apakah data simulasi atau perangkat nyata.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 54: Analisis data dengan Pandas

**Fase:** Integrasi | **Durasi:** 60–120 menit

### Tujuan dan konsep
Ubah record menjadi DataFrame, bersihkan, hitung statistik dan anomali.

### Contoh kode
```text
import pandas as pd\ndf=pd.DataFrame([{'value':10},{'value':11},{'value':50}])\nprint(df['value'].describe())
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Terapkan konsep pada pipeline Rust → JSONL → Python. Dokumentasikan apakah data simulasi atau perangkat nyata.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 55: Grafik dan ekspor laporan

**Fase:** Integrasi | **Durasi:** 60–120 menit

### Tujuan dan konsep
Buat grafik time-series dan ekspor ringkasan CSV.

### Contoh kode
```text
# Ekspor summary.csv dan timeseries.png dengan label dan satuan.
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Terapkan konsep pada pipeline Rust → JSONL → Python. Dokumentasikan apakah data simulasi atau perangkat nyata.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.

---

## Hari 56: Pengujian end-to-end dan demo

**Fase:** Integrasi | **Durasi:** 60–120 menit

### Tujuan dan konsep
Uji pipeline dari awal sampai akhir, dokumentasikan batasan dan demo.

### Contoh kode
```text
# cargo run\n# python capstone/python-analysis/analyze.py capstone/data/readings.jsonl
```

### Penjelasan
Pahami setiap baris, tipe data, alur eksekusi, dan hasilnya. Jalankan contoh di VS Code. Jika contoh menggunakan library eksternal, pasang library di virtual environment (Python) atau dependency di Cargo.toml (Rust).

### Praktik
1. Ketik ulang contoh dan jalankan.
2. Ubah minimal dua input/nilai.
3. Tambahkan validasi atau kondisi batas.
4. Catat output dan error yang ditemukan.

### Tantangan
Terapkan konsep pada pipeline Rust → JSONL → Python. Dokumentasikan apakah data simulasi atau perangkat nyata.

### Evaluasi diri
- [ ] Dapat menjelaskan konsep tanpa membaca ulang.
- [ ] Program berjalan dan output diverifikasi.
- [ ] Menguji kondisi normal dan batas.
- [ ] Menulis refleksi 3–5 kalimat.


## Kriteria kelulusan
Selesaikan seluruh tantangan, lulus kuis mingguan, dan demonstrasikan capstone. Jika belum paham, ulangi sesi. Checklist bukan pengganti kompetensi.
