# Tutorial Visual Block untuk Pemula: Python, Rust, dan IoT

Panduan ini ditujukan bagi orang yang **belum pernah belajar pemrograman**. Mulai dari memahami urutan instruksi melalui blok visual, kemudian algoritma dan flowchart, baru membaca kode Python atau Rust.

> **Catatan penting:** blok pada panduan ini adalah representasi visual untuk belajar, bukan blok yang dapat dieksekusi seperti proyek Scratch. Python dan Rust tetap ditulis sebagai kode teks. Tujuannya agar peserta memahami logika sebelum berhadapan dengan sintaks.

## 1. Cara berpikir seperti programmer

Program adalah sekumpulan instruksi yang dijalankan komputer secara berurutan. Komputer tidak menebak maksud kita. Instruksi harus jelas, berurutan, dan tidak saling bertentangan.

Gunakan pola belajar berikut untuk setiap materi:

1. **Lihat blok visual:** pahami apa yang dilakukan program.
2. **Baca algoritma:** uraikan langkahnya dengan bahasa sehari-hari.
3. **Ikuti flowchart:** lihat urutan dan percabangan proses.
4. **Baca kode:** cocokkan setiap baris dengan blok.
5. **Jalankan dan amati:** bandingkan hasil aktual dengan perkiraan.
6. **Ubah satu hal:** lihat bagaimana perubahan instruksi mengubah hasil.

## 2. Mengenal jenis blok dasar

| Blok | Makna sederhana | Contoh kegiatan |
|---|---|---|
| Mulai / Selesai | Penanda awal atau akhir | Program dimulai |
| Input | Menerima data | Membaca nama atau sensor |
| Proses | Mengolah atau menyimpan nilai | Menghitung rata-rata |
| Output | Menampilkan atau mengirim hasil | Menampilkan suhu |
| Keputusan | Memilih berdasarkan kondisi | Jika suhu > 35 |
| Perulangan | Mengulang instruksi | Membaca sensor setiap detik |
| Fungsi | Sekumpulan instruksi bernama | Fungsi hitung rata-rata |

### Bentuk blok yang dipakai

- **MULAI / SELESAI:** titik awal dan akhir.
- **INPUT:** data masuk ke program.
- **PROSES:** komputer melakukan pekerjaan.
- **KEPUTUSAN:** kondisi menghasilkan cabang YA atau TIDAK.
- **ULANGI:** kembali mengerjakan langkah tertentu.
- **OUTPUT:** hasil ditampilkan atau dikirim.

## 3. Latihan 1: Program pertama

### Blok visual

```text
┌───────────────┐
│     MULAI     │
└───────┬───────┘
        ↓
┌──────────────────────┐
│ OUTPUT: Halo Dunia!  │
└──────────┬───────────┘
           ↓
┌───────────────┐
│    SELESAI    │
└───────────────┘
```

### Algoritma
1. Mulai.
2. Tampilkan tulisan "Halo Dunia!".
3. Selesai.

### Python

```python
print("Halo Dunia!")
```

**Penjelasan per baris**
- `print()` adalah perintah untuk menampilkan sesuatu.
- Teks diapit tanda kutip karena merupakan data berupa tulisan.
- Tanda kurung berisi hal yang ingin ditampilkan.

### Rust

```rust
fn main() {
    println!("Halo Dunia!");
}
```

**Penjelasan per bagian**
- `fn main()` adalah fungsi utama, tempat program mulai berjalan.
- Kurung kurawal `{}` membatasi isi fungsi.
- `println!` menampilkan teks dan berpindah ke baris berikutnya.
- Titik koma `;` mengakhiri pernyataan tersebut.

**Perbedaan penting:** Python biasanya lebih ringkas. Rust memiliki aturan sintaks yang lebih ketat. Keduanya menjalankan logika yang sama.

## 4. Latihan 2: Input dan output

### Blok visual

```text
[MULAI]
   ↓
[INPUT: nama pengguna]
   ↓
[PROSES: simpan nama]
   ↓
[OUTPUT: "Halo, " + nama]
   ↓
[SELESAI]
```

### Python

```python
nama = input("Masukkan nama: ")
print("Halo,", nama)
```

- `input()` meminta pengguna mengetik data.
- `nama` adalah variabel, yaitu tempat menyimpan nilai.
- Tanda `=` memberikan nilai ke variabel.
- `print()` menampilkan hasil.

