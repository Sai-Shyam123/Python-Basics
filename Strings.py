# Strings

brand1 = 'amiGoscode'
print(brand1.upper())
print(brand1.lower())
print(brand1.capitalize())
print(len(brand1))
print(brand1.replace('e', 'E'))
print(brand1 == "amiGoscode")
print(brand1 != "amiGoscode")
print("code" in brand1)
print("code" not in brand1)

# Multiline comments

comment = "My Name Is Khalil And I am like A Happy Meal " \
          "I am Yakhi Arabi" \
          "Lakakakakak" \
          "kakaw"

comment1 = """
Hello Guys My Name Is Khalil And I'm Like A Happy Meal
Kakaw
Mamasidoo
!!!!!!!!!!!
"""

# Formatting Strings
print(comment1)
name_for_email = 'Sai Shyam'
email = """
Hello {} ,
How Are u ?
Nice meeting u .
"""

print(email.format(name_for_email))

age_for_email = 11
email1 = f"""
Hello {name_for_email} ,
How Are u ?
Nice meeting u .
age = {age_for_email + 3} 
"""

print(email1)