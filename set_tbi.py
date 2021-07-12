#set
print("Set Methods")
vowels = {'a', 'e', 'i', 'u'}
print(vowels)

print("# adding")
vowels.add('o')
print('Vowels are:', vowels)

print("# clearing vowels")
vowels.clear()
print('Vowels (after clear):', vowels)

print("# copy()")
x=vowels.copy()

print("#Difference")
A = {'a', 'b', 'c', 'd'}
B = {'c', 'f', 'g'}
print(A.difference(B))
print(B.difference(A))

print("# Difference update")
result = A.difference_update(B)
print('A = ', A)
print('B = ', B)
print('result = ', result)
numbers = {2, 3, 4, 5}

print("# discard")
numbers.discard(3)
print('numbers = ', numbers)
numbers.discard(10)
print('numbers = ', numbers)

print("#Intersection")
A = {2, 3, 5, 4}
B = {2, 5, 100}
C = {2, 3, 8, 9, 10}
print(B.intersection(A))
print(B.intersection(C))
print(A.intersection(C))
print(C.intersection(A, B))

print("#Intersection Update")
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
result = A.intersection_update(B)
print('result =', result)
print('A =', A)
print('B =', B)

print("#isdisjoint")
A = {1, 2, 3, 4}
B = {2, 3, 4, 5}
result = A.intersection_update(B)
print('result =', result)
print('A =', A)
print('B =', B)

print("#issubset")
A = {1, 2, 3}
B = {1, 2, 3, 4, 5}
C = {1, 2, 4, 5}
print(A.issubset(B))
print(B.issubset(A))
print(A.issubset(C))
print(C.issubset(B))

print("#pop")
A ={'a', 'b', 'c', 'd'}
print('Return Value is', A.pop())
print('A = ', A)
      
print("#symmetric Difference")
A = {'a', 'b', 'c', 'd'}
B = {'c', 'd', 'e' }
C = {}
print(A.symmetric_difference(B))
print(B.symmetric_difference(A))
print(A.symmetric_difference(C))
print(B.symmetric_difference(C))

print("#symmetric difference update")
A = {'a', 'c', 'd'}
B = {'c', 'd', 'e' }
result = A.symmetric_difference_update(B)
print('A =', A)
print('B =', B)
print('result =', result)

print("#union")
A = {'a', 'c', 'd'}
B = {'c', 'd', 2 }
C = {1, 2, 3}
print('A U B =', A.union(B))
print('B U C =', B.union(C))
print('A U B U C =', A.union(B, C))
print('A.union() =', A.union())

print("#update")
A = {'a', 'b'}
B = {1, 2, 3}
result = A.update(B)
print('A =', A)
print('result =', result)
