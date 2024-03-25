'''List comprehensions provide a concise way to create lists. 

It consists of brackets containing an expression followed by a for clause, then
zero or more for or if clauses. The expressions can be anything, meaning you can
put in all kinds of objects in lists.

The result will be a new list resulting from evaluating the expression in the
context of the for and if clauses which follow it. 

The list comprehension always returns a result list. '''


'''
new_list = []
for i in original_list:
    if filter(i):
        new_list.append(expressions(i))  '''

#You can obtain the same thing using list comprehension:

# new_list = [expression(i) for i in original_list if filter(i)]


#The list comprehension starts with a '[' and ']', to help you remember that the
#result is going to be a list.

#There are 3 parts to list comprehension:

#*result*  = [*transform/expression*    *iteration*         *filter/condition*     ]

#The filter part answers the question if the item should be transformed.


old_list = [1,2,3,4,5]
new_list = []

for i in old_list:
    j = i **2
    new_list.append(j)

print(new_list)

new_list = [i**2 for i in old_list ]

print(new_list)

#1) creating a simple list of 10 numbers using range()
x = [i for i in range(10)]
print(x)

#2) creating a list that evaluates an expression
squares = [x**2 for x in range(10)]
print(squares)

#3) creating a list from another list
list1 = [3,4,5]

multiplied = [item*3 for item in list1]
print(multiplied)

#4) using list comprehension for string manipulation

listofwords = ["The","Force","will","be","wuth","you.","Always."]

items = [word[1].upper() for word in listofwords]
print(items)

#5) show lower case

result = [x.lower() for x in ["A","B","C"]]
print(result)

#6) Creating a list based on a condition
# create a list of the square of all even numbers from 1 to 10

new_range = [i*i for i in range(1,11) if i%2 == 0]
print(new_range)

#7) Extracting numbers only from a string and putting it in a list
string = "Hello 12345 world"
numbers = [int(character) for character in string if character.isdigit()]
print(numbers)
letters = [x.upper() for x in string.split(' ') if x.isalpha()]
print(letters)


#8) get a specific line from a text file

infile = open('test.txt','r')

result = [i.rstrip('\n') for i in infile if 'line3' in i]
print(result)

#9) Using functions in list comprehension

def double(x):
    return x * 2


result = [double(x) for x in range(1,11) if x % 2 ==1]
print(result)

#10) you can add more arguments (using multiple iterators and lists):

a = [(x,y) for x in [10,50] for y in [20,40]]
print(a)

a = [x+y for x in [10,50] for y in [20,40] if x+y>70]
print(a)



## Exercise ##

# 1 Using a list comprehension, create a new list called "newlist" out of the list "numbers", 
# which contains only the positive numbers from the list, as integers.

numbers = [34.6, -203.4, 44.9, 68.3, -12.2, 44.6, 12.7]




## 2 create a list of integers which specify the length of each word in
## a sentence except for the word 'the'

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()



## Given dictionary is consisted of vehicles and their weights in kilograms. 
## Contruct a list of the names of vehicles with weight below 5000 kilograms. 
## In the same list comprehension make the key names all upper case.

dict={"Sedan": 1500, "SUV": 2000, "Pickup": 2500, "Minivan": 1600, "Van": 2400, 
"Semi": 13600, "Bicycle": 7, "Motorcycle": 110}




## Find all the numbers from 1 to 1000 that have a 4 in them



## count how many times the word 'the' appears in the text file - 'sometext.txt'



## Extract the numbers from the following phrase ##

phrase = 'In 1984 there were 13 instances of a protest with over 1000 people attending. On average there were 15 reported injuries at each " \
"event, with about 3 or 4 that were classifled as serious per event.'






