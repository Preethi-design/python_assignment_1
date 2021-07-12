print("Dictionary Methods")
d = {1: "one", 2: "two"}
print(d)
print("#clear")
d.clear()
print('d =', d)

print("#copy()")
original = {1:'one', 2:'two'}
new = original.copy()
print('Orignal: ', original)
print('New: ', new)

print("#From Keys")
keys = {'a', 'e', 'i', 'o', 'u' }
vowels = dict.fromkeys(keys)
print(vowels)

print("#get()")
person = {'name': 'Phill', 'age': 22}
print('Name: ', person.get('name'))
print('Age: ', person.get('age'))

print("#items()")
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
print(sales.items())

print("#keys")
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
print(person.keys())

print("#popitem()")
person = {'name': 'Phill', 'age': 22, 'salary': 3500.0}
result = person.popitem()
print('Return Value = ', result)
print('person = ', person)

print("#setdefault")
person = {'name': 'Phill', 'age': 22}
age = person.setdefault('age')
print('person = ',person)
print('Age = ',age)

print("#pop")
sales = { 'apple': 2, 'orange': 3, 'grapes': 4 }
element = sales.pop('apple')
print('The popped element is:', element)
print('The dictionary is:', sales)

print("#update")
d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)
print(d)

print("#add")
d1 = {3: "three"}
d.update(d1)
print(d)
