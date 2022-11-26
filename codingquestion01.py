import re

phone=input("Enter Phone Number: ")

pattern=re.compile("(\(?\)?\s?-?\.?)")

if pattern.match(phone):
    print("Valid Phone Number!")
else:
    print("Not Valid")