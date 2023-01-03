# Return a 3-element integer list containing number of consonants, vowels,
# and other characters (respectively) for the given string
import string

def countChars(s):
  # Implement me!
  if len(s) == 0:
    return [0,0,0]
  else:
    first_char = s[0]
    remaining_str = s[1:]
    partial_count = countChars(remaining_str)
    
    if first_char.lower() in ("a", "e", "i", "o", "u"):
      partial_count[1] += 1
    elif first_char.lower() in string.ascii_lowercase:
      partial_count[0] += 1
    else:
      partial_count[2] += 1
    
    return partial_count


# Tester code; you may make changes to the call to countChars(),
# to account for any extra parameters you may add
s = "abc de"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [3, 2, 1]")
print()
s = "To be or not to be"
print(s)
print("Consonants, Vowels, Other:", countChars(s))
print("Expected: [7, 6, 5]")
