import csv
from collections import Counter
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
INPUT_FILE = PROJECT_ROOT / "data" / "sample_login_attempts.csv"
FAILED_LOGIN_THRESHOLD = 5


def read_login_attempts(file_path):
    """Read login attempts from a CSV file."""
    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        return list(reader)


def get_failed_logins(login_attempts):
    """Return only failed login attempts."""
    return [
        attempt
        for attempt in login_attempts
        if attempt["login_status"].lower() == "failed"
    ]


def count_failed_logins_by_username(failed_logins):
    """Count failed login attempts by username."""
    usernames = [attempt["username"] for attempt in failed_logins]
    return Counter(usernames)


def count_failed_logins_by_ip(failed_logins):
    """Count failed login attempts by IP address."""
    ip_addresses = [attempt["ip_address"] for attempt in failed_logins]
    return Counter(ip_addresses)


def print_suspicious_activity(title, counter):
    """Print anything over the failed login threshold."""
    print(f"\n{title}")
    print("-" * len(title))

    suspicious_items = {
        item: count
        for item, count in counter.items()
        if count >= FAILED_LOGIN_THRESHOLD
    }

    if not suspicious_items:
        print("No suspicious activity found.")
        return

    for item, count in suspicious_items.items():
        print(f"{item}: {count} failed login attempts")


def main():
    login_attempts = read_login_attempts(INPUT_FILE)
    failed_logins = get_failed_logins(login_attempts)

    failed_by_username = count_failed_logins_by_username(failed_logins)
    failed_by_ip = count_failed_logins_by_ip(failed_logins)

    print("Login Failure Analysis Report")
    print("=============================")
    print(f"Total login attempts: {len(login_attempts)}")
    print(f"Total failed logins: {len(failed_logins)}")
    print(f"Alert threshold: {FAILED_LOGIN_THRESHOLD} failed attempts")

    print_suspicious_activity(
        "Suspicious usernames",
        failed_by_username
    )

    print_suspicious_activity(
        "Suspicious IP addresses",
        failed_by_ip
    )


if __name__ == "__main__":
    main()
