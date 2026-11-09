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
