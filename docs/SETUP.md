# Setup Lingkungan

## VS Code di laptop/desktop

Pasang VS Code, extension Python (Microsoft), dan rust-analyzer. Buka folder repository dan gunakan terminal terintegrasi.

## Python

Pasang Python 3.11+. Verifikasi `python --version`.

```bash
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# Linux/macOS: source .venv/bin/activate
python -m pip install -r python/requirements.txt
```

## Rust

Pasang rustup dari https://rustup.rs/ lalu verifikasi:

```bash
rustc --version
cargo --version
rustup update
cargo new latihan-rust
cd latihan-rust
cargo run
cargo fmt
cargo test
```

Jangan commit token/password. Gunakan virtual environment untuk paket Python. Jika perintah tidak dikenali, buka ulang terminal dan periksa PATH.

## Belajar melalui Android

Tidak harus selalu memakai laptop. Baca [Panduan Belajar Python dan Rust melalui Android](ANDROID-LEARNING.md) untuk:
- Pydroid 3 untuk menjalankan Python secara lokal.
- Termux untuk Python, Git, dan latihan Rust/Cargo.
- Tutorial browser seperti W3Schools.
- Sinkronisasi latihan melalui GitHub.
- Batasan build dan dependency di Android.

**Catatan:** Android cocok untuk latihan dan proyek kecil. Build Rust besar, paket Python native, debugging kompleks, dan pekerjaan data berat lebih tepat dilakukan di laptop atau server remote.


## Setup Embedded Rust untuk ESP32

Pengembangan firmware ESP32 adalah jalur terpisah dari Rust desktop. Ikuti [Panduan Embedded Rust untuk ESP32](EMBEDDED-RUST-ESP32.md), karena target compiler, linker, konfigurasi chip, dan proses flashing bergantung pada board.

Persiapan umum:
- VS Code dan `rust-analyzer`.
- Rust melalui `rustup`.
- Driver USB-to-serial yang sesuai board.
- Template proyek resmi untuk chip yang dipakai.
- `espflash`, dapat dipasang dengan `cargo install espflash --locked`.

Jangan menyalin konfigurasi ESP32 klasik ke ESP32-C3. ESP32 klasik menggunakan Xtensa, sedangkan ESP32-C3 menggunakan RISC-V. ESP8266/NodeMCU ESP8266 juga bukan target `esp-hal` pada panduan ini.
