# Visualisasi Konsep Rust untuk Pemula

Dokumen pendamping untuk `RUST-TUTORIAL.md`. Fokusnya adalah konsep yang sering membuat pemula tersandung: tipe, ownership, borrowing, collections, Option, Result, dan error handling.

## 1. Variabel dan mutability

```text
[NILAI 25.5] → [let suhu: f32] → [NILAI tersimpan]
```

```rust
let suhu: f32 = 25.5;
let mut tekanan: f32 = 1.2;
tekanan = 1.3;
```

- `let`: binding tidak dapat ditugasi ulang.
- `let mut`: binding dapat diubah.
- `f32`: tipe angka pecahan 32-bit.
- Tipe eksplisit membantu compiler memeriksa konsistensi.

## 2. Ownership: siapa pemilik nilai?

Rust memastikan setiap nilai memiliki aturan kepemilikan yang jelas. Pikirkan sebuah dokumen yang berpindah pemilik. Ini analogi untuk memahami move, bukan definisi teknis lengkap.

### Sebelum move

```text
sensor_a ─────→ [String: "ESP32-01"]
```

### Setelah move

```text
sensor_a  (tidak lagi dapat memakai nilai)
sensor_b ─────→ [String: "ESP32-01"]
```

```rust
let sensor_a = String::from("ESP32-01");
let sensor_b = sensor_a;
// println!("{sensor_a}"); // error: nilai sudah dipindahkan
println!("{sensor_b}");
```

Untuk tipe seperti integer sederhana yang mengimplementasikan `Copy`, penugasan dapat menyalin nilai, bukan memindahkan kepemilikan.

## 3. Borrowing: meminjam tanpa mengambil kepemilikan

```text
pemilik data ─────→ [String]
                       ↑
                 &data (pinjaman baca)
```

```rust
fn tampilkan(teks: &String) {
    println!("{teks}");
}

fn main() {
    let nama = String::from("ESP32-01");
    tampilkan(&nama);
    println!("{nama}"); // masih dapat dipakai
}
```

Tanda `&` membuat reference. Fungsi menerima pinjaman, bukan mengambil ownership.

## 4. Mutable borrowing

```text
pemilik data ─────→ [String]
                       ↑
                &mut data
             pinjaman untuk mengubah
```

```rust
fn tambah_label(teks: &mut String) {
    teks.push_str("-LAB");
}

fn main() {
    let mut nama = String::from("ESP32");
    tambah_label(&mut nama);
    println!("{nama}");
}
```

Aturan penting: dalam satu waktu, Rust membatasi reference mutable agar tidak ada konflik akses. Secara sederhana, satu pinjaman mutable aktif atau beberapa pinjaman immutable, bukan keduanya sekaligus pada area yang sama.

## 5. Scope dan lifetime dasar

```text
[MULAI BLOK]
   ├─ [buat variabel lokal]
   ├─ [gunakan variabel]
   └─ [akhir blok: variabel lokal tidak berlaku lagi]
```

Scope adalah wilayah kode tempat binding berlaku. Lifetime berkaitan dengan berapa lama reference valid. Jangan menyimpulkan bahwa lifetime berarti objek selalu hidup selama aplikasi berjalan.

## 6. Struct: mengelompokkan data

```text
[Sensor]
  ├─ id
  ├─ temperature
  └─ online
```

```rust
struct Sensor {
    id: String,
    temperature: f32,
    online: bool,
}
```

Struct menggabungkan beberapa field menjadi satu tipe data.

## 7. Enum dan match: memilih bentuk data

```text
[status sensor]
   ├─ [Online]
   ├─ [Offline]
   └─ [Error]
```

```rust
enum Status {
    Online,
    Offline,
    Error,
}

fn tampilkan(status: Status) {
    match status {
        Status::Online => println!("Terhubung"),
        Status::Offline => println!("Terputus"),
        Status::Error => println!("Ada kesalahan"),
    }
}
```

`match` memeriksa kemungkinan varian. Compiler membantu memastikan semua varian ditangani.

## 8. Option: nilai mungkin tersedia atau tidak

```text
[hasil pencarian]
     ◇ ada nilai? ◇
       /       \
    YA           TIDAK
    ↓              ↓
[Some(nilai)]   [None]
```

```rust
let pembacaan: Option<f32> = Some(28.5);

match pembacaan {
    Some(nilai) => println!("Suhu: {nilai}"),
    None => println!("Belum ada data"),
}
```

Option bukan penanda error umum. Ia menyatakan nilai mungkin ada (`Some`) atau tidak ada (`None`).

## 9. Result: operasi bisa berhasil atau gagal

```text
[operasi baca file]
       ◇ berhasil? ◇
        /       \
      YA         TIDAK
      ↓             ↓
 [Ok(data)]     [Err(error)]
```

```rust
use std::fs;

fn main() {
    match fs::read_to_string("sensor.txt") {
        Ok(konten) => println!("{konten}"),
        Err(error) => println!("Gagal membaca file: {error}"),
    }
}
```

Option berarti mungkin tidak ada nilai. Result berarti operasi menghasilkan keberhasilan atau kegagalan yang membawa informasi error.

## 10. Collections: banyak nilai

```text
[Vec pembacaan]
   ├─ indeks 0: 28.1
   ├─ indeks 1: 28.5
   └─ indeks 2: 29.0
```

```rust
let suhu = vec![28.1, 28.5, 29.0];
for nilai in &suhu {
    println!("{nilai}");
}
```

## 11. Alur data collector

```text
[simulasi/baca sensor]
          ↓
[validasi rentang dan field]
          ↓
[serialisasi JSON]
          ↓
[tulis satu record JSONL]
          ↓
[Python membaca JSONL]
          ↓
[validasi dan analisis Pandas]
          ↓
[ringkasan dan grafik]
```

JSONL adalah teks dengan satu objek JSON per baris. Tetapkan kontrak field, tipe, satuan, dan timestamp agar Rust dan Python sepakat tentang bentuk data.

## 12. Debugging dengan compiler

1. Baca pesan error pertama, bukan hanya baris terakhir.
2. Temukan file dan nomor baris.
3. Baca bagian kode yang disebut.
4. Periksa tipe, ownership, borrowing, dan tanda baca.
5. Ubah satu hal.
6. Jalankan `cargo check` lagi.

Compiler adalah alat bantu belajar. Pesan error sering menunjukkan aturan bahasa yang belum dipahami.

## Latihan visual

1. Gambarkan pemilik String sebelum dan sesudah move.
2. Tandai reference immutable dan mutable dalam potongan kode.
3. Buat flowchart untuk `Option<f32>`.
4. Buat flowchart untuk pembacaan file yang menghasilkan `Result`.
5. Gambarkan alur satu record sensor dari Rust sampai grafik Python.
