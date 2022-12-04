import sys

max_calories = []
local_sum = 0

for line in sys.stdin:
  if line.replace("\n", "") == '':
    max_calories.append(local_sum)
    local_sum = 0

  else:
    local_sum = local_sum + int(line)

max_calories.append(local_sum)

max_calories.sort(reverse=True)

print(f'sum: {sum(max_calories[:3])}')
