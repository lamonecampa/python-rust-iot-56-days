# Silabus Rust Terapan untuk IoT dan Analisis Data

**Posisi dalam program:** Hari 29–56 dari kurikulum 56 hari  
**Prasyarat:** Menyelesaikan Python hari 1–28, mampu memakai terminal dan VS Code  
**Durasi:** 28 hari, 1–2 jam/hari  
**Pendekatan:** 30% konsep, 50% praktik terarah, 20% debugging dan refleksi

**Metode pemula:** konteks nyata → visual block → flowchart → pseudocode → prediksi → kode → debugging → evaluasi. Lihat [Standar Pembelajaran](PEDAGOGICAL-STANDARD.md) dan [Panduan Visual Rust](RUST-VISUAL-GUIDE.md).

## 1. Rasional dan batas capaian

Rust dipelajari sebagai bahasa untuk membangun komponen yang membutuhkan performa, kontrol sumber daya, dan keandalan. Python tetap digunakan untuk eksplorasi data, statistik, visualisasi, dan eksperimen machine learning. Pembagian tugas ini lebih realistis daripada memaksakan seluruh pekerjaan data science ke Rust sejak awal.

Dalam 28 hari, targetnya adalah membangun fondasi Rust yang cukup kuat untuk membuat data collector berbasis terminal, memvalidasi data sensor, menulis JSON Lines (JSONL), menguji fungsi inti, dan menyerahkan data ke pipeline analisis Python.

**Bukan target 28 hari:** mahir async Rust, membuat backend produksi, embedded Rust pada mikrokontroler, menguasai machine learning Rust, atau menjamin sistem siap deployment. Topik tersebut menjadi jalur lanjutan setelah fondasi bahasa dikuasai.

## 2. Capaian pembelajaran

Setelah menyelesaikan program, peserta mampu:

1. Menyiapkan toolchain Rust, Cargo, VS Code, dan struktur proyek.
2. Menulis program Rust menggunakan variabel, tipe data, fungsi, percabangan, perulangan, dan pattern matching.
3. Menjelaskan ownership, move, borrowing, mutable reference, dan lifetime dasar dengan contoh.
4. Memodelkan data sensor menggunakan struct, enum, collections, dan module.
5. Menggunakan Option, Result, operator `?`, dan pesan error yang informatif.
6. Membaca dan menulis file, serta melakukan serialisasi/deserialisasi JSON menggunakan Serde.
7. Menulis unit test, menjalankan formatter, dan menggunakan Clippy.
8. Menghasilkan data JSONL yang tervalidasi untuk diproses oleh Python/Pandas.
9. Membaca pesan compiler dan memperbaiki kesalahan secara sistematis.

## 3. Peta kompetensi dan materi 28 hari

| Hari | Materi | Praktik utama | Bukti kompetensi |
|---:|---|---|---|
| 29 | Instalasi rustup, rustc, Cargo, VS Code | `cargo new`, `cargo run`, `cargo check` | Proyek berjalan |
| 30 | Variabel, mutability, shadowing, konstanta | Model nilai sensor | Program nilai sensor |
| 31 | Tipe skalar, compound, casting | Konversi satuan suhu/debit | Konversi tervalidasi |
| 32 | Operator dan control flow | Klasifikasi kondisi sensor | Status normal/waspada/bahaya |
| 33 | Fungsi, parameter, return, scope | Fungsi konversi dan validasi | Fungsi modular |
| 34 | String, `&str`, UTF-8 | Parsing ID perangkat | Parser ID |
| 35 | Review dan proyek mini CLI | Kalkulator ambang sensor | CLI sederhana |
| 36 | Ownership dan move semantics | Eksperimen pemindahan String | Penjelasan move |
| 37 | Borrowing dan reference | Fungsi baca data tanpa mengambil ownership | Fungsi berbasis reference |
| 38 | Mutable borrowing dan aturan aliasing | Update status sensor | Mutasi aman |
| 39 | Slice dan lifetime pengantar | Fungsi membaca potongan data | Fungsi slice |
| 40 | Struct, impl, method | Model SensorReading | Model data |
| 41 | Enum dan pattern matching | Status perangkat dan pesan error | State machine sederhana |
| 42 | Review ownership, struct, enum | Refactor model sensor | Model domain stabil |
| 43 | Vec, HashMap, iterator | Buffer dan agregasi pembacaan | Agregasi sederhana |
| 44 | Module, crate, visibility | Pisahkan model, validasi, dan I/O | Struktur modular |
| 45 | Option, Result, `?` | Validasi input dan error propagation | Error terkelola |
| 46 | Traits dan generics dasar | Trait untuk sumber pembacaan | Abstraksi sederhana |
| 47 | File I/O dan path | Tulis/baca file lokal | File data |
| 48 | Serde, JSON, JSONL | Serialize dan deserialize record | JSONL valid |
| 49 | Testing, rustfmt, Clippy | Unit test dan pemeriksaan kode | Test lulus |
| 50 | Kontrak data Rust–Python | Definisikan skema record | Data contract |
| 51 | Generator data sensor Rust | Simulasi data terukur | Dataset JSONL |
| 52 | Validasi dan penanganan data rusak | Uji nilai di luar rentang | Laporan validasi |
| 53 | Python membaca JSONL | Parsing dengan Pandas | DataFrame |
| 54 | Analisis time-series | Statistik dan grafik | Grafik analisis |
| 55 | Integrasi dan dokumentasi | Jalankan pipeline dari awal | Demo terulang |
| 56 | Uji akhir dan evaluasi | Presentasi capstone | Repositori dan laporan |

