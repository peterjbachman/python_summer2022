# Fibonacci sequence
# X_[i] = X_[i-1] + X_[i-2], where X_1 = 1, X_2 = 1
# 1,1,2,3,5,8,....

# Write a for loop, while loop, or function (or all three!) to create a
# list of the first 10 numbers of the fibonacci sequence
x = []
for i in range(0, 10):
  if i == 0:
    x.append(1)
  elif i == 1:
    x.append(1)
  else:
    x.append(x[i - 1] + x[i - 2])
x

"""return true if there is no e in 'word', else false"""
def has_no_e(word):
  return(not ("e" in word))

"""return true if there is e in 'word', else false"""
def has_e(word):
  return("e" in word)

"""return true if word1 contains only letters from word2, else false"""
def uses_only(word1, word2):
  return all(letters in word1 for letters in word2)

uses_only("centaur", "cent")

"""return true if word1 uses all the letters in word2, else false"""
def uses_all(word1, word2):
  return all(letters in word2 for letters in word1)

uses_all("centrau", "centaur")

"""true/false is the word in alphabetical order?"""
# Hint: check the methods for lists
def is_abecedarian(word):
  alpWord = sorted(word)
  orgWord = [i for i in word]
  return alpWord == orgWord
