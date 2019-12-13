'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    #declase your test string variable
    test = 'th'
    #base case: if length of word is less than the test string length: 2; return 0
    if len(word) < 2:
      return 0
    #if the length of the word is the length, return 1, else return 0 if the string doesn't match
    if len(word) == 2:
      if word[:2] == test:
        return 1
      else:
        return 0
    #start at first two indeces,  if they match the test string, return one and recursively call count_th on the rest of the string, else return 0 and recursively call count_th on rest of string
    #NOTE that this only works based off the assumption that our test string is only 2 characters in length
    if word[0] + word[1] == test:
      print(word[1:])
      return 1 + count_th(word[1:])
    else:
      print(word[1:])
      return 0 + count_th(word[1:])



# print(count_th('health'))