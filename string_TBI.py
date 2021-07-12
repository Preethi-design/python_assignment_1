print("string methods")
string = "python is AWesome."
print(string)

print("#capitalize")
capitalized_string = string.capitalize()
print('Old String: ', string)
print('Capitalized String:', capitalized_string)

print("#center")
string = "Python is awesome"
new_string = string.center(24)
print("Centered String: ", new_string)

print("#casefold")
string = "PYTHON IS AWESOME"
print("# print lowercase string")
print("Lowercase string:", string.casefold())

print("#count()")
string = "Python is awesome, isn't it?"
substring = "is"
count = string.count(substring)
print("The count is:", count)

print("#endswith")
text = "Python is easy to learn."
result = text.endswith('to learn')
print(result)

print("#expandtabs")
str = 'xyz\t12345\tabc'
result = str.expandtabs()
print(result)

print("#encode")
string = 'pythön!'
print('The string is:', string)
string_utf = string.encode()
print('The encoded version is:', string_utf)

print("#find")
quote = 'Let it be, let it be, let it be'
result = quote.find('let it')
print("Substring 'let it':", result)

if (quote.find('be,') != -1):
    print("Contains substring 'be,'")
else:
    print("Doesn't contain substring")

print("#format")
print("Hello {}, your balance is {}.".format("Adam", 230.2346))
print("Hello {0}, your balance is {blc}.".format("Adam", blc=230.2346))

print("#index")
sentence = 'Python programming is fun.'
result = sentence.index('is fun')
print("Substring 'is fun':", result)

print("#isalnum")
name = "M234onica"
print(name.isalnum())

print("# contains whitespace")
name = "M3onica Gell22er "
print(name.isalnum())
name = "133"
print(name.isalnum())

print("#isalpha")
name = "Monica"
print(name.isalpha())

print("#isdecimal")
s = "28212"
print(s.isdecimal())

print("# contains alphabets")
s = "32ladk3"
print(s.isdecimal())

print("# contains alphabets and spaces")
s = "Mo3 nicaG el l22er"
print(s.isdecimal())

print("#isdigit")
s = "28212"
print(s.isdigit())

print("# contains alphabets and spaces")
s = "Mo3 nicaG el l22er"
print(s.isdigit())

print("#isidentifier")
str = 'Python'
print(str.isidentifier())
str = 'Py thon'
print(str.isidentifier())

print("#islower")
s = 'this is good'
print(s.islower())

print("#isnumeric")
s = '1242323'
print(s.isnumeric())

print("#isprintable")
s = 'Space is a printable'
print(s)
print(s.isprintable())

print("#isspace")
s = '   \t'
print(s.isspace())

print("#istitle")
s = 'Python Is Good.'
print(s.istitle())

print("#isupper")
string = "THIS IS ALSO G00D!"
print(string.isupper());

print("#join")
numList = ['1', '2', '3', '4']
separator = ', '
print(separator.join(numList))

print("#split")
text= 'Love thy neighbor'
# splits at space
print(text.split())

print("#rsplit")
text= 'Love thy neighbor'
# splits at space
print(text.rsplit())

print("#splitlines")
grocery = 'Milk\nChicken\r\nBread\rButter'
print(grocery.splitlines())

print("#startswith")
text = "Python is easy to learn."
result = text.startswith('is easy')
# returns False
print(result)

print("#title")
text = 'My favorite number is 25.'
print(text.title())

print("#zfills")
text = "program is fun"
print(text.zfill(15))
print(text.zfill(20))

print("#format_map")
point = {'x':4,'y':-5}
print('{x} {y}'.format(**point))
