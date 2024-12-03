import sys
import re

sum = 0

# Read input until EOF
for line in sys.stdin:
    line = line.strip()  # Strip leading/trailing spaces

    if line:
        matches = re.findall("mul\(\d{1,3},\d{1,3}\)|do\(\)|don\'t\(\)", line)

print(sum)
