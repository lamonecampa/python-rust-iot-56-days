# Embedded Rust untuk ESP32

**Posisi:** jalur lanjutan setelah fondasi Rust Hari 29–56  
**Durasi rekomendasi:** 14 sesi praktik, 1–2 jam/sesi  
**Target awal:** ESP32 klasik (Xtensa) dan ESP32-C3 (RISC-V)  
**Tool utama:** Rust, Cargo, esp-rs, esp-hal, espflash, VS Code

> Modul ini adalah jalur embedded lanjutan, bukan pengganti kurikulum 56 hari. Jangan mulai dari mikrokontroler sebelum nyaman dengan fungsi, struct, enum, ownership, borrowing, Result, dan debugging Cargo.

## 1. Tujuan pembelajaran

Setelah menyelesaikan modul, peserta diharapkan mampu:

1. Menjelaskan perbedaan program Rust desktop (`std`) dan firmware embedded (`no_std`).
2. Memilih target chip dan toolchain yang sesuai dengan board.
3. Membuat proyek firmware ESP32 dengan template yang sesuai versi ekosistem.
4. Mengendalikan GPIO untuk LED dan tombol.
5. Membaca ADC dan berkomunikasi melalui UART, I2C, serta SPI sesuai dukungan chip.
6. Menjelaskan perbedaan blocking dan asynchronous I/O.
7. Mengirim data sensor ke sistem IoT, jika dukungan Wi-Fi untuk chip dan versi crate yang dipilih sudah memadai.
8. Menguji firmware pada perangkat fisik dan mendokumentasikan konfigurasi pin.

## 2. Pilih board sebelum menulis kode

| Board/chip | Arsitektur | Catatan pembelajaran |
|---|---|---|
| ESP32-WROOM-32 / DevKit | Xtensa | Didukung ekosistem Rust Espressif; perhatikan konfigurasi toolchain Xtensa |
| ESP32-C3 Super Mini | RISC-V | Pilihan awal yang baik untuk belajar embedded Rust |
| ESP32-S3 | Xtensa | Cocok untuk eksperimen lebih lanjut; cek dukungan peripheral yang diperlukan |
| ESP32-CAM | Umumnya ESP32 klasik | Bisa dipelajari bertahap, tetapi kamera dan pin yang dipakai board membuatnya bukan board pertama yang paling sederhana |
| ESP8266 / NodeMCU ESP8266 | Xtensa LX106 | Bukan target `esp-hal` utama pada modul ini; jangan memakai instruksi ESP32 secara langsung |

**Rekomendasi:** mulai dengan ESP32-C3 Super Mini atau ESP32 DevKit V1 yang memiliki dokumentasi pin jelas. Bila hanya memiliki ESP32-CAM, mulai dari identifikasi chip dan pin yang benar, bukan menyalin contoh pin board lain.

### Pemeriksaan board

Sebelum praktik, catat:
- Nama board dan chip yang tercetak pada modul.
- USB-to-serial bridge yang digunakan.
- Port serial yang muncul saat board disambungkan.
- LED onboard: apakah tersedia, aktif HIGH atau aktif LOW, dan terhubung ke GPIO berapa.
- GPIO yang aman dipakai serta pin yang terhubung ke flash, PSRAM, boot strapping, kamera, atau peripheral onboard.

Jangan menganggap GPIO0 selalu merupakan pin LED. Contoh dokumentasi yang menggunakan GPIO0 adalah contoh API, bukan jaminan pin tersebut cocok untuk semua board.

## 3. Ekosistem Rust pada ESP32