### Rust

```rust
use std::io;

fn main() {
    let mut nama = String::new();

    println!("Masukkan nama:");
    io::stdin()
        .read_line(&mut nama)
        .expect("Gagal membaca input");

    println!("Halo, {}", nama.trim());
}
```

- `use std::io;` membawa fasilitas input-output standar.
- `let mut nama` membuat variabel yang nilainya boleh diubah.
- `String::new()` membuat tempat penyimpanan teks kosong.
- `read_line()` membaca teks dari keyboard.
- `expect()` menghentikan program dengan pesan jika pembacaan gagal.
- `trim()` menghapus karakter spasi/baris baru di tepi teks.

## 5. Latihan 3: Keputusan IF

Masalah: jika nilai suhu lebih dari 35°C, tampilkan PERINGATAN. Jika tidak, tampilkan NORMAL.

### Blok visual

```text
       [MULAI]
          ↓
 [INPUT: suhu sensor]
          ↓
   ◇ suhu > 35? ◇
      ↙       ↘
    YA         TIDAK
    ↓            ↓
[OUTPUT:      [OUTPUT:
PERINGATAN]   NORMAL]
      ↘       ↙
       [SELESAI]
```

### Python

```python
suhu = 37.5

if suhu > 35:
    print("PERINGATAN")
else:
    print("NORMAL")
```

### Rust

```rust
fn main() {
    let suhu: f32 = 37.5;

    if suhu > 35.0 {
        println!("PERINGATAN");
    } else {
        println!("NORMAL");
    }
}
```

**Cara membaca keputusan:** komputer memeriksa apakah kondisi benar. Jika benar, jalankan cabang pertama. Jika salah, jalankan cabang kedua.

Coba ubah suhu menjadi 30.0, 35.0, dan 40.0. Perhatikan bahwa kondisi `>` berarti lebih besar, bukan lebih besar atau sama dengan.

## 6. Latihan 4: Perulangan

Masalah: tampilkan angka 1 sampai 5.

### Blok visual

```text
[MULAI]
   ↓
[angka = 1]
   ↓
◇ angka <= 5? ◇ ── TIDAK ──→ [SELESAI]
   │ YA
   ↓
[OUTPUT angka]
   ↓
[angka = angka + 1]
   └──────── kembali ke pemeriksaan
```

### Python

```python
for angka in range(1, 6):
    print(angka)
```

### Rust

```rust
fn main() {
    for angka in 1..=5 {
        println!("{angka}");
    }
}
```

- Perulangan menjalankan instruksi berulang kali.
- Python `range(1, 6)` menghasilkan 1, 2, 3, 4, 5.
- Rust `1..=5` juga mencakup angka 5.
- Hati-hati: Rust `1..5` tidak mencakup angka 5.

## 7. Latihan 5: Membaca sensor dan menentukan status

Contoh ini memakai nilai sensor simulasi agar logika dapat dipelajari tanpa perangkat fisik.

### Blok visual

```text
[MULAI]
   ↓
[INPUT: baca nilai suhu]
   ↓
◇ suhu >= 40? ◇
  YA ↓          TIDAK ↓
[status =     ◇ suhu >= 35? ◇
 "BAHAYA"]      YA ↓       TIDAK ↓
              [status =   [status =
              "WASPADA"]  "NORMAL"]
                  ↘        ↙
              [OUTPUT status]
                    ↓
                 [SELESAI]
```

### Python

```python
suhu = 37.2

if suhu >= 40:
    status = "BAHAYA"
elif suhu >= 35:
    status = "WASPADA"
else:
    status = "NORMAL"

print(f"Suhu: {suhu} C")
print(f"Status: {status}")
```

### Rust

```rust
fn main() {
    let suhu: f32 = 37.2;

    let status = if suhu >= 40.0 {
        "BAHAYA"
    } else if suhu >= 35.0 {
        "WASPADA"
    } else {
        "NORMAL"
    };

    println!("Suhu: {suhu} C");
    println!("Status: {status}");
}
```

**Uji tiga kondisi batas:** 34.9°C, 35.0°C, dan 40.0°C. Menguji nilai batas adalah kebiasaan penting, karena kesalahan sering muncul tepat di batas kondisi.

