import os
import json
import csv
import xml.etree.ElementTree as ET
from html.parser import HTMLParser
import pandas as pd

# -------------------------------------------------------------
# Setup Sample Data Files
# -------------------------------------------------------------
def setup_samples(data_dir="data_samples"):
    os.makedirs(data_dir, exist_ok=True)

    # 1. Text File (Key-Value style and anomalies)
    text_content = """# Student Records Batch A
ID: 101 | Name: Alice Smith | Age: 20 | Score: 88.5
ID: 102 | Name: Bob Jones | Age: -5 | Score: 92.0
ID: 103 | Name:  | Age: 22 | Score: N/A
ID: 104 | Name: Charlie Brown | Age: 19 | Score: 76.0
ID: INVALID_ID | Name: Diana | Age: 21 | Score: 85.0
"""
    with open(os.path.join(data_dir, "sample.txt"), "w", encoding="utf-8") as f:
        f.write(text_content)

    # 2. CSV File
    csv_content = """student_id,name,age,grade,attendance_pct
101,Alice Smith,20,A,95.5
102,Bob Jones,,B,82.0
103,Charlie Brown,22,,74.5
104,Diana Prince,19,A,150.0
105,Evan Wright,21,C,
"""
    with open(os.path.join(data_dir, "sample.csv"), "w", encoding="utf-8") as f:
        f.write(csv_content)

    # 3. HTML File
    html_content = """<!DOCTYPE html>
<html>
<head><title>Course Catalog</title></head>
<body>
  <h2>Available Courses</h2>
  <table id="course-table">
    <thead>
      <tr><th>Course Code</th><th>Title</th><th>Credits</th><th>Instructor</th></tr>
    </thead>
    <tbody>
      <tr><td>CS101</td><td>Intro to Programming</td><td>4</td><td>Dr. Alan Turing</td></tr>
      <tr><td>CS201</td><td>Data Structures</td><td></td><td>Prof. Knuth</td></tr>
      <tr><td>CS301</td><td>Database Management</td><td>-1</td><td>Dr. Codd</td></tr>
      <tr><td>CS401</td><td>Machine Learning</td><td>3</td><td></td></tr>
    </tbody>
  </table>
</body>
</html>
"""
    with open(os.path.join(data_dir, "sample.html"), "w", encoding="utf-8") as f:
        f.write(html_content)

    # 4. XML File
    xml_content = """<?xml version="1.0" encoding="UTF-8"?>
<inventory>
  <item id="SKU001">
    <name>Wireless Mouse</name>
    <price>25.99</price>
    <stock>120</stock>
  </item>
  <item id="SKU002">
    <name>Mechanical Keyboard</name>
    <price>-45.00</price>
    <stock>45</stock>
  </item>
  <item id="SKU003">
    <name></name>
    <price>199.99</price>
    <stock>0</stock>
  </item>
  <item id="SKU004">
    <name>Gaming Monitor</name>
    <price>350.00</price>
    <stock></stock>
  </item>
</inventory>
"""
    with open(os.path.join(data_dir, "sample.xml"), "w", encoding="utf-8") as f:
        f.write(xml_content)

    # 5. JSON File
    json_content = [
        {"user_id": 1, "username": "alice99", "email": "alice@example.com", "active": True, "balance": 450.75},
        {"user_id": 2, "username": "bob_ross", "email": "bob-invalid-email", "active": False, "balance": -20.00},
        {"user_id": 3, "username": None, "email": "charlie@example.com", "active": True, "balance": 1500.00},
        {"user_id": 4, "username": "diana_p", "email": None, "active": True, "balance": None}
    ]
    with open(os.path.join(data_dir, "sample.json"), "w", encoding="utf-8") as f:
        json.dump(json_content, f, indent=2)

    print(f"Generated sample datasets in '{data_dir}/'")


