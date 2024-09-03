my_list = [1, 2, 3, 4]
print("Original list:", my_list)

my_list.append(5)
print("After appending 5:", my_list)

my_list.remove(2)
print("After removing 2:", my_list)

my_list[0] = 10
print("After modifying first element to 10:", my_list)

my_dict = {'a': 1, 'b': 2, 'c': 3}
print("\nOriginal dictionary:", my_dict)

my_dict['d'] = 4
print("After adding key 'd' with value 4:", my_dict)

del my_dict['b']
print("After removing key 'b':", my_dict)

my_dict['a'] = 10
print("After modifying value of key 'a' to 10:", my_dict)

my_set = {1, 2, 3, 4}
print("\nOriginal set:", my_set)

my_set.add(5)
print("After adding 5:", my_set)

my_set.discard(2)
print("After discarding 2:", my_set)

my_set.discard(1)
my_set.add(10)
print("After modifying the set:", my_set)
