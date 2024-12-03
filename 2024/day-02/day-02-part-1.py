import sys

safe_count = 0
direction = 0
max_distance = 3
min_distance = 1

# Read input until EOF
for line in sys.stdin:
    line = line.strip()  # Strip leading/trailing spaces

    if line:
        # Process each line (strip newline character and split into numbers)
        numbers = list(map(int, line.split()))
        difference = numbers[0] - numbers[1]

        if abs(difference) > max_distance or abs(difference) < min_distance:
            continue

        if difference > 0:
            direction = -1
        else:
            direction = 1

        valid_line = True

        for i in range(1, len(numbers) - 1):
            difference = numbers[i] - numbers[i + 1]

            if abs(difference) > max_distance or abs(difference) < min_distance:
                valid_line = False
                break

            if min_distance <= abs(difference) <= max_distance:
                new_difference = numbers[i] - numbers[i + 1]
                if new_difference > 0:
                    new_direction = -1
                else:
                    new_direction = 1

                if new_direction != direction:
                    valid_line = False
                    break

        if valid_line:
            safe_count += 1

print(safe_count)