# -------------------------------------------------------------
# HTML Parser Helper
# -------------------------------------------------------------
class SimpleHTMLTableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.in_tbody = False
        self.in_tr = False
        self.in_td = False
        self.current_row = []
        self.rows = []

    def handle_starttag(self, tag, attrs):
        if tag == "tbody":
            self.in_tbody = True
        elif self.in_tbody and tag == "tr":
            self.in_tr = True
            self.current_row = []
        elif self.in_tr and tag == "td":
            self.in_td = True

    def handle_data(self, data):
        if self.in_td:
            self.current_row.append(data.strip())

    def handle_endtag(self, tag):
        if tag == "td":
            self.in_td = False
        elif tag == "tr" and self.in_tr:
            self.rows.append(self.current_row)
            self.in_tr = False
        elif tag == "tbody":
            self.in_tbody = False


# -------------------------------------------------------------
# Parsers & Anomaly Checkers
# -------------------------------------------------------------
def parse_text_file(filepath):
    print("\n" + "=" * 60)
    print(f"1. Parsing Text File: {filepath}")
    print("=" * 60)
    records = []
    anomalies = []

    with open(filepath, "r", encoding="utf-8") as f:
        for line_no, line in enumerate(f, start=1):
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = [p.strip() for p in line.split("|")]
            entry = {}
            for part in parts:
                if ":" in part:
                    k, v = part.split(":", 1)
                    entry[k.strip()] = v.strip()
            records.append(entry)

            # Anomaly Checks
            # Rule 1: ID must be numeric
            # Rule 2: Name must not be empty
            # Rule 3: Age must be positive (1-100)
            # Rule 4: Score must be valid float
            entry_id = entry.get("ID", "")
            name = entry.get("Name", "")
            age = entry.get("Age", "")
            score = entry.get("Score", "")

            if not entry_id.isdigit():
                anomalies.append(f"Line {line_no}: Invalid non-numeric ID '{entry_id}'")
            if not name:
                anomalies.append(f"Line {line_no}: Missing Name for ID '{entry_id}'")
            try:
                age_val = int(age)
                if age_val <= 0 or age_val > 100:
                    anomalies.append(f"Line {line_no}: Impossible Age anomaly ({age_val})")
            except ValueError:
                anomalies.append(f"Line {line_no}: Non-integer Age '{age}'")

            try:
                float(score)
            except ValueError:
                anomalies.append(f"Line {line_no}: Missing or invalid numeric Score '{score}'")

    print(f"Extracted {len(records)} records.")
    print(f"Detected {len(anomalies)} anomalies:")
    for a in anomalies:
        print(f"  - {a}")
    return records


def parse_csv_file(filepath):
    print("\n" + "=" * 60)
    print(f"2. Parsing CSV Document: {filepath}")
    print("=" * 60)
    df = pd.read_csv(filepath)
    print("Extracted DataFrame:")
    print(df)

    print("\nMissing Values Audit:")
    null_counts = df.isnull().sum()
    print(null_counts[null_counts > 0])

    print("\nBusiness Rule Anomaly Audit:")
    anomalies = []
    for idx, row in df.iterrows():
        # Attendance percentage must be 0 <= pct <= 100
        if pd.notnull(row['attendance_pct']) and (row['attendance_pct'] < 0 or row['attendance_pct'] > 100):
            anomalies.append(f"Row {idx} (ID {row['student_id']}): attendance_pct {row['attendance_pct']} out of bounds (0-100%)")
        if pd.isnull(row['grade']):
            anomalies.append(f"Row {idx} (ID {row['student_id']}): Grade is missing")
        if pd.isnull(row['age']):
            anomalies.append(f"Row {idx} (ID {row['student_id']}): Age is missing")
    
    for a in anomalies:
        print(f"  - {a}")
    return df


