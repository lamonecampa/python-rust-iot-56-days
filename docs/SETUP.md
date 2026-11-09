# Setup Lingkungan

## VS Code
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
