# Python Log File Analyzer

A Python tool that parses server log files using regular expressions
and extracts structured information such as timestamps, log levels,
and messages.

## Features

- Regex-based log parsing
- File reading and iteration
- Data extraction using dictionaries
- Export parsed logs to CSV
- Simple log statistics

## Technologies Used

- Python
- Regular Expressions (re module)
- File I/O
- CSV module

## Project Structure

python-log-file-analyzer/
│
├── data/
│ └── sample_log.txt
│
├── src/
│ └── parser.py
│
├── results/
│ └── log_summary.csv
│
├── README.md
└── requirements.txt

## Example Output

timestamp,level,message
2026-03-12 14:23:10,INFO,User login
2026-03-12 14:24:11,ERROR,Database timeout

## How to Run

Run "python src/parser.py" in the root of the folder
