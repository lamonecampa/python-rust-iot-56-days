# Standar Pembelajaran Ramah Pemula

Dokumen ini menjadi standar untuk seluruh materi Python hari 1–28, Rust hari 29–49, dan integrasi hari 50–56.

## Prinsip utama

Materi harus mengajar orang yang belum pernah menulis satu baris kode. Jangan menganggap peserta sudah memahami istilah seperti variabel, tipe data, compiler, terminal, atau fungsi.

Gunakan urutan tetap:

1. **Konteks nyata:** mulai dengan masalah sehari-hari atau kasus IoT yang mudah dibayangkan.
2. **Tujuan belajar:** tulis satu sampai tiga kemampuan yang bisa diamati.
3. **Kosakata baru:** definisikan istilah dengan bahasa sederhana.
4. **Visual block:** gambarkan input, proses, keputusan, perulangan, dan output.
5. **Algoritma:** tulis langkah-langkah menggunakan kalimat biasa.
6. **Flowchart/pseudocode:** tunjukkan alur sebelum kode.
7. **Prediksi:** minta peserta menebak hasil sebelum menjalankan program.
8. **Kode bertahap:** mulai dari contoh paling kecil, lalu tambah satu konsep.
9. **Bedah baris:** jelaskan setiap baris, simbol penting, dan alasan pemakaiannya.
10. **Simulasi manual:** telusuri nilai variabel langkah demi langkah.
11. **Jalankan program:** bandingkan hasil aktual dengan prediksi.
12. **Debugging:** tampilkan satu kesalahan umum, gejala, penyebab, dan perbaikannya.
13. **Latihan terbimbing:** soal serupa dengan petunjuk.
14. **Latihan mandiri:** soal baru tanpa petunjuk lengkap.
15. **Refleksi dan evaluasi:** peserta menjelaskan kembali konsep dengan kata-katanya sendiri.

## Aturan desain materi

- Satu konsep baru utama per pelajaran. Konsep lain yang dibutuhkan harus diulas singkat.
- Gunakan kalimat pendek dan satu instruksi per langkah.
- Jelaskan analogi, lalu jelaskan batas analogi tersebut agar tidak menyesatkan.
- Jangan menggunakan istilah teknis sebelum definisinya diberikan.
- Jangan hanya memberi kode jadi. Tunjukkan proses berpikir dan perubahan kode.
- Sertakan output yang diharapkan dan versi uji yang mengubah input.
- Gunakan nilai batas, nilai normal, dan nilai tidak valid saat menguji kondisi.
- Berikan petunjuk bertingkat: petunjuk konsep, petunjuk langkah, baru contoh solusi.
- Jangan memperkenalkan Rust ownership/borrowing sekaligus dengan banyak konsep baru.
- Tandai kode yang berjalan di desktop, MicroPython ESP32, atau embedded Rust. Ketiganya bukan lingkungan yang otomatis saling kompatibel.
- Setiap contoh perangkat keras harus mencantumkan asumsi board, GPIO, tegangan, wiring, dan risiko jika relevan.
- Aksesibilitas: jangan mengandalkan warna saja; sertakan label teks pada diagram.

## Template wajib setiap pelajaran

### A. Masalah sehari-hari
Jelaskan kebutuhan yang akan diselesaikan.

### B. Tujuan
Setelah belajar, peserta mampu melakukan tindakan yang dapat diuji.

### C. Kosakata
| Istilah | Arti sederhana |
|---|---|

### D. Visual block
Tampilkan urutan blok dengan label dan arah panah. Untuk keputusan, tampilkan cabang YA/TIDAK. Untuk perulangan, tunjukkan jalur kembali.

### E. Algoritma dan pseudocode
Tuliskan langkah dalam bahasa sehari-hari dan bentuk pseudocode.

### F. Prediksi output
Berikan input dan minta peserta menebak hasilnya sebelum menjalankan kode.

### G. Kode dan bedah baris
Tampilkan kode minimal. Jelaskan fungsi setiap baris, simbol, indentasi, kurung, titik koma, dan tipe data yang penting.

### H. Simulasi jejak program
| Langkah | Nilai variabel | Kondisi | Tindakan/output |
|---|---|---|---|

### I. Praktik
Berikan satu latihan terbimbing dan satu latihan mandiri.

