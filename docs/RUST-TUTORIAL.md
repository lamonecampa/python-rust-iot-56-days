# Tutorial Rust Bertahap untuk IoT dan Analisis Data

Panduan praktik Rust untuk peserta yang sudah menyelesaikan Python dasar. Materi ini dirancang untuk Hari 29–49, lalu dilanjutkan integrasi pada Hari 50–56.

**Waktu:** 1–2 jam per hari  
**Editor:** VS Code  
**Toolchain:** rustup, rustc, Cargo  
**Fokus proyek:** data collector sensor yang menghasilkan JSONL untuk analisis Python.

## Cara menggunakan tutorial

Untuk setiap bab:
1. Baca tujuan dan konsep.
2. Buat proyek atau file sesuai instruksi.
3. Ketik kode sendiri, jangan hanya copy-paste.
4. Jalankan perintah Cargo.
5. Ubah nilai dan buat satu kesalahan dengan sengaja.
6. Baca pesan compiler, perbaiki, lalu tulis kesimpulan.

Perintah dasar:

```bash
rustc --version
cargo --version
cargo new rust_sensor_lab
cd rust_sensor_lab
cargo run
cargo check
cargo fmt
cargo clippy
cargo test
```

Cargo mengelola proyek, dependency, build, test, dan metadata. Untuk proyek belajar, biasakan menjalankan perintah dari folder yang berisi `Cargo.toml`.

## Bab 1. Variabel, mutability, dan tipe data

Rust menggunakan tipe statis. Variabel tidak dapat diubah kecuali dideklarasikan dengan `mut`.

```rust
fn main() {
    let device_id = "ESP32-01";
    let mut temperature: f32 = 27.5;

    println!("Device: {device_id}");
    println!("Suhu awal: {temperature:.1} C");

    temperature = 28.0;
    println!("Suhu terbaru: {temperature:.1} C");
}
```

**Penjelasan:**
- `let` membuat binding immutable.
- `let mut` mengizinkan perubahan nilai.
- `&str` adalah string slice, cocok untuk teks literal.
- `f32` adalah bilangan pecahan 32-bit.
- `println!` adalah macro, ditandai tanda seru.

**Latihan:** buat variabel `flow_rate: f32`, `pressure: f32`, dan `is_online: bool`. Cetak seluruh nilai dengan satuan yang benar.

**Kesalahan yang perlu dicoba:** hapus `mut`, lalu ubah nilai. Amati pesan compiler.

## Bab 2. Fungsi dan control flow

```rust
fn classify_temperature(value: f32) -> &'static str {
    if value >= 40.0 {
        "BAHAYA"
    } else if value >= 35.0 {
        "WASPADA"
    } else {
        "NORMAL"
    }
}

fn main() {
    for temperature in [29.5, 36.2, 41.0] {
        println!("{temperature}: {}", classify_temperature(temperature));
    }
}
```

Ekspresi terakhir pada fungsi menjadi nilai kembalian jika tidak diakhiri titik koma. `if` adalah expression. `for` melakukan iterasi atas array.

**Latihan:** buat fungsi `is_valid_flow(value: f32) -> bool` berdasarkan rentang yang ditetapkan sendiri. Jelaskan sumber rentang tersebut, jangan asal memilih angka.

## Bab 3. String dan perbedaan String dengan &str

```rust
fn print_device(name: &str) {
    println!("Perangkat: {name}");
}

fn main() {
    let fixed_name: &str = "ESP32-01";
    let owned_name: String = String::from("ESP32-02");

    print_device(fixed_name);
    print_device(&owned_name);
}
```

`String` menyimpan teks yang dimiliki dan dapat tumbuh. `&str` adalah view/referensi ke teks. Fungsi yang hanya perlu membaca teks sering lebih fleksibel menerima `&str`.

**Latihan:** terima ID perangkat dari input terminal, simpan sebagai String, lalu kirim sebagai `&str` ke fungsi validasi.

## Bab 4. Ownership dan move

Ownership adalah aturan inti Rust untuk mengelola memori tanpa garbage collector. Setiap nilai memiliki owner; ketika owner keluar dari scope, nilai dibersihkan. Assignment pada tipe seperti String dapat memindahkan ownership.

```rust
fn main() {
    let first = String::from("ESP32-01");
    let second = first;

    println!("{second}");
    // println!("{first}"); // error: ownership sudah dipindahkan
}
```

