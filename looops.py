# count = 1
# while count <= 5:
#     print("hello")
#     count += 1

# print(count)
# #print number from 1 to 5
# i = 1
# while i<= 5:
#     print(i)
#     i +=1
# i = 100
# while i>= 1:
#     print(i)
#     i -=1


#print the multiplication table of a number n
# n = int(input("enter number:"))
# i = 1
# while i<= 10:
#     print(n*i)
#     i += 1


#print the element of the folling list using a loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
num =[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

idx = 0
while idx < len(num):
    print(num[idx])
    idx += 1
#search for a number x in this tuple using loop
#[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

num =(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)

x = 36

i = 0
while i<len(num):
    if(num[i] == x):
        print("found and idx", i)
    i += 1