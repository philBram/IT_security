import sys
import getopt

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
      -k, --key             Specify encryption/decryption key (0 - 255)''')

    exit(0)


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

if len(args) > 1 or len(fOut) <= 0 or int(key) > 255 or int(key) < 0:
    showUsage()

with open(fIn, 'r') as fInput:
    inContent = fInput.read()
    outContent = ""

    if encrypt:
        for char in inContent:
            if ord(char) < 256 and ord(char) >= 0:
                outContent += chr((ord(char) + int(key)) % 255)
        
    else:
        for char in inContent:
            outContent += chr((ord(char) + (255 - int(key))) % 255)

    with open(fOut, 'w') as fOutput:
        fOutput.write(outContent)