Jangan menghafal bahwa semua assignment memindahkan nilai. Tipe sederhana seperti integer yang menerapkan trait `Copy` disalin. String umumnya dipindahkan.

**Latihan:** buat fungsi yang menerima String by value. Panggil fungsi tersebut, lalu coba gunakan variabel asal. Perbaiki dengan memilih salah satu: meminjam reference atau clone jika memang perlu salinan terpisah.

## Bab 5. Borrowing dan references

Borrowing memungkinkan fungsi mengakses data tanpa mengambil ownership.

```rust
fn count_chars(text: &String) -> usize {
    text.len()
}

fn main() {
    let device = String::from("ESP32-CAM");
    let count = count_chars(&device);

    println!("{device} memiliki {count} byte");
}
```

`&String` adalah immutable reference. Untuk fungsi pembaca teks, `&str` biasanya lebih umum:

```rust
fn count_bytes(text: &str) -> usize {
    text.len()
}
```

**Catatan:** `len()` menghitung byte UTF-8, bukan selalu jumlah karakter yang terlihat.

## Bab 6. Mutable borrowing dan aturan aliasing

```rust
fn add_offset(value: &mut f32, offset: f32) {
    *value += offset;
}

fn main() {
    let mut temperature = 27.0;
    add_offset(&mut temperature, 0.5);
    println!("{temperature}");
}
```

- `&mut T` adalah mutable reference.
- `*` melakukan dereference untuk mengakses nilai melalui reference.
- Pada satu waktu, Rust mencegah kombinasi aliasing yang dapat menyebabkan data race atau perubahan tak terduga.

**Latihan:** buat fungsi yang memperbarui nilai flow rate. Pastikan tidak membuat dua mutable reference aktif ke variabel yang sama.

## Bab 7. Slices dan lifetime pengantar

```rust
fn first_reading(values: &[f32]) -> Option<f32> {
    values.first().copied()
}

fn main() {
    let readings = vec![12.1, 12.4, 12.8];
    println!("{:?}", first_reading(&readings));
}
```

Slice `&[f32]` meminjam bagian data tanpa mengambil ownership seluruh vector. `Option<f32>` menyatakan bahwa hasil mungkin ada atau tidak ada.

Lifetime menjelaskan berapa lama reference tetap valid. Pada tahap ini, pahami bahwa Rust menolak reference yang berpotensi menunjuk ke data yang sudah tidak hidup. Jangan menambahkan anotasi lifetime secara mekanis; compiler sering dapat melakukan elision.

## Bab 8. Struct dan impl

```rust
#[derive(Debug, Clone)]
struct SensorReading {
    device_id: String,
    sensor: String,
    value: f32,
    unit: String,
}

impl SensorReading {
    fn is_valid(&self) -> bool {
        self.value.is_finite()
    }

    fn describe(&self) -> String {
        format!("{}: {} {} ({})",
            self.device_id, self.value, self.unit, self.sensor)
    }
}

fn main() {
    let reading = SensorReading {
        device_id: String::from("ESP32-01"),
        sensor: String::from("flow"),
        value: 12.5,
        unit: String::from("L/min"),
    };

    println!("{:?}", reading);
    println!("{}", reading.describe());
    println!("Valid: {}", reading.is_valid());
}
```

Struct mengelompokkan field yang berkaitan. `impl` menambahkan method. `&self` berarti method membaca instance tanpa mengambil ownership.

**Latihan:** tambahkan timestamp sebagai String dan buat method yang memeriksa device_id tidak kosong.

## Bab 9. Enum dan pattern matching

```rust
#[derive(Debug)]
enum DeviceStatus {
    Online,
    Offline,
    Warning(String),
}

fn status_message(status: &DeviceStatus) -> String {
    match status {
        DeviceStatus::Online => "Perangkat aktif".to_string(),
        DeviceStatus::Offline => "Perangkat terputus".to_string(),
        DeviceStatus::Warning(message) => format!("Peringatan: {message}"),
    }
}

fn main() {
    let status = DeviceStatus::Warning("debit tinggi".to_string());
    println!("{}", status_message(&status));
}
```

Enum menyatakan pilihan state yang eksplisit. `match` memaksa semua kemungkinan pola ditangani, kecuali digunakan wildcard.

