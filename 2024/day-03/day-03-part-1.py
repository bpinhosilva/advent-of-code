import sys
import re

sum = 0

# Read input until EOF
for line in sys.stdin:
    line = line.strip()  # Strip leading/trailing spaces

    if line:
        # group values in list of tuples
        matches = re.findall("mul\((\d{1,3}),(\d{1,3})\)", line)

        for (x, y) in matches:
            sum += int(x) * int(y)

print(sum)
