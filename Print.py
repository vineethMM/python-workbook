def get_row(dimension, filler, length, border):
  return border + (filler * length + border) * dimension

def print_square(dimension, length):
  for row in range((dimension * length) + 1):
    if(row % length == 0):
      print(get_row(dimension, "-", length, "+"))
    else:
      print(get_row(dimension, " ", length, "|"))   

print_square(2, 5)      