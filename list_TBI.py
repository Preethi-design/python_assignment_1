print("List Methods")

#list
animals = ['cat', 'dog', 'rabbit']
animal = ['cow']

print("# Append")
animals.append('pig')
print('Updated animals list: ', animals)

print("# extend")
animals.extend(animal)
print('Updated animals list: ', animals)

print("#copy method")
old_list = [1, 2, 3]
new_list = old_list
new_list.append('a')
print('New List:', new_list)
print('Old List:', old_list)

print("#count method")
vowels = ['a', 'e', 'i', 'o', 'i', 'u']
count = vowels.count('i')
print('The count of i is:', count)

print("#index method")
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
vowel = ['a', 'e', 'i', 'u']

print("#pop item")
languages = ['Python', 'Java', 'C++', 'French', 'C']
return_value = languages.pop(3)
print('Return Value:', return_value)

print("# Updated List")
print('Updated List:', languages)

print("#remove")
animals = ['cat', 'dog', 'rabbit', 'guinea pig']
animals.remove('rabbit')

print("# Updated animals List")
print('Updated animals list: ', animals)

print("#Reverse")
systems = ['Windows', 'macOS', 'Linux']
print('Original List:', systems)
systems.reverse()

print("# updated list")
print('Updated List:', systems)
vowels = ['e', 'a', 'u', 'o', 'i']

print("# sort")
vowels.sort()
print('Sorted list:', vowels)

print("#clear")
list = [{1, 2}, ('a'), ['1.1', '2.2']]
list.clear()
print('List:', list)
