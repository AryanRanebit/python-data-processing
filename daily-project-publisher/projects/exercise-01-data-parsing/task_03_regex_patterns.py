import re

# -------------------------------------------------------------
# Exercise 3: Searching, Splitting, and Replacing using RegEx
# -------------------------------------------------------------

def demo_regex_searching():
    print("\n" + "=" * 60)
    print("1. RegEx Searching (`re.search`, `re.findall`, `re.finditer`)")
    print("=" * 60)

    sample_log = """
    2026-03-15 08:30:12 [INFO] user_id=101 email=john.doe@company.org phone=+1-555-0199 login_success
    2026-03-15 08:31:05 [WARN] user_id=102 email=invalid-email phone=9876543210 login_failed
    2026-03-15 08:32:44 [ERROR] user_id=103 email=sara_connor@tech.co.uk phone=+91-98765-43210 connection_timeout
    2026-03-15 08:35:19 [INFO] user_id=104 email=alice.smith99@domain.com phone=555-123-4567 login_success
    """

    print("Target Text:")
    print(sample_log.strip())

    # Pattern A: Extract valid email addresses
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'
    found_emails = re.findall(email_pattern, sample_log)
    print("\n[re.findall] Extracted Valid Emails:")
    for email in found_emails:
        print(f"  - {email}")

    # Pattern B: Extract timestamps and log levels with capturing groups
    log_entry_pattern = r'(?P<timestamp>\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2})\s\[(?P<level>[A-Z]+)\]\suser_id=(?P<uid>\d+)'
    print("\n[re.finditer] Extracted Log Header Groups:")
    for match in re.finditer(log_entry_pattern, sample_log):
        print(f"  Match -> Time: {match.group('timestamp')} | Level: {match.group('level'):<5} | User ID: {match.group('uid')}")

    # Pattern C: Searching for specific first error
    error_match = re.search(r'\[ERROR\].*?email=(?P<email>\S+)', sample_log)
    if error_match:
        print(f"\n[re.search] First Error Found for email: {error_match.group('email')}")


def demo_regex_splitting():
    print("\n" + "=" * 60)
    print("2. RegEx Splitting (`re.split`)")
    print("=" * 60)

    # Multi-delimiter text (semicolons, commas, tabs, pipelines, variable whitespaces)
    raw_csv_messy = "Apple, Banana; Orange | Pineapple \t Mango ,,, Grape ;;; Watermelon"
    print(f"Original String:\n  '{raw_csv_messy}'")

    # Split on any combination of commas, semicolons, pipes, or tabs with surrounding spaces
    split_pattern = r'\s*[,;|]\s*|\t+'
    tokens = [t.strip() for t in re.split(split_pattern, raw_csv_messy) if t.strip()]

    print("\n[re.split] Clean Tokens Extracted:")
    print(f"  {tokens}")

    # Sentence boundary splitting (handling abbreviations carefully)
    paragraph = "Dr. Smith arrived at 8:00 A.M. He began the surgery! Was the team prepared? Yes, completely."
    sentence_pattern = r'(?<=[.!?])\s+(?=[A-Z])'
    sentences = re.split(sentence_pattern, paragraph)
    print("\n[re.split] Sentences:")
    for idx, s in enumerate(sentences, 1):
        print(f"  {idx}. {s}")


def demo_regex_replacing():
    print("\n" + "=" * 60)
    print("3. RegEx Replacing and Masking (`re.sub`, `re.subn`)")
    print("=" * 60)

    sensitive_text = """
    Customer Records:
    1. John Doe - Phone: 987-654-3210, Card: 4111-2222-3333-4444, SSN: 123-45-6789
    2. Mary Jane - Phone: (555) 019-2834, Card: 5500-0000-1111-2222, SSN: 987-65-4321
    """
    print("Original Sensitive Document:")
    print(sensitive_text.strip())

    # Replace 1: Mask Credit Card Numbers (Keep only last 4 digits)
    card_pattern = r'\b(?:\d{4}-){3}(\d{4})\b'
    masked_cards = re.sub(card_pattern, r'****-****-****-\1', sensitive_text)

    # Replace 2: Mask SSN (format: \d{3}-\d{2}-\d{4})
    ssn_pattern = r'\b\d{3}-\d{2}-\d{4}\b'
    masked_all = re.sub(ssn_pattern, 'XXX-XX-XXXX', masked_cards)

    # Replace 3: Standardize Phone numbers using callable replacer function in re.sub
    phone_pattern = r'\(?(\d{3})\)?[-.\s]?(\d{3})[-.\s]?(\d{4})'
    def format_phone(match):
        return f"+1 ({match.group(1)}) {match.group(2)}-{match.group(3)}"

    anonymized_text, count = re.subn(phone_pattern, format_phone, masked_all)

    print(f"\n[re.sub & re.subn] Scrubbed & Anonymized Text (Replacements made: {count}):")
    print(anonymized_text.strip())


def main():
    demo_regex_searching()
    demo_regex_splitting()
    demo_regex_replacing()
    print("\n" + "=" * 60)
    print("Exercise 3 Complete: RegEx Searching, Splitting, and Replacing demonstrated.")
    print("=" * 60)


if __name__ == "__main__":
    main()
