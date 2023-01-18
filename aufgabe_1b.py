import sys
import getopt
from turtle import clear

fOut = ""
fIn = ""
encrypt = True
key = -1
progName = sys.argv[0]


def showUsage():
    print(f'''Usage: {progName} [options] file
    Options:
      -h, --help            Display this information
      -o, --output          Specify output file
      -d, --decrypt         Decrypt (default is encrypt)
      -k, --key             Specify encryption/decryption key (1 - 100)''')

    exit(0)


def encryption(key, clearText, cipher, offset=0, index=0, lastIndex=0):
    if lastIndex >= len(cipher):
        return clearText
    
    while index + offset < len(cipher):
        clearText[index + offset] = cipher[lastIndex]
        lastIndex += 1
        index += key + 1

    return encryption(key, clearText, cipher, offset=offset + 1, lastIndex=lastIndex)


def decryption(key, clearText, cipher="", offset=0, index=0):
    while index + offset < len(clearText):
        cipher += clearText[index + offset]
        index += key + 1

    if offset == key and index + offset >= len(clearText):
        return cipher
    
    return decryption(key, clearText, cipher, offset=offset + 1)


try:
    opts, args = getopt.getopt(sys.argv[1:], 'o:k:dh', ['output=', 'key=', 'help', 'decrypt'])
    fIn = args[0]
except:
    showUsage()

for opt, arg in opts:
    if opt in ['-o', '--output']:
        fOut = arg
    elif opt in ['-k', '--key']:
        key = arg
    elif opt in ['-d', '--decrypt']:
        encrypt = False
    elif opt in ['-h', '--help']:
        showUsage()

if len(args) > 1 or len(fOut) <= 0 or int(key) > 100 or int(key) < 1:
    showUsage()

with open(fIn, 'r') as fInput:
    inContent = fInput.read()
    outContent = ""

    if encrypt:
        outContent = "".join(encryption(int(key), [""] * len(inContent), inContent))
    else:
        outContent = decryption(int(key), inContent)

    with open(fOut, 'w') as fOutput:
        fOutput.write(outContent)