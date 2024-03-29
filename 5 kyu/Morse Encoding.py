class Morse:
    @classmethod
    def encode(self,message):
        res=[]
        for i in message.split():
            temp=[]
            for char in i:
                temp.append(alpha[char])
            res.append("000".join(temp))
        string="0000000".join(res)
        string+="" if len(string)%32==0 else "0"*(32-len(string)%32)
        numbers=[]
        for i in range(0, len(string), 32):
            numbers.append(to_twos_complement(string[i:i+32], 32))
        return numbers
    @classmethod
    def decode(self,array):
        binary=""
        for i in array:
            binary+=from_twos_complement(i, 32)
        res=[]
        for i in binary.rstrip("0").split("0000000"):
            temp=""
            for j in i.split("000"):
                temp+=alpha2[j]
            res.append(temp)
        return " ".join(res) 
def to_twos_complement(binary, bits):
    binary="".join(binary.split())
    res= -(2**(bits-1)) if binary[0]=="1" else 0
    for i in range(1, bits):
        res+=2**(bits-1-i) if binary[i]=="1" else 0
    return res
def from_twos_complement(n, bits):
    if n>=0:
        return "0"*(bits-len(bin(n)[2:]))+bin(n)[2:]
    else:
        remain=abs(-(2**(bits-1))-n)
        return "1"+"0"*(bits-len(bin(remain)[2:])-1)+bin(remain)[2:]
alpha={
  'A': '10111',
  'B': '111010101',
  'C': '11101011101',
  'D': '1110101',
  'E': '1',
  'F': '101011101',
  'G': '111011101',
  'H': '1010101',
  'I': '101',
  'J': '1011101110111',
  'K': '111010111',
  'L': '101110101',
  'M': '1110111',
  'N': '11101',
  'O': '11101110111',
  'P': '10111011101',
  'Q': '1110111010111',
  'R': '1011101',
  'S': '10101',
  'T': '111',
  'U': '1010111',
  'V': '101010111',
  'W': '101110111',
  'X': '11101010111',
  'Y': '1110101110111',
  'Z': '11101110101',
  '0': '1110111011101110111',
  '1': '10111011101110111',
  '2': '101011101110111',
  '3': '1010101110111',
  '4': '10101010111',
  '5': '101010101',
  '6': '11101010101',
  '7': '1110111010101',
  '8': '111011101110101',
  '9': '11101110111011101',
  '.': '10111010111010111',
  ',': '1110111010101110111',
  '?': '101011101110101',
  "'": '1011101110111011101',
  '!': '1110101110101110111',
  '/': '1110101011101',
  '(': '111010111011101',
  ')': '1110101110111010111',
  '&': '10111010101',
  ':': '11101110111010101',
  ';': '11101011101011101',
  '=': '1110101010111',
  '+': '1011101011101',
  '-': '111010101010111',
  '_': '10101110111010111',
  '"': '101110101011101',
  '$': '10101011101010111',
  '@': '10111011101011101',
  ' ': '0'  # Technically is 7 0-bits, but we assume that a space will always be between two other characters
}
alpha2={'10111': 'A', '111010101': 'B', '11101011101': 'C', '1110101': 'D', '1': 'E', '101011101': 'F', '111011101': 'G', '1010101': 'H', '101': 'I', '1011101110111': 'J', '111010111': 'K', '101110101': 'L', '1110111': 'M', '11101': 'N', '11101110111': 'O', '10111011101': 'P', '1110111010111': 'Q', '1011101': 'R', '10101': 'S', '111': 'T', '1010111': 'U', '101010111': 'V', '101110111': 'W', '11101010111': 'X', '1110101110111': 'Y', '11101110101': 'Z', '1110111011101110111': '0', '10111011101110111': '1', '101011101110111': '2', '1010101110111': '3', '10101010111': '4', '101010101': '5', '11101010101': '6', '1110111010101': '7', '111011101110101': '8', '11101110111011101': '9', '10111010111010111': '.', '1110111010101110111': ',', '101011101110101': '?', '1011101110111011101': "'", '1110101110101110111': '!', '1110101011101': '/', '111010111011101': '(', '1110101110111010111': ')', '10111010101': '&', '11101110111010101': ':', '11101011101011101': ';', '1110101010111': '=', '1011101011101': '+', '111010101010111': '-', '10101110111010111': '_', '101110101011101': '"', '10101011101010111': '$', '10111011101011101': '@', '0': ' '}