| Alat/crate | Peran |
|---|---|
| `rustup` / Rust toolchain | Compiler dan pengelolaan toolchain |
| `cargo` | Build system dan dependency manager |
| `esp-rs` | Ekosistem Rust untuk chip Espressif |
| `esp-hal` | Hardware Abstraction Layer bare-metal `no_std` |
| `esp-idf-hal` | HAL yang menggunakan ESP-IDF dan lingkungan `std` |
| `espflash` | Flash firmware dan serial monitor |
| `esp-generate` | Generator proyek untuk konfigurasi target Espressif |
| `esp-wifi` | Integrasi Wi-Fi/Bluetooth pada kombinasi chip dan versi yang didukung |
| `embassy` | Ekosistem async embedded |

### Memilih esp-hal atau esp-idf-hal

- **esp-hal:** jalur bare-metal `no_std`, memberi kontrol lebih langsung atas peripheral. Ini jalur utama modul pemula embedded.
- **esp-idf-hal:** memakai ESP-IDF, cocok bila membutuhkan fitur ESP-IDF atau API yang lebih dekat dengan ekosistem ESP-IDF.

Keduanya bukan nama berbeda untuk hal yang sama. Contoh kode, konfigurasi, dan dependency tidak boleh dicampur sembarangan.

## 4. Persiapan perangkat lunak

Gunakan laptop/desktop sebagai lingkungan build utama. Android/Termux dapat dipakai untuk membaca materi atau eksperimen tertentu, tetapi bukan lingkungan utama yang direkomendasikan untuk cross-compilation dan debugging firmware.

