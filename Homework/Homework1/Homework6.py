#Using everything we learned to day about Functional Programing, lambda and itters create one of each of the following:
#Basic Lambda Function
# Create a lambda function that takes one arguments and returns even or odd.
#Advanced lambda Function
# Create a lambda function that takes a list and returns their sum 
# Sorting with Lambda
# Filtering with Lambda - `filter()` 
# Mapping with Lambda - `map()`
# Reducing with Lambda -  `reduce()` 
# Enumerate with or without Lambda - `enumerate()`
# zip with or without lambda (may combine enumerate like in class) - `zip()`

#Create a lambda function that takes one arguments and returns even or odd.
even_odd = lambda x: 'The number is even' if x % 2 == 0 else 'The number is odd'
print (even_odd(5))

#Create a lambda function that takes a list and returns their sum 
summing = lambda list: sum(list)
listomatic = [2,4,3,5,1]
print('The sum of the list is: ', summing(listomatic))

#Sorting with Lambda
listomatic.sort(key=lambda x: x, reverse=False)
print('Lambda sorted list:', listomatic)

#Filtering with Lambda - `filter()` 
filteredlist = list(filter(lambda x: x % 2 == 0, listomatic))
print('Lambda filtered list:', filteredlist)

#Mapping with Lambda - `map()`
squared = list(map(lambda x: x**2, listomatic))
print('Lambda mapped list:', squared)

#Reducing with Lambda -  `reduce()` 
from functools import reduce
sumbutcomplicated = reduce(lambda x,y: x + y, listomatic)
print ('Lambda reduced list:', sumbutcomplicated)

#Enumerate with or without Lambda - `enumerate()`
listofwords = ['what', 'du', 'hell', 'big', 'boy']
for i, word in enumerate(listofwords):
    print(f"Place {i}: {word}")

#zip with or without lambda (may combine enumerate like in class) - `zip()`
alltogethernowbaby = zip(listomatic, listofwords)
print(list(alltogethernowbaby))