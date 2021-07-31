import re

text = 'Arandom09DHHBHBHghuufhue87873 string.'

pattern1 = re.compile("[ABC]")
pattern2 = re.compile("[a-z]")
pattern3 = re.compile("[A-Z]")
pattern4 = re.compile("[a-zA-Z0-9]+")

result = pattern1.search(text)
result1 = pattern2.search(text)
result2 = pattern3.search(text)
result3 = pattern4.search(text)


# print(result)
# print(result1)
# print(result2)
# print(result3)


#Email Project
text1 = input('input random text(include email in correct format anywhere in the text):')
pattern_for_email = re.compile('[a-zA-Z0-9\.\-\_]+\@[a-zA-Z0-9]+\.[a-zA-Z]+')
result_for_email = pattern_for_email.findall(text1)
print(result_for_email)
