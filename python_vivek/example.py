#@tag:nextEditSuggestions : settings for code suggestion is turned off

# car = 'honda'
# carCap = car.upper()
# print(carCap)


'''
At the Python language level, you can think of everything as an object.

Even things that look like keywords or constants (None, True, functions, classes, modules, integers, strings) are objects.

This "everything is an object" design is one of the reasons Python is called a highly object-oriented language.
'''

x = 42

print(id(x))     # identity
print(type(x))   # type
print(x)         # value


# List: ordered and Mutable
item = ['tuktuk', 2, 3.14, True]
print(item) 

# Tuple: Ordered and immutable (cannot be changed).
tup1 = (1,2,34)
print(tup1, type(tup1))

# Dictionary:(JSON in JS): Stores data in key-value pairs.
dict1 = {
    'name': 'vivek', 
    'age': 31
}
dict1['name'] = 'vihu'
print(dict1, dict1['age'], dict1.get('age'), dict1.items())


# Set: Unordered collection of unique items.
colors = {"red", "green", "blue", 'blue'}
list = [1,3,5,8,9,8,8]
set1 = set(list)
print(set1, colors)


# Input
# ipNum = int(input())
# print(ipNum)
# if(ipNum < 4):
#     print('The entered input is less than 4')
# elif (ipNum == 4):
#     print('The entered num is 4')
# else:
#     print('The entered num is greater than 4')




# for i in range(0, 5):
#     print(i)

# j = 0
# while (j<5):
#     print('while',j)
#     j+=1


# Function and Error Handle
def average(num1, num2):
    try:
        print(segredgd)
        avg = (num1 + num2)/2
        return avg
    except Exception as e:
        print('Custom error::', e)

res = average(10,20)
res1 = average(20, 30)
print(res, res1)
print(1+3)


file = open("customFileName.txt", "w" )
file.write("This is a beginners code")
file.close()
print(file)

file1 = open("customFileName.txt", "r" )
content = file1.read()
file1.close()
print(content)