## 4. Strategi pembelajaran setiap sesi

- **15–20 menit:** baca konsep dan satu contoh kecil.
- **35–50 menit:** ketik ulang kode, jalankan, lalu modifikasi.
- **15–20 menit:** kerjakan latihan tanpa menyalin solusi.
- **5–10 menit:** catat error, penyebab, dan perbaikannya.

Aturan wajib: setiap contoh harus dijalankan. Peserta perlu mengubah input, menguji kondisi batas, dan menjelaskan mengapa kode bekerja. Menonton video atau membaca tutorial tidak dihitung sebagai bukti kompetensi.

## 5. Metode asesmen

| Komponen | Bobot | Indikator |
|---|---:|---|
| Pemahaman konsep | 20% | Mampu menjelaskan konsep dan trade-off |
| Implementasi | 25% | Kode benar, sesuai spesifikasi |
| Ownership dan error handling | 20% | Penggunaan reference dan Result tepat |
| Testing dan debugging | 15% | Test bermakna dan mampu membaca compiler |
| Kualitas kode | 10% | Struktur, naming, rustfmt, Clippy |
| Dokumentasi dan demo | 10% | README, instruksi run, hasil dapat direproduksi |

**Kriteria lulus yang disarankan:** nilai minimal 70/100 dan seluruh fungsi utama capstone berjalan. Nilai tinggi tidak boleh menutupi kegagalan memahami ownership atau validasi data.

## 6. Proyek akhir

**Judul:** Rust Sensor Data Collector dengan Python Analytics.

### Arsitektur
1. Rust menghasilkan atau menerima pembacaan sensor.
2. Rust memvalidasi timestamp, device_id, nilai, dan satuan.
3. Rust menyimpan record valid ke JSONL.
4. Python membaca JSONL dan memeriksa integritas data.
5. Pandas menghitung ringkasan dan tren.
6. Matplotlib menghasilkan grafik.

### Kontrak data minimal

```json
{
  "device_id": "ESP32-01",
  "timestamp": "2026-11-09T10:30:00Z",
  "sensor": "flow",
  "value": 12.5,
  "unit": "L/min"
}
```

Setiap baris file JSONL harus berisi satu objek JSON lengkap. Tetapkan rentang valid sesuai spesifikasi sensor yang benar-benar digunakan. Jangan menganggap satu rentang cocok untuk semua sensor.

### Pengujian minimum
- Nilai normal, batas minimum, dan batas maksimum.
- Nilai di bawah/di atas rentang.
- Timestamp atau device_id kosong.
- JSON rusak atau field hilang.
- File tidak ditemukan atau tidak dapat ditulis.
- Dataset kosong dan dataset dengan satu record.

## 7. Materi lanjutan setelah hari ke-56