**Latihan:** tambahkan status Maintenance dan tangani seluruh varian.

## Bab 10. Collections dan iterators

```rust
use std::collections::HashMap;

fn main() {
    let readings = vec![12.1_f32, 12.4, 11.9, 12.6];
    let average = readings.iter().sum::<f32>() / readings.len() as f32;

    let mut counts = HashMap::new();
    counts.insert("flow", readings.len());

    println!("Rata-rata: {average:.2}");
    println!("Jumlah flow: {:?}", counts.get("flow"));
}
```

- `Vec<T>` menyimpan urutan elemen bertipe sama.
- `HashMap<K, V>` menyimpan pasangan key-value.
- `iter()` meminjam elemen; `into_iter()` dapat mengambil ownership, tergantung konteks.
- Jangan menghitung rata-rata vector kosong tanpa memeriksa panjangnya.

**Latihan:** hitung minimum, maksimum, dan rata-rata dengan penanganan dataset kosong.

## Bab 11. Modules dan struktur proyek

Pisahkan kode berdasarkan tanggung jawab, misalnya:
- `model.rs`: struct dan enum.
- `validation.rs`: aturan validasi.
- `storage.rs`: file I/O.
- `main.rs`: alur program.

Gunakan `mod` untuk mendeklarasikan module dan `pub` hanya pada item yang perlu diakses dari luar module. Jangan membuat semua item public tanpa alasan.

**Latihan:** pindahkan struct SensorReading dari main.rs ke model.rs dan gunakan dari main.

## Bab 12. Option, Result, dan error handling

```rust
fn parse_flow(input: &str) -> Result<f32, String> {
    let value: f32 = input
        .parse()
        .map_err(|_| "Nilai flow harus berupa angka".to_string())?;

    if !value.is_finite() || value < 0.0 {
        return Err("Nilai flow harus finite dan tidak negatif".to_string());
    }

    Ok(value)
}

fn main() {
    match parse_flow("12.5") {
        Ok(value) => println!("Flow: {value} L/min"),
        Err(error) => eprintln!("Error: {error}"),
    }
}
```

- `Option<T>`: nilai mungkin tersedia (`Some`) atau tidak (`None`).
- `Result<T, E>`: operasi berhasil (`Ok`) atau gagal (`Err`).
- `?` meneruskan error ke pemanggil jika tipe error kompatibel.
- Hindari `unwrap()` pada jalur input atau I/O yang dapat gagal.

**Latihan:** parse input kosong, teks, angka negatif, NaN, dan angka valid.

## Bab 13. Traits dan generics dasar

Trait mendefinisikan perilaku bersama. Generics memungkinkan fungsi atau tipe bekerja dengan beberapa tipe tanpa mengulang implementasi.

```rust
trait Validate {
    fn validate(&self) -> bool;
}

struct FlowReading {
    value: f32,
}

impl Validate for FlowReading {
    fn validate(&self) -> bool {
        self.value.is_finite() && self.value >= 0.0
    }
}

fn check<T: Validate>(item: &T) -> bool {
    item.validate()
}

fn main() {
    let reading = FlowReading { value: 12.5 };
    println!("Valid: {}", check(&reading));
}
```

**Latihan:** implementasikan trait Validate untuk model PressureReading dengan batas yang dinyatakan eksplisit.

## Bab 14. File I/O dan JSONL dengan Serde

Tambahkan dependency pada `Cargo.toml`:

```toml
[dependencies]
serde = { version = "1", features = ["derive"] }
serde_json = "1"
```

Contoh serialize satu record menjadi satu baris JSONL:

```rust
use serde::Serialize;
use std::fs::OpenOptions;
use std::io::{BufWriter, Write};

#[derive(Serialize)]
struct Reading {
    device_id: String,
    sensor: String,
    value: f32,
    unit: String,
}

fn main() -> std::io::Result<()> {
    let reading = Reading {
        device_id: "ESP32-01".to_string(),
        sensor: "flow".to_string(),
        value: 12.5,
        unit: "L/min".to_string(),
    };

    let file = OpenOptions::new()
        .create(true)
        .append(true)
        .open("readings.jsonl")?;

    let mut writer = BufWriter::new(file);
    serde_json::to_writer(&mut writer, &reading)?;
    writeln!(writer)?;

    Ok(())
}
```

