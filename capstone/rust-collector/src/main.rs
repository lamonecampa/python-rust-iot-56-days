use serde::Serialize;
use std::{fs::{self, File}, io::{BufWriter, Write}, path::Path};

#[derive(Serialize)]
struct Reading {
    timestamp: String,
    device: String,
    sensor: String,
    value: f64,
    unit: String,
}

fn is_valid(reading: &Reading) -> bool {
    reading.value.is_finite() && (0.0..=100.0).contains(&reading.value)
}

fn main() -> Result<(), Box<dyn std::error::Error>> {
    let output = Path::new("../data/readings.jsonl");
    if let Some(parent) = output.parent() {
        fs::create_dir_all(parent)?;
    }

    let file = File::create(output)?;
    let mut writer = BufWriter::new(file);

    for index in 0..120 {
        let value = if index == 70 {
            150.0 // deliberate invalid sample for validation exercise
        } else {
            10.0 + ((index * 7) % 19) as f64 * 0.7
        };

        let reading = Reading {
            timestamp: format!("2026-01-01T00:{:02}:00Z", index % 60),
            device: "ESP32-SIM-01".to_string(),
            sensor: "flow".to_string(),
            value,
            unit: "L/min".to_string(),
        };

        if is_valid(&reading) {
            serde_json::to_writer(&mut writer, &reading)?;
            writer.write_all(b"\n")?;
        } else {
            eprintln!("Rejected sample {index}: value {value} outside range");
        }
    }

    writer.flush()?;
    println!("Wrote JSONL to {}", output.display());
    Ok(())
}
