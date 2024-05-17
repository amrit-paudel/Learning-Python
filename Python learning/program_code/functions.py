
# apparently function can return more than one value
# like return both circumference and area of circle
def get_roots(a,b,c):
    r1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
    r2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
    return r1,r2
r1,r2 = get_roots(1,-5,6)
print(r1,r2)

t1,t2 = get_roots( b=-5, c=6, a=1 )
print(t1,t2)

# 1 mile as 1.61 km
def mile_to_km(mv=0):
    kmv = mv * 1.61
    if mv!=0:
        print( f"{kmv} km" )
        
    for i in range( 1,6,1 ):
        print( f"{i} mile  = {i*1.61} km" )
    return
mile_to_km()

#remember this feature
import string
print( string.ascii_uppercase )
print( string.ascii_lowercase )

src_str = string.ascii_uppercase
print( src_str[1:] + src_str[:1] ) # we just moved on letter forward in the alphabetical order


# recurion 
# tower of hanoi
def TOH( num, start, middle , end ):
    if num == 1:
        print( f"Moving disk {1} from {start} to {end}" )
        return
    TOH( num-1, start, end, middle )
    print( f"Moving disc {num} from {start} to {end} " )
    TOH( num-1, middle, start,end )

TOH( 3,"A","B","C" )



# print the n fibonachi series
def fibonachi(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonachi(n-1) + fibonachi(n-2)
print( fibonachi(6) )

# memoization
# a dictionary, where the base case is already stored in it

memo = { 0:0, 1:1 }
def fibonachi(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = fibonachi(n-1) + fibonachi(n-2)
        return memo[n]

print( fibonachi(6) )

# map()
nums = [1,2,3,4,5]
numssq = map( lambda item : item ** 2 , nums )
print(list(numssq))

# filter()
even_nums = filter( lambda item : item%2 == 0 , nums )
print( list(even_nums) )

# reduce()
from functools import reduce
sum = reduce( lambda item1,item2: item1+item2 , nums )
print(sum)

#list comprehension
list1 = [1,2,3,4,5]

list3 = [ x for x in list1 if x % 2 == 0 ]
print(list3)
