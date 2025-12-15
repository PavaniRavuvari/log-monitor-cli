# Log Monitoring CLI Tool

## Description
A Python-based command-line tool to parse, analyze, and monitor server log files.  
It extracts important information, detects errors, identifies top IPs, and generates insightful reports in both console and file formats.

---

## Features
- Parse server log files to extract IP, timestamp, HTTP method, URL, and status code  
- Analyze logs to:
  - Identify top N IPs by request count  
  - Summarize HTTP status codes  
  - Detect 4xx and 5xx errors  
- Generate reports:
  - Displayed in console  
  - Saved to a file (`log_report.txt`)  
- Modular and clean Python code structure

---

## Folder Structure
log-monitor-cli/
├── monitor/
│ ├── init.py
│ ├── parser.py
│ ├── analyzer.py
│ ├── reporter.py
│ └── alerts.py
├── sample_logs/
│ └── access.log
├── monitor.py
├── requirements.txt
└── README.md