1. Pasang VS Code.
2. Pasang Rust melalui [rustup.rs](https://rustup.rs/).
3. Pasang extension `rust-analyzer`.
4. Pasang driver USB-to-serial sesuai chip bridge board (misalnya CP210x atau CH34x).
5. Ikuti langkah target dan toolchain dari [The Rust on ESP Book](https://docs.espressif.com/projects/rust/book/).
6. Pasang flasher:

```bash
cargo install espflash --locked
espflash --version
```

Versi toolchain, target, dan konfigurasi linker berbeda menurut chip serta template proyek. Gunakan generator/template resmi yang sesuai, lalu simpan konfigurasi yang dihasilkan. Jangan menyalin konfigurasi lama dari tutorial yang tidak menyebut versi.

Referensi setup resmi:
- [The Rust on ESP Book](https://docs.espressif.com/projects/rust/book/)
- [esp-rs GitHub](https://github.com/esp-rs)
- [esp-hal documentation](https://docs.espressif.com/projects/rust/esp-hal/)
- [espflash](https://docs.espressif.com/projects/rust/book/getting-started/tooling/espflash.html)

## 5. Alur kerja proyek firmware

Alur umum:

```text
[Identifikasi chip dan board]
          |
          v
[Pilih target dan template]
          |
          v
[Konfigurasi Cargo dan toolchain]
          |
          v
[cargo check / cargo build]
          |
          v
[Hubungkan board via USB]
          |
          v
[Flash firmware dengan espflash]
          |
          v
[Amati serial log dan perilaku GPIO]
          |
          v
[Uji, catat hasil, dan debugging]
```

Contoh perintah pemeriksaan proyek setelah template dibuat:

```bash
cargo check
cargo build
cargo fmt
```

Perintah flash bergantung pada template dan port serial. Ikuti instruksi yang dihasilkan proyek atau dokumentasi versi `espflash` yang dipakai. Pada Linux, port biasanya berbentuk `/dev/ttyUSB0` atau `/dev/ttyACM0`; pada Windows biasanya `COMx`. Nama port bukan nilai universal.

## 6. Praktik pertama: LED berkedip

Tujuan: memahami hubungan kode Rust, GPIO, dan perangkat fisik.

Contoh berikut menunjukkan pola API `esp-hal` modern. Ini **contoh ilustratif**, bukan proyek lengkap yang bisa ditempel begitu saja ke sembarang Cargo.toml. Gunakan template resmi untuk chip yang dipilih, lalu sesuaikan nama peripheral dan GPIO berdasarkan pinout board.

```rust
#![no_std]
#![no_main]

use esp_hal::{
    clock::CpuClock,
    delay::Delay,
    gpio::{Level, Output, OutputConfig},
    main,
};
use esp_backtrace as _;

#[main]
fn main() -> ! {
    let config = esp_hal::Config::default()
        .with_cpu_clock(CpuClock::max());

    let peripherals = esp_hal::init(config);

    // Ganti GPIO2 dengan pin LED yang benar untuk board Anda.
    let mut led = Output::new(
        peripherals.GPIO2,
        Level::Low,
        OutputConfig::default(),
    );

    let delay = Delay::new();

    loop {
        led.toggle();
        delay.delay_millis(500);
    }
}
```

**Penting:** nama GPIO pada contoh harus tersedia untuk chip yang dipilih. Pada beberapa board LED onboard aktif LOW, pada board lain aktif HIGH, dan beberapa board tidak memiliki LED onboard. Pastikan juga konfigurasi pin sesuai template `esp-hal` yang digunakan. API crate dapat berubah; periksa contoh pada tag rilis yang sama dengan dependency proyek.

### Penjelasan blok

1. `#![no_std]`: firmware tidak memakai standard library desktop.
2. `#![no_main]`: entry point ditangani runtime/macro embedded.
3. `esp_hal::init`: menginisialisasi peripheral chip.
4. `Output::new`: mengonfigurasi satu GPIO sebagai output.
5. `led.toggle()`: membalik level output.
6. `delay.delay_millis(500)`: menunggu sekitar 500 ms.
7. `loop`: mengulangi aksi selama perangkat menyala.

### Prediksi dan pengujian

- Apa yang terjadi jika delay diubah menjadi 100 ms?
- Mengapa LED bisa terlihat mati walaupun firmware berjalan?
- Bagaimana perilaku berubah jika LED aktif LOW?
- Apa perbedaan kesalahan compile, gagal flash, dan salah pemetaan pin?

Bukti praktik: video/foto LED, nama board, GPIO yang digunakan, versi dependency, log build, dan catatan hasil.

## 7. Roadmap praktik 14 sesi

| Sesi | Materi | Praktik dan hasil |
|---:|---|---|
| 1 | Arsitektur ESP32, board, pinout, USB serial | Identifikasi chip dan peta pin |
| 2 | Rust embedded, `no_std`, target, toolchain | Proyek firmware berhasil di-`check` |
| 3 | GPIO output | LED blink |
| 4 | GPIO input dan pull-up/pull-down | Tombol mengendalikan LED |
| 5 | Debouncing dan state sederhana | Tombol tidak menghasilkan trigger berulang |
| 6 | PWM/LEDC | Atur kecerahan LED atau kecepatan motor kecil melalui driver yang sesuai |
| 7 | ADC | Baca potensiometer/sensor analog dan lakukan kalibrasi dasar |
| 8 | UART | Komunikasi dengan GPS atau serial device |
| 9 | I2C | Baca sensor I2C |
| 10 | SPI | Komunikasi dengan peripheral SPI, misalnya modul LoRa jika driver dan konfigurasi chip tersedia |
| 11 | Timer, interrupt, dan state machine | Sampling berkala tanpa loop blocking yang tidak perlu |
| 12 | Wi-Fi dan HTTP/MQTT | Kirim telemetry bila dukungan chip/crate yang dipilih stabil dan tersedia |
| 13 | Struktur data, error handling, dan logging | Firmware sensor modular dengan penanganan error |
| 14 | Mini project dan uji perangkat | Demo firmware, diagram wiring, dan laporan pengujian |

Tidak semua sesi dapat dikerjakan dengan semua varian ESP32. Cek matriks peripheral dan status API untuk chip yang dipakai sebelum memilih proyek.

## 8. Mini project: Rust ESP32 Sensor Node

### Arsitektur target

```text
[Sensor]
   |
   v
[ESP32 + Firmware Rust]
   |
   +--> [Validasi pembacaan]
   |
   +--> [Serial log / UART]
   |
   +--> [Wi-Fi jika didukung]
              |
              v
       [MQTT / HTTP Gateway]
              |
              v
       [Python Analytics]
              |
              v
       [Grafik dan dashboard]
```

### Tahapan pengembangan

1. Tahap A: LED dan tombol, tanpa sensor eksternal.
2. Tahap B: baca sensor melalui ADC/I2C/UART.
3. Tahap C: validasi nilai, satuan, dan status sensor.
4. Tahap D: kirim data serial ke komputer, lalu parse dengan Python.
5. Tahap E: tambahkan Wi-Fi dan MQTT/HTTP setelah jalur dasar stabil.

Contoh payload data:

```json
{
  "device_id": "ESP32-C3-01",
  "sensor": "temperature",
  "value": 28.4,
  "unit": "C",
  "status": "valid"
}
```

Untuk tahap awal, kirim lewat UART/USB serial lebih mudah di-debug daripada langsung menambahkan Wi-Fi, MQTT, dan dashboard sekaligus.

## 9. Catatan khusus untuk perangkat yang sering digunakan di proyek IoT

- **ESP32 klasik:** target yang didukung, tetapi membutuhkan toolchain Xtensa yang sesuai.
- **ESP32-C3:** target RISC-V; konfigurasi toolchain berbeda dari ESP32 Xtensa.
- **ESP32-CAM:** mulai dari GPIO/serial yang tidak bentrok dengan kamera, flash, PSRAM, atau SD card. Integrasi kamera merupakan topik lanjutan.
- **LoRa SX1278/Ra-02:** dapat menjadi proyek SPI lanjutan, tetapi pastikan driver Rust yang dipilih kompatibel dengan versi `embedded-hal` dan chip.
- **GPS NEO-7M:** cocok untuk praktik UART.
- **YF-S201:** cocok untuk praktik input pulsa/interrupt, tetapi perlu perhatian pada level tegangan dan rangkaian conditioning.
- **ESP8266:** jangan gunakan konfigurasi `esp-hal` untuk ESP32. Dukungan dan jalur Rust-nya berbeda serta tidak menjadi target modul ini.

Periksa tegangan logika, arus, level pin, dan datasheet sebelum wiring. GPIO ESP32 bukan input 5 V tolerant.

## 10. Rubrik penilaian

| Aspek | Bobot |
|---|---:|
| Pemahaman arsitektur, target, dan toolchain | 15% |
| Implementasi peripheral dan wiring | 25% |
| Struktur kode, ownership, dan error handling | 20% |
| Pengujian dan debugging | 20% |
| Dokumentasi, diagram, dan demo | 20% |

**Kriteria lulus:** firmware berhasil dibangun dan di-flash pada board yang disebutkan, fungsi utama diuji, wiring terdokumentasi, dan peserta dapat menjelaskan alur program. Screenshot kode saja bukan bukti perangkat bekerja.

## 11. Referensi resmi dan proyek

1. [The Rust on ESP Book](https://docs.espressif.com/projects/rust/book/) — panduan utama instalasi dan pengembangan.
2. [esp-hal repository](https://github.com/esp-rs/esp-hal) — HAL dan contoh berdasarkan rilis.
3. [esp-hal documentation](https://docs.espressif.com/projects/rust/esp-hal/) — dokumentasi API dan matriks dukungan peripheral.
4. [espflash guide](https://docs.espressif.com/projects/rust/book/getting-started/tooling/espflash.html) — flashing dan serial monitor.
5. [esp-rs organization](https://github.com/esp-rs) — proyek dan tooling ekosistem.

**Aturan versi:** jangan mencampur contoh `main` branch, dokumentasi versi lama, dan dependency versi baru. Pilih satu rilis `esp-hal`, gunakan contoh dari rilis yang sama, lalu catat versi crate di repository proyek.
