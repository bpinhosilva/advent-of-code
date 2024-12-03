import sys
from enum import Enum

safe_count = 0


class Direction(Enum):
    NONE = 0
    SAME = 1
    ASC = 2
    DES = 3


def get_direction(a, b):
    diff = a - b

    if diff > 0:
        return Direction.DES
    elif diff < 0:
        return Direction.ASC
    else:
        return Direction.SAME


def is_safe_path(a, b, direction):
    if 1 <= int(abs(a - b)) <= 3 and get_direction(a, b) == direction:
        return True

    return False


def solve(arr, direction=Direction.NONE, exceptions=1):
    if exceptions < 0:
        return False
    if len(arr) <= 1:
        return True
    if (direction is Direction.NONE):
        direction = get_direction(arr[0], arr[1])

    for i in range(len(arr) - 1):
        if not is_safe_path(arr[i], arr[i + 1], direction):
            for j in range(len(arr)):
                sub_array_ith = arr.copy()
                sub_array_ith.pop(j)

                sub_problem = solve(sub_array_ith, Direction.NONE, exceptions - 1)

                if sub_problem is True:
                    return True
            return False

    return True


# Read input until EOF
for line in sys.stdin:
    line = line.strip()  # Strip leading/trailing spaces

    if line:
        # Process each line (strip newline character and split into numbers)
        numbers = list(map(int, line.split()))

        if solve(numbers):
            safe_count += 1

print(safe_count)
