#!/usr/bin/env python3

import re
import csv

log_entries = []

pattern = r"(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) (\w+) (.*)"
with open ("data/sample_log.txt","r") as file:
    for line in file:
        match = re.search(pattern, line)
        if match:
            entry = {
                "timestamp": match.group(1),
                "level": match.group(2),
                "message": match.group(3)
            }
            log_entries.append(entry)
            
            print("Parsed log entries:")
            for entry in log_entries:
                print(entry)
                
with open("results/log_summary.csv","w", newline="") as csvfile:
    fieldnames = ["timestamp", "level", "message"]
    
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerows(log_entries)
print("Log summary saved to results/log_summary.csv")

error_count = 0
for entry in log_entries:
    if entry["level"] == "ERROR":
        error_count += 1
print(f"Total errors found: {error_count}") 