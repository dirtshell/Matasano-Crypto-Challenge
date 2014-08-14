import base64

rawHex = '1c0111001f010100061a024b53535009181c'
decodedHex = rawHex.decode("hex")

XOROperatorHex = '686974207468652062756c6c277320657965'
decodedXOROperatorHex = XOROperatorHex.decode("hex")

def XORStrings(stringA, stringB):
  outputString = "" # Ouptut string is empty for now
  binaryA = stringA.decode("hex") # The plaintext of stringA
  binaryB = stringB.decode("hex") # The plaintext of stringB
  for x, y in zip(binaryA, binaryB): # Zip it up so each char has an XOR operator matched to it
    outputString += chr(ord(x) ^ ord(y)) # Append the result of the XOR as a character to the outputString
  return outputString

print(XORStrings(rawHex, XOROperatorHex))