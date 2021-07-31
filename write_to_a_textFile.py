file = open('file.txt', 'w')
file.write('My name is Sai Shyam')
file.write('\nI am 12')
file.close()

file = open('file.txt', 'r')
f = file.readlines()

newList = []

for line in f:
  if line[-1] == '\n':
    newList.append(line[:-1])
  else:
    newList.append(line)

print(newList)

file.close()
