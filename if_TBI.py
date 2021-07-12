a = 10
b = 20
print("_____________________ if _______________________")
if b > a:
  print("b is greater than a")

print("_______________________ elif ______________________")

if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")

print("______________________ else _______________________")
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")
print("_______________________ and ______________________")
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

print("________________________ or _____________________")
a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")
print("_______________ Nested if ______________________________")
x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")
