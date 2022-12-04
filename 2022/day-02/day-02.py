import sys

shape = {
  # rock
  "A": 1,
  "X": 1,

  # paper
  "B": 2,
  "Y": 2,

  # scissors
  "C": 3,
  "Z": 3
}

round = {
  "w": 6,
  "l": 0,
  "d": 3
}


# Rock defeats Scissors, Scissors defeats Paper, and Paper defeats Rock.
def compute_score(theirs, yours):
  if theirs == yours \
      or (theirs == "A" and yours == "X") \
      or (theirs == "B" and yours == "Y") \
      or (theirs == "C" and yours == "Z"):
    return round["d"] + shape[yours]
  elif theirs == 'A' and yours == 'Y':
    return round["w"] + shape[yours]
  elif theirs == 'A' and yours == 'Z':
    return round["l"] + shape[yours]
  elif theirs == 'B' and yours == 'X':
    return round["l"] + shape[yours]
  elif theirs == 'B' and yours == 'Z':
    return round["w"] + shape[yours]
  elif theirs == 'C' and yours == 'X':
    return round["w"] + shape[yours]
  elif theirs == 'C' and yours == 'Y':
    return round["l"] + shape[yours]
  else:
    return 0


your_score = 0

for line in sys.stdin:
  if line.replace("\n", "") == '':
    break

  else:
    your_score = your_score + compute_score(line[0], line[2])

print(f' your score: {your_score}')
