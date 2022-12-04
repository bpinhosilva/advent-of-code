import sys

max_calories = 0
current_elf_index = 1
elf_index = 1
local_sum = 0

for line in sys.stdin:
  if line.replace("\n", "") == '':

    if local_sum > max_calories:
      max_calories = local_sum
      elf_index = current_elf_index

    current_elf_index = current_elf_index + 1
    local_sum = 0

  else:
    local_sum = local_sum + int(line)

if local_sum > max_calories:
  max_calories = local_sum
  elf_index = current_elf_index

print(f'index elf: {elf_index}, total: {max_calories}')
