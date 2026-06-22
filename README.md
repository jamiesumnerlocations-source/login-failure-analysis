# login-failure-analysis
Read login attempts from a CSV, count failed logins by username and IP address, then flag anything over a threshold.

# Login Failure Analysis

## Project Summary

A small Python project that analyses mock login attempt data and flags repeated failed logins by username and IP address.

## Problem It Solves

Repeated failed login attempts can indicate brute-force activity, password guessing, compromised accounts, or poor access-control hygiene. This project demonstrates a basic way to review login data and highlight patterns that may need investigation.

## Example Output

```text
Login Failure Analysis Report
=============================
Total login attempts: 9
Total failed logins: 7
Alert threshold: 5 failed attempts

Suspicious usernames
--------------------
admin: 5 failed login attempts

Suspicious IP addresses
-----------------------
185.22.91.10: 5 failed login attempts

## Skills Demonstrated

* Python scripting
* CSV file handling
* Data filtering
* Counting and grouping records
* Basic security log analysis
* Identifying suspicious login behaviour
* Producing readable command-line reports

## How to Run

1. Clone the repository.
2. Make sure Python 3 is installed.
3. From the project root, run:

```bash
python src/analyse_logins.py
```

## Example Input

The project uses a mock CSV file stored in:

```text
data/sample_login_attempts.csv
```

Example columns:

```text
timestamp, username, ip_address, login_status, failure_reason
```

## Example Output

```text
Login Failure Analysis Report
=============================
Total login attempts: 9
Total failed logins: 7
Alert threshold: 5 failed attempts

Suspicious usernames
--------------------
admin: 5 failed login attempts

Suspicious IP addresses
-----------------------
185.22.91.10: 5 failed login attempts
```

## What I Learned

This project helped me practise reading structured log data, filtering useful records, grouping repeated events, and producing a basic security-focused report. It also helped reinforce how repeated failed logins can be used as an early indicator of suspicious activity.

## Future Improvements

* Add command-line arguments for file path and alert threshold.
* Export the report to a text or CSV file.
* Add timestamps and detect repeated attempts within a short time window.
* Add risk scoring.
* Add unit tests.
* Rebuild a second version using pandas.
