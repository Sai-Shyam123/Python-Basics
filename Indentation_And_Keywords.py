import keyword

# Indentation And Keyword

name2 = 'Indhu'
surname = 'BlaahBlaah'

# So this piece of code cannot be written as
"""
name2 = 'Indhu'
    surname = 'BlaahBlaah'

    #So There shoudl be no indentation
"""


# But Indentation is possible inside functions and non intended text does not work inside methods
def my_function():
    name3 = 'Indhu'
    surname3 = 'BlaahBlaah'


# Reserved Keywords
print(keyword.kwlist)