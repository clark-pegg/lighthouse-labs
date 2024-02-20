def numberOfVowels(data):
  vowels = 0

  for character in data:
    if(character == "a" or character == "e" or character == "i" or character == "o" or character == "u"):
      vowels += 1

  return vowels

print(numberOfVowels("orange"))
print(numberOfVowels("lighthouse labs"))
print(numberOfVowels("aeiou"))