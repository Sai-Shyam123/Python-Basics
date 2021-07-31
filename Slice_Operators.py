#Slice Operators

fruits = ['apples', 'bananas', 'pears']
text = 'Hello I Like Python'

# When we leave it blank it sets the default stop to the max index num and start to 0
print(text[0:len(text)-1:3])
print(fruits[:2])

# We can also add stuff to lists using slice_operators
fruits[1:1] = 'm'
print(fruits)
