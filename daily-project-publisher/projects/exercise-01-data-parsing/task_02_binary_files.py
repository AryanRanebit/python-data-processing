import os
import struct
import pickle

# -------------------------------------------------------------
# Exercise 2: Reading and Writing Binary Files
# -------------------------------------------------------------

def demo_pickle_binary_io(filepath="sample_data.bin"):
    print("\n" + "=" * 60)
    print("1. Binary Serialization using 'pickle' (Structured Objects)")
    print("=" * 60)

    # Complex Python data structure (nested dictionary, list, tuples)
    dataset = {
        "dataset_name": "Sensor Telemetry Batch 01",
        "timestamp": "2026-10-01T10:00:00Z",
        "sensors": [
            {"sensor_id": "SN-001", "temperature_c": 24.5, "status": "ACTIVE"},
            {"sensor_id": "SN-002", "temperature_c": 31.2, "status": "ACTIVE"},
            {"sensor_id": "SN-003", "temperature_c": 78.9, "status": "OVERHEAT_WARNING"}
        ],
        "checksum": 0xABCD1234
    }

    # Writing binary data
    print(f"Writing structured Python object to binary file '{filepath}'...")
    with open(filepath, "wb") as bf:
        pickle.dump(dataset, bf)
    print(f"File written successfully. Size: {os.path.getsize(filepath)} bytes.")

    # Reading binary data
    print(f"Reading structured object back from '{filepath}'...")
    with open(filepath, "rb") as bf:
        loaded_data = pickle.load(bf)

    print("Loaded Data Object:")
    print(f"  Dataset Name : {loaded_data['dataset_name']}")
    print(f"  Timestamp    : {loaded_data['timestamp']}")
    print(f"  Sensors Count: {len(loaded_data['sensors'])}")
    for s in loaded_data['sensors']:
        print(f"    - {s['sensor_id']} | Temp: {s['temperature_c']} C | Status: {s['status']}")

    assert loaded_data == dataset, "Verification failed: loaded object does not match original!"
    print("Integrity check PASSED: Read data matches written object exactly.")


def demo_raw_struct_binary_io(filepath="telemetry_packed.bin"):
    print("\n" + "=" * 60)
    print("2. Low-Level Binary Pack/Unpack using 'struct' & Byte Streams")
    print("=" * 60)

    # Format string:
    #   I : unsigned int (4 bytes, Record ID)
    #   10s: char[10] (10 bytes, Sensor Code)
    #   f : float (4 bytes, Temperature)
    #   ? : bool (1 byte, Is Flagged)
    # Total record size = 19 bytes (or padded)
    record_format = "=I10sf?"
    record_size = struct.calcsize(record_format)
    print(f"Compiled binary struct format: '{record_format}', Record size: {record_size} bytes.")

    records = [
        (101, b"SENSOR_A  ", 26.75, False),
        (102, b"SENSOR_B  ", 85.12, True),
        (103, b"SENSOR_C  ", 19.30, False),
    ]

    # Write raw binary records
    print(f"Packing and writing {len(records)} binary records to '{filepath}'...")
    with open(filepath, "wb") as bf:
        # Write 2-byte header: total count
        bf.write(struct.pack("=H", len(records)))
        for rec in records:
            packed_bytes = struct.pack(record_format, *rec)
            bf.write(packed_bytes)
    
    file_bytes = os.path.getsize(filepath)
    print(f"Binary file written. Total size on disk: {file_bytes} bytes.")

    # Read and unpack raw bytes
    print(f"Reading raw binary bytes from '{filepath}'...")
    unpacked_records = []
    with open(filepath, "rb") as bf:
        count_bytes = bf.read(2)
        total_count = struct.unpack("=H", count_bytes)[0]
        print(f"Header indicates {total_count} records stored.")

        for _ in range(total_count):
            chunk = bf.read(record_size)
            unpacked = struct.unpack(record_format, chunk)
            record_id, sensor_bytes, temp, is_flagged = unpacked
            sensor_name = sensor_bytes.decode('ascii').strip()
            unpacked_records.append({
                "record_id": record_id,
                "sensor": sensor_name,
                "temperature": round(temp, 2),
                "flagged": is_flagged
            })

    print("Unpacked Records:")
    for ur in unpacked_records:
        print(f"  ID: {ur['record_id']} | Sensor: {ur['sensor']} | Temp: {ur['temperature']} | Flagged: {ur['flagged']}")

    print("Low-Level Binary Pack/Unpack test PASSED.")


def demo_raw_bytearray_io(filepath="raw_stream.bin"):
    print("\n" + "=" * 60)
    print("3. Direct Raw Byte Streams and Bit Manipulation")
    print("=" * 60)

    # Creating a mutable byte array (e.g. 0 to 255 values)
    raw_data = bytearray([0xDE, 0xAD, 0xBE, 0xEF, 0xCA, 0xFE, 0xBA, 0xBE])
    print(f"Original Byte Stream: {[hex(b) for b in raw_data]}")

    with open(filepath, "wb") as bf:
        bf.write(raw_data)

    with open(filepath, "rb") as bf:
        read_stream = bf.read()

    print(f"Read Byte Stream    : {[hex(b) for b in read_stream]}")
    assert raw_data == read_stream, "Byte stream mismatch!"
    print("Raw Byte Stream verification PASSED.")


def main():
    demo_pickle_binary_io()
    demo_raw_struct_binary_io()
    demo_raw_bytearray_io()
    print("\n" + "=" * 60)
    print("Exercise 2 Complete: Reading and Writing Binary Files successful.")
    print("=" * 60)


if __name__ == "__main__":
    main()
