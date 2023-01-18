import sys

programName = sys.argv[0]
asciiCountArray = []
totalCount = 0

for i in range(256):
    asciiCountArray.append([i, 0])


def showUsage():
    print(f'Usage: {programName} file')
    exit(0)


def printResult():
    print('ascii result statistic (chars with 0 count not showing)\n---------------------------------------------------------------')
    print('total count:\t\t' + str(totalCount) + '\n')

    asciiCountArray.sort(key=lambda x: x[1], reverse=True)

    for li in asciiCountArray:
        if li[1] > 0:

            asciiChar = ""

            if (li[0] >= 0x21 and li[0] <= 0x7E) or (li[0] >= 0xA1 <= 0xAC) or (li[0] >= 0xAE and li[0] <= 0xFF):
                asciiChar = "'" + chr(li[0]) + "'"
            
            else:
                asciiChar = ascii(chr(li[0]))
            
            asciiChar += '\t\tcount:\t' + str(li[1])
            asciiChar += '\t\tpercent:\t' + str(round((li[1] / totalCount) * 100, 3)) + '%'

            print(asciiChar)


try:
    fIn = sys.argv[1]
except:
    showUsage()

if len(sys.argv) > 2:
    showUsage()

with open(fIn, 'r') as fInput:
    inContent = fInput.read()

    for char in inContent:
        if ord(char) < 256 and ord(char) >= 0:
            asciiCountArray[ord(char)][1] += 1
            totalCount += 1

printResult()