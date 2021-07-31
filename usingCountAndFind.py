# .find() , .count()

string = input('Please type something : ')
print(string.find('lo'))
print(string.count('h'))

if string.count('_') > 1:
    print('Nope')
else :
    print('nice')