results = [] # A dictionary to hold all possible answers and their scores
wordDictionary = [] # A dictionary to hold all the words we will check against to determine englishness

# Creates a dictionary list
with open('dictionary.txt', 'rb') as dictionaryFile:
  for word in dictionaryFile.read().split('\n'):
    wordDictionary.append(word.upper())

# Scores the string on simple heuristics
def scoreString(aString):
  wordCount = 0 # Worth 5 on my scoring system
  spaces = 0 # Worth 0.5 on my scoring system

  for word in aString.split():  # Splits by spaces by default
    spaces += 1
    if word.upper() in wordDictionary: # Remember to make all text uppercase like in the dictionary
      wordCount += 1

  score = (0.5 * spaces) + (5 * wordCount)
  return score

# XORs a string with a given byte 
def xorStringWithByte(aString, byte):
  decipheredText = ''
  for char in aString: # Decipher every char
    decipheredChar = chr(ord(char) ^ byte)
    if ord(decipheredChar) > 128 or ord(decipheredChar) < 32: # Yeah, I stayed up all night because I forgot the line feed
      if ord(decipheredChar) != 10 and ord(decipheredChar) != 13: # Its ugly, but Im tired so idgaf
        return {'string': 'INVALID TEXT'}# If its not a valid printable char, just stop now
    else:
      decipheredText += decipheredChar
  return {'score': scoreString(decipheredText), 'string': decipheredText, 'line': str(lineNumber+1), 'keyByte': chr(byte)} # If you are here the string is valid

# The main loop
with open('S1C4 - File Attachment.txt', 'rb') as cipheredData:
  for lineNumber, cipheredText in enumerate(cipheredData): # Look at each line
    for byte in xrange(256): # Try XORing with every character
      dehexedString = cipheredText.rstrip().decode('hex')
      result = xorStringWithByte(dehexedString, byte)
      if result['string'] != 'INVALID TEXT':
        results.append(result)

# Output the likely candidates
def getKey(item): # Define this so I can sort by score
  return item['score']

sortedResults = (sorted(results, key=getKey)) # Output the list of results by score
for entry in sortedResults:
  print entry