### J. Debugging
| Kesalahan | Mengapa terjadi | Cara memperbaiki |
|---|---|---|

### K. Evaluasi
Minta peserta menjelaskan alur, memprediksi output, memodifikasi program, dan memperbaiki satu kesalahan.

## Jalur belajar dan capaian

| Fase | Materi | Bukti kompetensi |
|---|---|---|
| Python 1–7 | Output, input, variabel, tipe, operator, kondisi | Program interaktif sederhana |
| Python 8–14 | Perulangan, koleksi, fungsi | Program pengolah data kecil |
| Python 15–21 | File, CSV, JSON, error, modul, OOP dasar | Membaca dan memvalidasi data |
| Python 22–28 | NumPy, Pandas, visualisasi, statistik, mini proyek | Analisis dataset dan grafik |
| Rust 29–35 | Toolchain, sintaks, fungsi, String, control flow | Program terminal terstruktur |
| Rust 36–42 | Ownership, borrowing, slices, struct, enum, collections | Memodelkan data sensor dengan aman |
| Rust 43–49 | Result, traits, file, Serde, testing | Collector JSONL teruji |
| Integrasi 50–56 | Kontrak data, validasi, analisis, laporan | Pipeline Rust ke Python berjalan |

## Cara mengajar konsep Rust yang sulit

### Ownership: nilai memiliki satu pemilik
Gunakan analogi barang yang dipinjamkan atau dipindahkan. Tegaskan bahwa analogi hanya membantu pemahaman: aturan ownership adalah aturan bahasa/compiler, bukan aturan sosial.

- Move: kepemilikan nilai berpindah.
- Borrow `&T`: meminjam untuk dibaca.
- Mutable borrow `&mut T`: meminjam untuk diubah dengan aturan eksklusif.
- Scope: area kode tempat binding berlaku.

Tampilkan diagram panah pemilik sebelum dan sesudah operasi. Jangan mulai dari lifetime formal.

### Result dan Option: hasil tidak selalu berhasil/tersedia
Gunakan dua cabang visual:
- `Some(value)` atau `Ok(value)`: ada nilai/berhasil.
- `None` atau `Err(error)`: tidak ada nilai/gagal.
Ajarkan `match` sebelum operator `?`.

### Tipe data dan memori
Gunakan tabel nilai dan tipe. Hindari klaim bahwa Rust selalu lebih cepat atau lebih aman dalam semua kondisi; jelaskan bahwa manfaat bergantung pada desain dan implementasi.

## Evaluasi mingguan

Setiap minggu memiliki:
1. Kuis konsep (20%).
2. Menyusun visual block/flowchart (20%).
3. Praktik coding (30%).
4. Debugging (15%).
5. Penjelasan lisan/tertulis (15%).

Ambang penguasaan yang disarankan: 70%. Jika belum tercapai, ulangi konsep yang belum dikuasai sebelum pindah ke materi yang bergantung padanya.

## Rubrik pemahaman

| Kriteria | 4 - Mandiri | 3 - Cukup | 2 - Perlu bantuan | 1 - Belum paham |
|---|---|---|---|---|
| Menjelaskan masalah | Jelas dan tepat | Sebagian besar tepat | Masih kabur | Tidak dapat menjelaskan |
| Membuat alur | Lengkap dan benar | Ada kekurangan kecil | Banyak langkah hilang | Tidak runtut |
| Memprediksi output | Tepat pada kasus normal dan batas | Tepat pada kasus normal | Perlu petunjuk | Tidak dapat memprediksi |
| Menulis/mengubah kode | Mandiri | Dengan sedikit bantuan | Meniru contoh | Tidak dapat memulai |
| Debugging | Menemukan sebab dan memperbaiki | Memperbaiki dengan petunjuk | Coba-coba tanpa alasan | Tidak dapat mendiagnosis |

## Pengujian kualitas materi sebelum dipakai

Minta satu orang yang belum pernah coding mencoba pelajaran tanpa penjelasan tambahan. Catat:
- istilah yang tidak dipahami;
- langkah yang membuat peserta berhenti;
- kesalahan yang berulang;
- waktu sampai latihan selesai;
- apakah peserta dapat menjelaskan kembali konsep.

Perbaiki materi berdasarkan hasil uji tersebut. Jangan menyimpulkan materi mudah hanya karena penulisnya sudah memahami topik.
