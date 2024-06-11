# Python code to demonstrate dictionary 
# comprehension

# Lists to represent keys and values
keys = ['a','b','c','d','e']
values = [1,2,3,4,5] 

# but this line shows dict comprehension here 
myDict = { k:v for (k,v) in zip(keys, values)} 

# We can use below too
# myDict = dict(zip(keys, values)) 

print (myDict)



# Python code to demonstrate dictionary 
# creation using list comprehension
myDict = {x: x**2 for x in [1,2,3,4,5]}
print (myDict)

# given string
l="GFG"

# using dictionary comprehension
dic = {
	x: {y: x + y for y in l} for x in l
}

print(dic)


# List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist) 

# Using list comprehension to iterate through loop 
List = [character for character in [1, 2, 3]] 

# Displaying list 
print(List)

# Empty list 
List = [] 

# Traditional approach of iterating 
for character in 'Geeks 4 Geeks!': 
	List.append(character) 

# Display list 
print(List) 


# Import required module 
import time 


# define function to implement for loop 
def for_loop(n): 
	result = [] 
	for i in range(n): 
		result.append(i**2) 
	return result 


# define function to implement list comprehension 
def list_comprehension(n): 
	return [i**2 for i in range(n)] 


# Driver Code 

# Calculate time taken by for_loop() 
begin = time.time() 
for_loop(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for_loop:', round(end-begin, 2)) 

# Calculate time takens by list_comprehension() 
begin = time.time() 
list_comprehension(10**6) 
end = time.time() 

# Display time taken by for_loop() 
print('Time taken for list_comprehension:', round(end-begin, 2)) 


# Python Set from Comprehension

 Consider 4 strings in a list
list1 = ["wecome","to","sparkby","examples"]
print("List : ",list1)

# Create set from the list
converted = {i  for i in list1}
print("Set: ",converted)


 Consider 8 strings in a tuple
tuple1 = ("wecome","to","sparkby","examples","wecome","to","sparkby","examples")
print("Tuple : ",tuple1)

# Create set from the tuple
converted = {i  for i in tuple1}
print("Set: ",converted)

# Output:
# Tuple :  ('wecome', 'to', 'sparkby', 'examples', 'wecome', 'to', 'sparkby', 'examples')
# Set:  {'to', 'sparkby', 'examples', 'wecome'}