def parse_html_document(filepath):
    print("\n" + "=" * 60)
    print(f"3. Parsing HTML Document: {filepath}")
    print("=" * 60)
    with open(filepath, "r", encoding="utf-8") as f:
        html_text = f.read()

    parser = SimpleHTMLTableParser()
    parser.feed(html_text)
    
    headers = ["Course Code", "Title", "Credits", "Instructor"]
    # Handle rows where cell count might vary
    rows = []
    anomalies = []
    for r_idx, r in enumerate(parser.rows):
        # Pad row to 4 elements if needed
        while len(r) < 4:
            r.append("")
        row_dict = dict(zip(headers, r))
        rows.append(row_dict)

        # Anomaly checks
        credits_str = row_dict["Credits"]
        instructor = row_dict["Instructor"]
        if not credits_str:
            anomalies.append(f"Row {r_idx + 1} ({row_dict['Course Code']}): Missing Credits")
        else:
            try:
                c = int(credits_str)
                if c <= 0:
                    anomalies.append(f"Row {r_idx + 1} ({row_dict['Course Code']}): Invalid negative or zero credits ({c})")
            except ValueError:
                anomalies.append(f"Row {r_idx + 1} ({row_dict['Course Code']}): Non-integer credits '{credits_str}'")

        if not instructor:
            anomalies.append(f"Row {r_idx + 1} ({row_dict['Course Code']}): Missing Instructor")

    print(f"Extracted {len(rows)} course records:")
    for r in rows:
        print(f"  {r}")
    print(f"\nDetected {len(anomalies)} anomalies:")
    for a in anomalies:
        print(f"  - {a}")
    return rows


def parse_xml_document(filepath):
    print("\n" + "=" * 60)
    print(f"4. Parsing XML Document: {filepath}")
    print("=" * 60)
    tree = ET.parse(filepath)
    root = tree.getroot()

    items = []
    anomalies = []
    for elem in root.findall("item"):
        item_id = elem.get("id")
        name = elem.findtext("name", default="").strip()
        price_str = elem.findtext("price", default="").strip()
        stock_str = elem.findtext("stock", default="").strip()

        item_data = {
            "id": item_id,
            "name": name,
            "price": price_str,
            "stock": stock_str
        }
        items.append(item_data)

        # Anomaly checks
        if not name:
            anomalies.append(f"Item {item_id}: Name is missing/empty")
        try:
            p = float(price_str)
            if p < 0:
                anomalies.append(f"Item {item_id}: Negative price anomaly ({p})")
        except ValueError:
            anomalies.append(f"Item {item_id}: Invalid/missing price '{price_str}'")

        try:
            s = int(stock_str)
            if s < 0:
                anomalies.append(f"Item {item_id}: Negative stock quantity ({s})")
        except ValueError:
            anomalies.append(f"Item {item_id}: Invalid/missing stock count '{stock_str}'")

    print(f"Extracted {len(items)} items from XML:")
    for it in items:
        print(f"  {it}")
    print(f"\nDetected {len(anomalies)} anomalies:")
    for a in anomalies:
        print(f"  - {a}")
    return items


def parse_json_document(filepath):
    print("\n" + "=" * 60)
    print(f"5. Parsing JSON Document: {filepath}")
    print("=" * 60)
    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    anomalies = []
    for idx, user in enumerate(data):
        user_id = user.get("user_id")
        username = user.get("username")
        email = user.get("email")
        balance = user.get("balance")

        if username is None or username == "":
            anomalies.append(f"Record {idx} (ID {user_id}): Missing username")
        if email is None or "@" not in email:
            anomalies.append(f"Record {idx} (ID {user_id}): Invalid or missing email ('{email}')")
        if balance is None:
            anomalies.append(f"Record {idx} (ID {user_id}): Missing balance field")
        elif balance < 0:
            anomalies.append(f"Record {idx} (ID {user_id}): Negative account balance ({balance})")

    print(f"Parsed {len(data)} JSON records.")
    print(f"Detected {len(anomalies)} anomalies:")
    for a in anomalies:
        print(f"  - {a}")
    return data


def main():
    data_dir = "data_samples"
    setup_samples(data_dir)

    parse_text_file(os.path.join(data_dir, "sample.txt"))
    parse_csv_file(os.path.join(data_dir, "sample.csv"))
    parse_html_document(os.path.join(data_dir, "sample.html"))
    parse_xml_document(os.path.join(data_dir, "sample.xml"))
    parse_json_document(os.path.join(data_dir, "sample.json"))
    print("\n" + "=" * 60)
    print("Exercise 1 Complete: All 5 file formats parsed and validated.")
    print("=" * 60)


if __name__ == "__main__":
    main()
