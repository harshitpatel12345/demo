my_dict = {'apple': 5, 'banana': 10, 'orange': 7}

print("Number of apples:", my_dict['apple'])

my_dict['grape'] = 3

my_dict['banana'] = 15

del my_dict['orange']

if 'grape' in my_dict:
    print("Grapes are in the dictionary")

print("Keys:", my_dict.keys())

print("Values:", my_dict.values())

print("Key-Value pairs:")
for key, value in my_dict.items():
    print(key, "-", value)

my_dict.clear()

if not my_dict:
    print("Dictionary is empty")
