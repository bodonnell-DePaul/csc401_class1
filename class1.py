# Translate the following into Python algebraic or Boolean expressions and then evaluate them:

#a The difference between Annie’s age (25) and Ellie’s (21)
25-21
#b The total of $14.99, $27.95, and $19.83
14.99 + 27.95 + 19.83
sum(14.99, 27.95, 19.83)
#c The area of a rectangle of length 20 and width 15
20*15
#d 2 to the 10th power
2**10
#e The minimum of 3, 1, 8, -2, 5, -3, and 0
min(3, 1, 8, -2, 5, -3, 0)
#f 3 equals 4-2
3 == 4-2
#g The value of 17//5 is 3
17 //5 == 3
#h The value of 17%5 is 3
17%5 == 3
#i 284 is even
284%2 == 0
#j 284 is even and 284 is divisible by 3
284%2 == 0 and 284 // 3 == 0 
#k 284 is even or 284 is divisible by 3
284%2 == 0 or 284 // 3 == 0 

#Assignment of string and other variables
snake_case = 'snake_case'
camelCase = 'camelCase'
PascalCase = 'PascalCase'
kebobCase = 'a liar!'
booInternet  = 'Brian O\'Donnell'
myName = "Brian O'Donnell"
multiLineString = '''
lots of text
over mulitple lines
and it is glorious
'''

#String operations
# + concat
booInternet + kebobCase
me = 'me'
me in camelCase #Evaluates to True
me not in camelCase #evaluates to False

#indicies and lenth
len(PascalCase) #equal 10
#index always start at 0
PascalCase[10] #throws in index out of bounds error

PascalCase[len(PascalCase)-1] 
PascalCase[-1]                
#'e'
PascalCase[-9] 
#'a'
PascalCase[-10]
#'P'
PascalCase[-1:-3] 
#''
PascalCase[-3:-1] 
#'as'
PascalCase[1:4]   
#'asc'
len(PascalCase + camelCase)  
#19

#Recap
#boolean True / False
#integers whole numbers 1,2,3,4,5,6 etc.
#floating points aka float which are decimals 1.5, 2.54323, 3.14 etc
#string which are just characters.  Can be used in single, double or triple quotes

#List - first data structure
lst = [1,2,3,4,5,PascalCase, 3.14]
me = 'me'
me in lst
#False
lst.append('me')
me in lst
#True
lst
#[1, 2, 3, 4, 5, 'PascalCase', 3.14, 'camelCase', 'me']
innerList = [PascalCase, camelCase, 'me', booInternet]
lst.append(innerList)
#lst
#[1, 2, 3, 4, 5, 'PascalCase', 3.14, 'camelCase', 'me', ['PascalCase', 'camelCase', 'me', "Brian O'Donnell"]]
'Brian' in lst
#False
booInternet in lst[-1]
#True
innerList = [PascalCase, camelCase, 'me', booInternet]
lst.pop() #removes last item
largeList = lst+innerList
#[1, 2, 3, 4, 5, 'PascalCase', 3.14, 'camelCase', 'me', 'PascalCase', 'camelCase', 'me', "Brian O'Donnell"]
len(lst)
#inserts before index 8
lst.insert(8, 'another value')
numberList = [45,232,75,234,6,354,34634,3,2342]
listCopy = numberList
numberList.sort()
numberList
#[3, 6, 45, 75, 232, 234, 354, 2342, 34634]
numberList.sort(reverse=True)  
numberList
#[34634, 2342, 354, 234, 232, 75, 45, 6, 3]

#Tuples can't add or remove any items after declaration
myTuple = ('this is immutable', 'just like a string', 'hooray')

x = x+1
x+=1
x-=1
x*=1
x/=1

#importing all of the random module
import random
z = random.randint(0,1000)

#m becomes shorthand for math module
import math as m 
m.sqrt(9.0)

#importing just a single method
from random import randrange
randrange(10,1000000,100)