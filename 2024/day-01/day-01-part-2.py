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

memo = {}
total = 0
    
for i in a:
    if i not in memo:
        memo[i] = 0
        
        for j in b:
            if i == j:
                memo[i] = memo[i] + 1
            
        
    total = total + i * memo[i]            
    

print(total)
