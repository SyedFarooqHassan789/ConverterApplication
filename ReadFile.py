codesDictionary = {}
file = open('./data/Codes.txt', 'r')
for line in file.readlines():
    alphabet, code = line.split(':')
    codesDictionary[alphabet] = code