Materi berikut tidak dipaksakan ke jalur pemula. Ambil setelah peserta nyaman dengan ownership, Result, collections, dan testing.

| Jalur | Materi | Mini project |
|---|---|---|
| Networking | TCP/UDP, HTTP client, MQTT | MQTT sensor collector |
| Concurrency | thread, channel, Arc, Mutex | Multi-source collector |
| Async | Tokio, async/await | Async MQTT/HTTP ingestion |
| Backend | Axum, REST API, SQLx | API data sensor |
| Data engineering | Polars, Arrow, Parquet | Pipeline data besar |
| Python interoperability | PyO3, maturin | Modul Rust dipanggil dari Python |
| Embedded | embedded-hal, no_std, target MCU | Firmware board yang didukung |
| Performance | Criterion, profiling, benchmark | Bandingkan bottleneck |

**Catatan teknis:** PyO3 bukan jalan pintas untuk mengubah semua kode Python menjadi Rust. Gunakan setelah ada fungsi komputasi yang terbukti menjadi bottleneck dan batas data antarbasa sudah jelas. Demikian juga embedded Rust membutuhkan pemilihan board, target, HAL, dan toolchain yang spesifik.

## 8. Referensi belajar

1. [The Rust Programming Language (The Book)](https://doc.rust-lang.org/book/) — acuan utama konsep bahasa.
2. [Rust by Example](https://doc.rust-lang.org/rust-by-example/) — contoh kecil yang dapat dijalankan.
3. [Rust Standard Library](https://doc.rust-lang.org/std/) — dokumentasi API standar.
4. [Kemal Codes Rust Tutorial](https://github.com/kemalcodes/rust-tutorial) — referensi proyek dan pengembangan aplikasi; gunakan sebagai bacaan pengayaan, bukan urutan wajib.
5. [Zero To Mastery: Learn Rust](https://zerotomastery.io/courses/learn-rust/) — alternatif materi video dan latihan terstruktur; akses kursus dapat berbayar.
6. [Ajay Gurav: Rust for Data Science and Machine Learning](https://ajaygurav.medium.com/zero-to-hero-mastering-rust-for-data-science-and-machine-learning-b97446c1833f) — gambaran integrasi Rust dan Python; bukan pengganti dokumentasi teknis PyO3.
7. [PyO3 User Guide](https://pyo3.rs/) — dokumentasi resmi integrasi Rust–Python.
8. [Serde Documentation](https://serde.rs/) — serialisasi dan deserialisasi data.

## 9. Prinsip penggunaan referensi

Urutan belajar utama mengikuti silabus dan tutorial lokal di repositori ini. Gunakan The Rust Book untuk konsep, Rust by Example untuk variasi contoh, ZTM untuk latihan tambahan, dan Kemal Codes untuk melihat bagaimana konsep dipakai dalam aplikasi lebih besar. Artikel Medium digunakan sebagai orientasi topik, lalu verifikasi implementasi melalui dokumentasi resmi.

Jangan menyalin proyek besar sebelum memahami dependensi, struktur, dan alur error-nya. Target program ini adalah kompetensi yang dapat dibuktikan melalui kode dan pengujian, bukan jumlah tutorial yang selesai ditonton.


## 10. Jalur lanjutan: Embedded Rust pada ESP32

Setelah Hari 56 dan fondasi Rust dikuasai, peserta dapat mengambil jalur lanjutan 14 sesi untuk membuat firmware ESP32. Materi meliputi `no_std`, target chip, toolchain Espressif, GPIO, tombol, PWM, ADC, UART, I2C, SPI, timer, interrupt, dan pengiriman telemetry.

Jalur ini **tidak dimasukkan ke target kelulusan 56 hari**, karena setup dan debugging perangkat fisik memerlukan waktu serta board yang spesifik. ESP32 klasik dan ESP32-C3 juga memakai target arsitektur berbeda. ESP8266 tidak boleh diasumsikan kompatibel dengan `esp-hal`.

Gunakan [Modul Embedded Rust untuk ESP32](EMBEDDED-RUST-ESP32.md) sebagai panduan praktik, termasuk tujuan sesi, contoh LED, proyek sensor node, batas dukungan, dan rubrik.
