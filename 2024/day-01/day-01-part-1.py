import sys

a = []
b = []

# Read input until EOF
for line in sys.stdin:
    line = line.strip()  # Strip leading/trailing spaces

    if line:
        # Process each line (strip newline character and split into numbers)
        numbers = list(map(int, line.split()))    
        a.append(numbers[0])
        b.append(numbers[1])
    

a.sort()
b.sort()

sum = 0

for i in range(len(a)):
    sum += int(abs(a[i] - b[i]))

print(sum)
