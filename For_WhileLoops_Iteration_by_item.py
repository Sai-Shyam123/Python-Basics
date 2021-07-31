# For Loops

for loop in range(0, 10, 2): # start, stop, step
    print(loop)

# While Loops

loop = True

while loop:
    password = input('Insert stop: ')
    if password == 'stop':
        break

#Iteration By Item

fruits = ['apples', 'pears', 'strawberries', 'mangos', 'sapota', 67, 76876, 9898]

for fruit in fruits:
    print(fruit)

print('1st loop is done!')

for fruit in fruits:
    if fruit == 'pears':
        print(fruit)

    else:
        print('Not pears')

print('blaahblaah')

for x in range(0, 8):
    if fruits[x] == 'pears':
        print(fruits[x])

    else:
        print('not pears')


print('Not blaah')


for blaah in range(len(fruits)):
    
    if fruits[blaah] == 'pears':
        print(fruits[blaah])

    else:
        print('not pears')



