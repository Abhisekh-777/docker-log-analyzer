import sys
from collections import Counter

if len(sys.argv) < 2:
    print("Usage: docker run log-analyzer <logfile>")
    sys.exit(1)

logfile = sys.argv[1]
status_codes = Counter()

with open(logfile, "r") as f:
    for line in f:
        parts = line.split()
        for p in parts:
            if p.isdigit() and len(p) == 3:
                status_codes[p] += 1
                break

print("HTTP Status Code Summary")
print("------------------------")

if not status_codes:
    print("No status codes found")
else:
    for code, count in sorted(status_codes.items()):
        print(f"{code}: {count}")