## 8. Latihan 6: Simulasi LED berkedip

### Blok visual

```text
[MULAI]
   ↓
[atur pin LED sebagai OUTPUT]
   ↓
┌──────────── ULANGI TERUS ────────────┐
│ [LED ON] → [tunggu 1 detik]          │
│ [LED OFF] → [tunggu 1 detik]         │
└─────────────────────────────────────┘
```

### Pseudocode

```text
atur pin LED sebagai OUTPUT
ULANGI TERUS:
    nyalakan LED
    tunggu 1 detik
    matikan LED
    tunggu 1 detik
```

### Contoh MicroPython untuk board ESP32

```python
from machine import Pin
from time import sleep

led = Pin(2, Pin.OUT)

while True:
    led.on()
    sleep(1)
    led.off()
    sleep(1)
```

**Penting:** ini contoh MicroPython untuk ESP32, bukan Python desktop biasa. Nomor GPIO harus disesuaikan dengan board dan rangkaian. LED bawaan pada sebagian board aktif-LOW, sehingga perilaku ON/OFF dapat terbalik.

**Bagaimana dengan Rust?** Rust pada ESP32 memerlukan toolchain dan framework embedded seperti esp-rs, konfigurasi target, serta akses GPIO yang sesuai board. Kode Rust desktop biasa tidak otomatis dapat mengendalikan pin ESP32. Pelajari logika perulangannya dahulu; praktik embedded Rust menjadi materi lanjutan.

## 9. Kamus sederhana: istilah pemrograman

| Istilah | Penjelasan untuk pemula |
|---|---|
| Program | Kumpulan instruksi untuk komputer |
| Algoritma | Langkah-langkah menyelesaikan masalah |
| Variabel | Tempat menyimpan nilai |
| Tipe data | Jenis nilai, misalnya angka, teks, benar/salah |
| Input | Data yang masuk |
| Output | Hasil yang keluar |
| Kondisi | Pertanyaan yang jawabannya benar atau salah |
| Perulangan | Instruksi yang dikerjakan berulang |
| Fungsi | Kumpulan instruksi dengan nama tertentu |
| Debugging | Mencari dan memperbaiki kesalahan |
| Compiler | Program yang menerjemahkan kode Rust menjadi program yang dapat dijalankan |
| Library | Kumpulan kode siap pakai |

## 10. Urutan belajar yang disarankan

Jangan langsung melompat ke AI atau IoT kompleks. Kuasai pola pikir dasar terlebih dahulu.

1. Hari 1–3: mulai, output, input, variabel.
2. Hari 4–7: tipe data, operator, dan keputusan.
3. Hari 8–10: perulangan.
4. Hari 11–15: koleksi data dan fungsi.
5. Hari 16–21: file, error, dan modul.
6. Hari 22–28: Python untuk pengolahan data.
7. Hari 29–49: pelajari Rust dengan pola visual yang sama, lalu pahami ownership, borrowing, dan tipe data Rust.
8. Hari 50–56: integrasikan data Rust dan analisis Python.

Untuk setiap topik, peserta sebaiknya menggambar ulang bloknya di kertas atau papan tulis sebelum menulis kode. Ini latihan memahami alur, bukan lomba mengetik cepat.

## 11. Latihan mandiri dan evaluasi

### Tantangan A: lampu berdasarkan kondisi
Buat algoritma yang menyalakan lampu jika kondisi gelap dan mematikannya jika terang.

### Tantangan B: alarm suhu
Jika suhu 40°C atau lebih, tampilkan BAHAYA. Jika 35°C sampai kurang dari 40°C, tampilkan WASPADA. Selain itu tampilkan NORMAL.

### Tantangan C: pencacah data
Tampilkan angka 1 sampai 10, lalu hitung jumlah seluruh angka.

### Rubrik evaluasi

| Aspek | Bobot |
|---|---:|
| Dapat menjelaskan tujuan program | 20% |
| Dapat menyusun blok dan algoritma | 25% |
| Dapat menerjemahkan blok ke kode | 25% |
| Dapat menjalankan dan membaca output | 15% |
| Dapat menemukan serta memperbaiki kesalahan | 15% |

**Kriteria lulus latihan:** peserta mampu menjelaskan alur dengan kata-katanya sendiri, bukan hanya menunjukkan kode yang berhasil dijalankan.
