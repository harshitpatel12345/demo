my_set = {1, 2, 3, 4, 5}

my_set.add(6)
my_set.add(7)

my_set.remove(5)

print("Is 3 in the set?", 3 in my_set)
print("Length of the set:", len(my_set))

other_set = {4, 5, 6, 8}

print("Union of sets:", my_set.union(other_set))
print("Intersection of sets:", my_set.intersection(other_set))
print("Difference of sets:", my_set.difference(other_set))

print("Elements in the set:")
for element in my_set:
    print(element)

my_set.clear()

print("Is the set empty?", len(my_set) == 0)
