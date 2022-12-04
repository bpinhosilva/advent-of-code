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
  if yours == "X":
    # should lose
    if theirs == "A":
      return shape["Z"]
    elif theirs == "B":
      return shape["X"]
    else:
      return shape["Y"]
  elif yours == "Y":
    # should be a draw
    return 3 + shape[theirs]
  elif yours == "Z":
    # you need to win
    if theirs == "A":
      return 6 + shape["Y"]
    elif theirs == "B":
      return 6 + shape["Z"]
    else:
      return 6 + shape["X"]
  else:
    return 0


your_score = 0

for line in sys.stdin:
  if line.replace("\n", "") == '':
    break

  else:
    your_score = your_score + compute_score(line[0], line[2])

print(f' your score: {your_score}')
