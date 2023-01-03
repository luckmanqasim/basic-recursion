
# Given 'n' as input, generate a list of numbers from 2^n-1 down to 0
def generateReverseOrder(n):
  # Implement me!
  if n == 0:
    return [""]
  else:
    partial_strings = generateReverseOrder(n-1)
    complete_strings = []
    for order in partial_strings:
      complete_strings.append("1" + order)
    for order in partial_strings:
      complete_strings.append("0" + order)
    return complete_strings


# Tester code; do not make any changes below here
print("Descending binary numbers:")
for i in range(1, 5):
  print(i, "bit:", *generateReverseOrder(i))

print("\nExpected:")
print("1 bit: 1 0")
print("2 bit: 11 10 01 00")
print("3 bit: 111 110 101 100 011 010 001 000")
print("4 bit: 1111 1110 1101 1100 1011 1010 1001 1000 0111 0110 0101 0100 0011 0010 0001 0000")
