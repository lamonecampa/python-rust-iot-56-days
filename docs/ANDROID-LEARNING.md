# Belajar Python dan Rust melalui Android

Panduan ini memungkinkan materi kurikulum 56 hari dipelajari dari HP Android, tanpa harus selalu membawa laptop. Android cocok untuk membaca materi, mengetik program kecil, menjalankan latihan, melakukan commit sederhana, dan mengakses lingkungan komputasi jarak jauh.

**Prinsip penting:** HP bisa menjadi lingkungan belajar yang nyata, tetapi tidak otomatis setara dengan laptop untuk semua workflow. Ukuran layar, keyboard, RAM, storage, dukungan paket native, dan pembatasan proses latar belakang tetap menjadi batas.

## 1. Pilih mode belajar

| Kebutuhan | Pilihan | Eksekusi kode | Koneksi |
|---|---|---|---|
| Membaca tutorial dan mencoba contoh pendek | Chrome + W3Schools | Browser / sandbox situs | Perlu internet |
| Belajar Python lokal dengan antarmuka sederhana | Pydroid 3 | Di HP | Offline setelah runtime dan paket tersedia |
| Python dan Rust melalui terminal | Termux | Di HP | Paket perlu diunduh saat instalasi |
| Mengedit file dan mengelola Git | Acode atau editor teks pilihan | Bergantung runtime terpisah | Bergantung workflow |
| Proyek berat, notebook besar, dependency sulit | SSH ke laptop/server atau cloud IDE | Mesin remote | Perlu internet |

**Rekomendasi awal untuk pemula:**
- Python: mulai dari Pydroid 3. Gunakan Termux setelah nyaman dengan terminal.
- Rust: gunakan Termux untuk latihan command-line dan Cargo jika perangkat serta repositorinya mendukung. Alternatif yang lebih mudah adalah browser/cloud IDE untuk snippet pendek, tetapi cek apakah compiler Rust benar-benar tersedia.
- Dokumentasi: W3Schools Rust dapat menjadi bacaan pendamping. Untuk konsep mendalam, tetap gunakan The Rust Book dan tutorial lokal di repositori ini.

Aplikasi editor bukan selalu compiler. Syntax highlighting atau tombol Run yang menjalankan kode di server tidak berarti kompilasi berlangsung di HP.

## 2. Setup Python di Android dengan Pydroid 3

1. Instal Pydroid 3 dari Google Play.
2. Buka aplikasi dan tunggu runtime Python selesai disiapkan.
3. Buat file `hari01.py`.
4. Masukkan:

```python
nama = input("Nama: ")
suhu = 27.5
print(f"Halo, {nama}")
print(f"Suhu sensor: {suhu:.1f} C")
```

5. Tekan Run dan periksa output.
6. Ubah nilai suhu dan tambahkan kondisi:

```python
if suhu >= 40:
    print("BAHAYA")
elif suhu >= 35:
    print("WASPADA")
else:
    print("NORMAL")
```

### Paket Python

Mulai dengan standard library agar tidak bergantung pada instalasi paket. Jika butuh paket eksternal, gunakan pengelola paket Pydroid dan periksa ketersediaan build yang kompatibel.

Untuk latihan data:
- `csv`, `json`, `datetime`, `statistics`: mulai dari standard library.
- `numpy`, `pandas`, `matplotlib`: pasang hanya jika versi yang kompatibel tersedia pada repositori paket Pydroid atau lingkungan Termux.
- Jangan menganggap semua paket PyPI dapat dipasang di Android. Paket dengan ekstensi native atau dependensi sistem mungkin gagal.

**Latihan Python di HP:** buat file CSV sederhana berisi timestamp dan pembacaan suhu, baca kembali file tersebut, lalu hitung rata-rata. Setelah berhasil, lanjutkan ke Pandas bila paket tersedia.

## 3. Setup Python di Android dengan Termux

Termux cocok bila ingin belajar workflow terminal dan Git.

Instal Termux dari sumber resmi proyek, seperti F-Droid atau rilis GitHub resmi. Hindari APK dari situs mirror yang tidak jelas. Jangan mencampur instalasi Termux dan add-on dari sumber tanda tangan yang berbeda.

