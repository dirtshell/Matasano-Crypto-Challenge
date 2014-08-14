import base64

def hex_b64(aString):
  return base64.b64encode(aString.decode("hex")) # Convert the hex to binary and the binary to base64

text = '49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d'
print(hex_b64(text))


