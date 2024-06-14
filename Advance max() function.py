#Syntax of max() with Example
#ex#ample of max()
numbers = [2, 5, 3, 7, 1]
maximum_number = max(numbers)
print(maximum_number)


## Python max() Index
# # function to find minimum and maximum position in list
def maximum(a, n):

	# inbuilt function to find the position of maximum
	maxpos = a.index(max(a))

	# printing the position
	print ("The maximum is at position", maxpos + 1)

# driver code
a = [3, 4, 1, 3, 4, 5]
maximum(a, len(a))

    #  Example creating a list  
my_strings = ["Apple", "Mango", "Banana", "Papaya", "Orange"]  
large_str = max(my_strings)  
print("The largest string in the list:", large_str)  

      #Example creating a list  
my_dict = {1 : 1, -3 : 9, 2 : 4, -5 : 25, 4 : 16}  
key_1 = max(my_dict)  
print("The largest key in the dictionary:", key_1)  
       
key_2 = max(my_dict, key = lambda x : my_dict[x])   
print("The Key of the largest value in the dictionary:", key_2)    
print("The largest value in the dictionary:", my_dict[key_2])  


## using the max() function with objects as numbers  
large_num = max(10, -4, 5, -3, 13)  
      
    # printing the result  
print("The largest number:", large_num)  
    # using the max() function with objects as numbers  
large_num = max(10, -4, 5, -3, 13)  
      
    # printing the result  
print("The largest number:", large_num)  
