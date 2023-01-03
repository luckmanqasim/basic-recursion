# This function must create a string from 's' that is reversed, where each
# character is duplicated 3 times and then separated by a space
def tripleSpaced(s):
  # Implement me!
  if len(s) == 0:
    return ""
  else:
    return tripleSpaced(s[1:]) + " " + s[0] * 3

# Tester code; do not make any changes below here
print("testing!:", tripleSpaced("testing!"))
print("Expected:  !!! ggg nnn iii ttt sss eee ttt")
print()
print("triple-spaced:", tripleSpaced("triple-spaced"))
print("Expected:       ddd eee ccc aaa ppp sss --- eee lll ppp iii rrr ttt")
print()
print("recursion is fun:", tripleSpaced("recursion is fun"))
print("Expected:          nnn uuu fff     sss iii     nnn ooo iii sss rrr uuu ccc eee rrr")
