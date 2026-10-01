# Practical 1: Data Parsing, Binary Files, RegEx & Relational Database CRUD

This module contains solutions for all 4 exercises in **Practical 1 (Data Processing Practicals)**.

---

## 📁 Project Structure

```
exercise-01-data-parsing/
├── data_samples/                  # Sample datasets for multi-format parsing
│   ├── sample.txt                 # Pipe-delimited key-value text file
│   ├── sample.csv                 # CSV with missing values & percentage anomalies
│   ├── sample.html                # HTML table with incomplete course records
│   ├── sample.xml                 # XML catalog with negative price/stock anomalies
│   └── sample.json                # JSON records with null attributes
├── task_01_parse_and_validate.py  # Exercise 1: Multi-format parsing & anomaly detection
├── task_02_binary_files.py        # Exercise 2: Binary reading and writing (pickle, struct, raw bytes)
├── task_03_regex_patterns.py      # Exercise 3: RegEx searching, splitting, and replacing
├── task_04_database_crud.py       # Exercise 4: Relational database design & SQL CRUD operations
└── README.md
```

---

## 🚀 Exercises Overview & Running Instructions

### Exercise 1: Data Parsing & Anomaly / Missing Value Detection
- **Script:** [`task_01_parse_and_validate.py`](./task_01_parse_and_validate.py)
- **Formats Handled:** Text, CSV, HTML, XML, and JSON.
- **Validation Features:**
  - Identifies null / empty fields (`pd.isna`, `None`, empty string).
  - Validates data types (numeric IDs, float scores, bounded percentages `0 <= pct <= 100`).
  - Reports line-by-line or record-by-record anomalies.
- **Run:**
  ```bash
  python task_01_parse_and_validate.py
  ```

---

### Exercise 2: Reading and Writing Binary Files
- **Script:** [`task_02_binary_files.py`](./task_02_binary_files.py)
- **Features Handled:**
  - Object serialization and deserialization via `pickle`.
  - Fixed-width binary record packaging with `struct.pack` and `struct.unpack` (`=I10sf?`).
  - Raw bit and byte streams using `bytearray`.
  - Integrity validation (`assert` checks).
- **Run:**
  ```bash
  python task_02_binary_files.py
  ```

---

### Exercise 3: Regular Expressions (Search, Split, Replace)
- **Script:** [`task_03_regex_patterns.py`](./task_03_regex_patterns.py)
- **Features Handled:**
  - **Searching:** Pattern matching emails, dates, timestamps, and log headers with named groups (`re.search`, `re.findall`, `re.finditer`).
  - **Splitting:** Multi-delimiter parsing (commas, semicolons, pipes, tabs) and sentence boundary tokenization (`re.split`).
  - **Replacing:** Data scrubbing and masking (Credit Card numbers, SSNs, and phone number formatting) (`re.sub`, `re.subn`).
- **Run:**
  ```bash
  python task_03_regex_patterns.py
  ```

---

### Exercise 4: Relational Database Design & CRUD Operations
- **Script:** [`task_04_database_crud.py`](./task_04_database_crud.py)
- **Database Engine:** SQLite (`student_portal.db`)
- **Schema Design:**
  - `departments` (PK: `department_id`)
  - `students` (PK: `student_id`, FK: `department_id`)
  - `courses` (PK: `course_id`, FK: `department_id`)
  - `enrollments` (PK: `enrollment_id`, FKs: `student_id`, `course_id`)
- **CRUD Operations:**
  - **Create:** Insert relational records across 4 interconnected tables.
  - **Read:** Query with multi-table `LEFT JOIN`s.
  - **Update:** Modify student GPA and enrollment grades with subqueries.
  - **Delete:** Remove student records and verify `ON DELETE CASCADE` referential action.
- **Run:**
  ```bash
  python task_04_database_crud.py
  ```
