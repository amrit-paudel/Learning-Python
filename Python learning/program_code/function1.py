import string

from functools import reduce

temp = string.ascii_uppercase

# see some string methods in the presentation
name = "amrit paudel"
# print( name.find('a') ) # returns the index of the 'a' in the string

# print( 'amritPOUDEL'.swapcase() ) # swaps the upper case to lower case and vice versa

def temp():
    global temp
    temp = 100  # we can define global variable using global keyword anywhere
    print(  "Temp function")
# temp()

# memo = { 0:0, 1:1 }
# def fibonachi(n):
#     if n in memo:
#         return memo[n]
#     else:
#         memo[n] = fibonachi(n-1) + fibonachi(n-2)
#         return memo[n]

# print( fibonachi(6) )

# 1: store base case in memo initially
# 2: inside the function if the value present in the memo
# 2: store all other case in nth index in memo
memo={ 0:0, 1:1 }
def fib(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib(n-1) + fib(n-2)
        return memo[n]
# print( fib(10) )


# factorial using recursive and memoization
fmemo = {0:1, 1:1} # since o! = 1 and also 1! = 1
def fact(n):
    if n in fmemo:
        return fmemo[n]
    else:
        # return n * fact(n-1)
        fmemo[n] = n*fact(n-1)
        return fmemo[n]
# print(fact(10))
# print(fmemo)

# x^nth using recursive function
pmemo = { 0:1 } # lets also try using memoization
def xnth( x,n ):
    # if n == 0:
    #     return 1
    # elif n == 1:
    #     return x
    if n in pmemo:
        return pmemo[n]
    else:
        # return x * xnth(x,n-1)
        pmemo[n] = x * xnth(x,n-1)
        return pmemo[n]
    
# print( xnth(2,10) )
# print( pmemo )

# there are various built in functions in python, see presentation

# abs() returns absolute value
# print( abs(-100) )

# min() returns minimum value
# print( min(10,20,30,40,50) )

# max() returns maximum value
# print( max( 10,20,30,40,100 ) )

# sorted() # sorts the string, list
# name = 'amrit'
# print( sorted(name) )

# temp_list = [10,20,2,1,90]
# print( sorted(temp_list) )

# chr(num) # returns the character of unicode num
# print( chr(97) ) # a

# ord('A') # returns the unicode of the character
# print( ord('A') ) # 65

# lambda function, .map() .filter() and .reduce()
# tlist = [1,2,3,4,5]

# sqlist = map( lambda item : item**2, tlist )
# print( list(sqlist) )

# evenlist = filter( lambda item : item%2 == 0, tlist )
# print( list( evenlist ) )

# sumofitems = reduce( lambda item1, item2 : item1+item2 , tlist )
# print( sumofitems )

# add = lambda item1,item2 : item1+item2
# print( add(1,1) )

# lambda function calling immediately
# print( f" Product is {(lambda item1,item2 : item1*item2) ( 10,10 )} " )

# list comprehension
lc_list = [1,2,3,4,5,6,7,8,9]
# lc_even_list = [ item for item in lc_list if item % 2 == 0 ]
# print( lc_even_list )

# doing the same using lambda function
# lc_even_list1 = list(  filter( lambda item : item%2 == 0, lc_list )  )
# print( lc_even_list1 )

# mostly only these two ways of looping in pthon are used
# for item in lc_list:
#     print(item)

# for i in range( 0,len(lc_list) ):
#     print( f" i = {i} item = {lc_list[i]} " )


















