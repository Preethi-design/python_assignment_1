print("-------------For Loop---------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print("-------------Break--------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break
print("-------------Continue--------------------")
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
  
print("-------------Range()--------------------")
for x in range(6):
  print(x)

print("-------------Range() and else--------------------")
for x in range(6):
  print(x)
else:
  print("Finally finished!")

print("-------------Nested loop--------------------")
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)
print("-------------pass--------------------")
for x in [0, 1, 2]:
  pass