Untuk proyek nyata, pertimbangkan error gabungan antara I/O dan serialisasi, validasi field, serta strategi rotasi file. Contoh ini fokus pada konsep dasar.

**Latihan:** tulis 10 record, satu objek per baris. Buka file dan pastikan setiap baris dapat diparse sebagai JSON terpisah.

## Bab 15. Testing, formatting, dan Clippy

Tambahkan unit test di file yang sama:

```rust
fn is_valid_flow(value: f32) -> bool {
    value.is_finite() && (0.0..=100.0).contains(&value)
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn accepts_normal_flow() {
        assert!(is_valid_flow(12.5));
    }

    #[test]
    fn rejects_negative_flow() {
        assert!(!is_valid_flow(-1.0));
    }

    #[test]
    fn rejects_nan() {
        assert!(!is_valid_flow(f32::NAN));
    }
}
```

Jalankan:

```bash
cargo fmt
cargo clippy -- -D warnings
cargo test
```

Test batas penting: nilai minimum, maksimum, di luar rentang, NaN, dan dataset kosong. Ganti angka rentang dengan spesifikasi sensor yang digunakan.

## Bab 16. Mini project: Sensor Data Collector

Buat program dengan spesifikasi:
1. Menghasilkan atau menerima data pembacaan sensor.
2. Menyimpan device_id, timestamp, nama sensor, value, dan unit.
3. Memvalidasi field wajib dan rentang data.
4. Menulis record valid ke file JSONL.
5. Menghitung jumlah record diterima dan ditolak.
6. Menulis unit test untuk fungsi validasi.
7. Menyediakan README dengan perintah build dan run.

Struktur yang disarankan:

```text
rust-sensor-collector/
├── Cargo.toml
├── src/
│   ├── main.rs
│   ├── model.rs
│   ├── validation.rs
│   └── storage.rs
├── tests/
│   └── integration_test.rs
└── README.md
```

Jangan langsung menambahkan MQTT, database, dan dashboard. Pastikan versi file lokal yang sederhana benar-benar stabil dahulu.

## Bab 17. Integrasi Rust dengan Python

Pada hari 50–56, gunakan Rust untuk menghasilkan dan memvalidasi data, lalu Python untuk analisis.

Contoh alur:

```text
Sensor / Simulator
       |
       v
Rust Collector
       |
       v
Validation + JSONL
       |
       v
Python + Pandas
       |
       v
Statistics + Visualization
```

Python perlu memeriksa ulang data. Validasi di dua sisi bukan pemborosan: batas kepercayaan antarkomponen perlu diuji.

Setelah pipeline JSONL stabil, pelajari PyO3 jika ada fungsi yang perlu dipanggil langsung dari Python. Mulai dari fungsi kecil dan benchmark sebelum menyimpulkan Rust lebih cepat untuk beban kerja tertentu.

## Checklist kelulusan Rust

- [ ] Dapat membuat proyek Cargo dari terminal.
- [ ] Dapat menjelaskan mutability dan tipe data.
- [ ] Dapat membedakan String dan &str.
- [ ] Dapat menjelaskan move, borrow, dan mutable borrow.
- [ ] Dapat menggunakan struct, enum, Vec, dan HashMap.
- [ ] Dapat menggunakan Option dan Result tanpa unwrap sembarangan.
- [ ] Dapat memisahkan kode ke module.
- [ ] Dapat membaca dan menulis JSONL.
- [ ] Unit test, rustfmt, dan Clippy berjalan.
- [ ] Pipeline Rust–Python menghasilkan analisis yang dapat direproduksi.

## Referensi

- [The Rust Programming Language](https://doc.rust-lang.org/book/)
- [Rust by Example](https://doc.rust-lang.org/rust-by-example/)
- [Rust Standard Library](https://doc.rust-lang.org/std/)
- [Kemal Codes Rust Tutorial](https://github.com/kemalcodes/rust-tutorial)
- [Zero To Mastery Learn Rust](https://zerotomastery.io/courses/learn-rust/)
- [Artikel Rust untuk Data Science dan Machine Learning](https://ajaygurav.medium.com/zero-to-hero-mastering-rust-for-data-science-and-machine-learning-b97446c1833f)
- [Serde](https://serde.rs/)
- [PyO3](https://pyo3.rs/)
