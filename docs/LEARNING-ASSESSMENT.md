# Panduan Belajar Terintegrasi: Latihan, Simulasi, dan Evaluasi

## Cara memakai laboratorium visual

Buka [Visual Lab](../visual-lab/index.html) di browser. Lab ini adalah alat latihan logika sederhana, bukan compiler Python/Rust. Gunakan untuk mengubah input, melihat cabang keputusan, memprediksi hasil, dan membandingkannya dengan kode.

## Jadwal evaluasi mingguan

| Minggu | Materi | Kuis | Praktik wajib | Bukti |
|---|---|---|---|---|
| 1 | Python dasar dan alur program | Variabel, input, tipe, operator | Program konversi suhu | Kode + penjelasan |
| 2 | Kondisi, loop, koleksi, fungsi | Prediksi cabang dan iterasi | Alarm suhu | Flowchart + kode |
| 3 | File, CSV, JSON, error, modul | Baca data dan tangani error | Pembaca data sensor | File output + kasus error |
| 4 | OOP, NumPy, Pandas, grafik, statistik | Interpretasi data | Analisis CSV | Grafik + laporan |
| 5 | Rust dasar dan control flow | Tipe, fungsi, String | Program terminal | Kode + cargo check |
| 6 | Ownership, borrowing, struct, enum | Trace ownership/reference | Model sensor | Diagram memori konseptual |
| 7 | Collections, Result, Serde, testing | Error handling dan JSONL | Collector | Unit test + JSONL |
| 8 | Integrasi | Kontrak data dan validasi | Pipeline end-to-end | Grafik dan demo |

## Format kuis yang harus digunakan

Setiap minggu berisi:
- 5 soal pilihan ganda untuk istilah dan konsep;
- 3 soal prediksi output;
- 1 tugas menggambar visual block/flowchart;
- 1 tugas debugging;
- 1 praktik mini yang dapat dijalankan.

Jangan hanya menilai jawaban akhir. Nilai juga alasan, alur, dan kemampuan menjelaskan kesalahan.

## Format umpan balik

Untuk setiap jawaban salah, tampilkan:
1. Bagian yang sudah benar.
2. Konsep yang keliru.
3. Petunjuk kecil.
4. Kesempatan mencoba ulang.
5. Pembahasan solusi setelah percobaan.

Hindari langsung memberikan jawaban penuh pada percobaan pertama.

## Kriteria kelulusan

- Nilai minimal 70% pada kuis dan praktik.
- Dapat menggambar alur sebelum menulis kode.
- Dapat memprediksi output untuk minimal satu kasus normal dan satu kasus batas.
- Dapat mengubah kode kecil tanpa menyalin seluruh contoh.
- Dapat menjelaskan satu kesalahan dan cara memperbaikinya.

## Batasan dan integritas teknis

- Visual Lab tidak menjalankan compiler Python atau Rust.
- Kode MicroPython ESP32 memerlukan board dan firmware MicroPython yang sesuai.
- Embedded Rust memerlukan target, toolchain, HAL/framework, dan konfigurasi perangkat yang tepat.
- Capstone awal memakai data simulasi; jangan menyebutnya sebagai deployment perangkat fisik.