Buka Termux dan jalankan:

```bash
pkg update && pkg upgrade
pkg install python git nano
python --version
git --version
```

Buat latihan:

```bash
mkdir -p ~/belajar-python
cd ~/belajar-python
nano hari01.py
python hari01.py
```

Isi `hari01.py`:

```python
for angka in range(1, 6):
    print(f"Pembacaan ke-{angka}")
```

Untuk paket Python, gunakan virtual environment:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
```

Pemasangan paket ilmiah di Termux dapat memiliki persyaratan khusus. Ikuti dokumentasi paket Termux dan jangan memaksakan instruksi Linux desktop jika dependensinya tidak tersedia.

## 4. Setup Rust di Android dengan Termux

Rust dapat dipelajari melalui terminal Android, tetapi kompilasi lokal lebih menuntut resource daripada menjalankan snippet Python sederhana.

1. Instal Termux dari sumber resmi yang sama dengan add-on yang dipakai.
2. Perbarui paket.
3. Periksa apakah paket Rust tersedia untuk repositori dan arsitektur perangkat:

```bash
pkg update && pkg upgrade
pkg search rust
```

4. Jika paket tersedia, instal:

```bash
pkg install rust
rustc --version
cargo --version
```

5. Buat proyek:

```bash
cargo new rust_sensor_lab
cd rust_sensor_lab
cargo run
```

6. Edit `src/main.rs` menggunakan editor terminal:

```bash
nano src/main.rs
```

Contoh:

```rust
fn main() {
    let device = "ESP32-01";
    let mut temperature: f32 = 27.5;

    println!("Device: {device}");
    temperature += 0.5;
    println!("Temperature: {temperature:.1} C");
}
```

7. Jalankan pemeriksaan:

```bash
cargo check
cargo fmt
cargo test
```

Jika instalasi Rust gagal, paket tidak tersedia untuk arsitektur/repository, atau build terlalu berat, jangan menghabiskan waktu mengutak-atik HP. Gunakan browser IDE atau SSH ke laptop/server Linux untuk kompilasi. Tetap edit dan baca kode melalui HP.

### Keterbatasan Rust di Android

- Build dependency besar dapat lambat dan memakai banyak RAM/storage.
- Tidak semua crate atau toolchain memiliki dukungan Android yang sama.
- Beberapa crate membutuhkan library native atau konfigurasi target khusus.
- Debugging GUI, emulator, dan pengembangan aplikasi Android penuh bukan bagian dari setup ini.
- Termux adalah lingkungan command-line Android, bukan Android Studio.

## 5. Browser learning dan sumber belajar

### Python
- [W3Schools Python](https://www.w3schools.com/python/) — tutorial ringkas dan contoh interaktif.
- [Python Tutorial resmi](https://docs.python.org/3/tutorial/) — acuan konsep dan sintaks.
- [freeCodeCamp: Python on a phone with Pydroid](https://www.freecodecamp.org/news/how-to-code-on-your-phone-python-pydroid-android-app-tutorial/) — contoh workflow Python melalui HP.
- [FromDev: Python tutorials and resources](https://www.fromdev.com/2014/03/python-tutorials-resources.html?amp=1) — daftar sumber tambahan; artikel lama, jadi periksa apakah tautan dan versi materi masih relevan.

### Rust
- [W3Schools Rust](https://www.w3schools.com/rust/) — pengantar dan latihan browser.
- [The Rust Book](https://doc.rust-lang.org/book/) — referensi utama bahasa.
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/) — contoh kode terarah.
- [Kemal Codes Rust Tutorial](https://github.com/kemalcodes/rust-tutorial) — pengayaan melalui proyek.
- [Zero To Mastery Learn Rust](https://zerotomastery.io/courses/learn-rust/) — materi video terstruktur; periksa syarat akses kursus.
- [Rust on Android: How to use it, debug it, and why](https://www.davthecoder.com/blog/rust-on-android-how-to-use-it-debug-it-and-why) — perspektif penggunaan Rust pada Android.
- [Android Open Source Project: Building Rust modules](https://source.android.com/docs/setup/build/rust/building-rust-modules/overview) — dokumentasi untuk membangun modul Rust di dalam source tree AOSP. **Ini bukan panduan memasang Rust di HP Android atau tutorial pemula.** Gunakan hanya jika topik belajar sudah masuk ke pengembangan platform Android/AOSP.

### Catatan kualitas sumber
Artikel FromDev tahun 2014 dan diskusi forum freeCodeCamp tahun 2018 berguna sebagai jejak referensi, bukan acuan instalasi terkini. Instruksi instalasi harus diverifikasi melalui dokumentasi resmi aplikasi dan proyek terkait. W3Schools cocok untuk latihan cepat, tetapi jangan jadikan satu-satunya sumber untuk ownership, lifetime, atau error handling Rust.

## 6. Workflow belajar dari HP dan laptop secara bergantian

Agar file tidak tercecer di folder aplikasi:

1. Simpan kode dan catatan di repository GitHub.
2. Gunakan Git untuk sinkronisasi perubahan.
3. Buat satu folder latihan per minggu atau per proyek.
4. Jangan mengedit file yang sama secara bersamaan dari dua perangkat.
5. Commit perubahan kecil dengan pesan yang jelas.
6. Simpan data simulasi kecil di Git; jangan commit file dataset besar, token, password, atau data pribadi.

Contoh workflow Termux:

```bash
git clone https://github.com/lamonecampa/python-rust-iot-56-days.git
cd python-rust-iot-56-days
git status
```

Untuk mengirim perubahan:

```bash
git add .
git commit -m "Add mobile practice for day 1"
git push
```

Pastikan autentikasi GitHub sudah disiapkan dengan metode yang aman. Jangan menaruh Personal Access Token langsung di source code atau README.

## 7. Rencana belajar mobile 30–60 menit

| Waktu | Aktivitas |
|---|---|
| 5–10 menit | Baca satu submateri melalui browser |
| 15–25 menit | Ketik dan jalankan satu contoh di Pydroid/Termux |
| 10–15 menit | Ubah input dan uji kondisi batas |
| 5–10 menit | Catat pemahaman, error, dan commit bila perlu |

Pada hari yang hanya memungkinkan memakai HP, prioritaskan:
- membaca konsep;
- latihan sintaks dan fungsi;
- ownership/borrowing dengan contoh kecil;
- parsing CSV/JSON;
- unit test sederhana;
- dokumentasi dan catatan.

Tunda build besar, benchmark berat, debugging kompleks, dan pengembangan embedded/Android penuh sampai tersedia laptop atau server.

## 8. Perangkat tambahan yang membantu

- Keyboard Bluetooth untuk mengetik kode lebih nyaman.
- Stand HP atau tablet agar layar tidak terus dipegang.
- Koneksi Wi-Fi saat mengunduh toolchain dan dependency.
- Penyimpanan cloud atau Git untuk backup.
- Earphone bila mengikuti video, tetapi tetap ketik dan jalankan kodenya.

## 9. Pemecahan masalah

| Masalah | Langkah awal |
|---|---|
| Perintah `python` tidak ditemukan | Periksa instalasi runtime; di Termux jalankan `pkg install python` |
| `cargo` tidak ditemukan | Periksa apakah paket Rust tersedia dan terpasang |
| Paket pip gagal dipasang | Cek dukungan Android dan binary wheel; coba paket lain atau lingkungan remote |
| Build Rust kehabisan memori | Tutup aplikasi lain, build proyek kecil, atau pindah ke mesin remote |
| File tidak dapat diakses | Gunakan folder kerja aplikasi atau konfigurasi storage Termux sesuai dokumentasi |
| Proses berhenti saat layar mati | Jangan andalkan HP untuk proses server jangka panjang; gunakan mesin remote |

## 10. Kesimpulan

Android cukup untuk belajar Python dan fondasi Rust secara konsisten. Setup paling sederhana adalah Pydroid 3 untuk Python dan Termux untuk Rust. Browser tutorial berguna untuk membaca dan mencoba konsep. Untuk pekerjaan berat dan integrasi sistem, gunakan laptop atau server melalui SSH.

Targetnya bukan memaksakan semua pekerjaan ke HP, tetapi menghilangkan alasan untuk berhenti belajar ketika laptop tidak tersedia.
