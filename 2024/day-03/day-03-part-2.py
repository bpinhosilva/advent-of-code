import sys
import re

sum = 0
enabled = True

# Read input until EOF
for line in sys.stdin:
    line = line.strip()  # Strip leading/trailing spaces

    if line:
        for r in re.finditer("mul\((\d{1,3}),(\d{1,3})\)|do\(\)|don\'t\(\)", line):
            option, a, b = r.group(0, 1, 2)

            if option == "don't()":
                enabled = False
            elif option == "do()":
                enabled = True
            elif enabled:
                sum += int(a) * int(b)

print(sum)
