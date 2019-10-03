#Syntax
#lambda arguments : expression
#The expression is executed and the result is returned:

#Example
#A lambda function that adds 10 to the number passed in as an argument, and print the result:

x = lambda a : a + 10
print(x(5))
#Lambda functions can take any number of arguments:

#Example
#A lambda function that multiplies argument a with argument b and print the result:

x = lambda a, b : a * b
print(x(5, 6))
#Example
#A lambda function that sums argument a, b, and c and print the result:

x = lambda a, b, c : a + b + c
print(x(5, 6, 2))

x = lambda z : z.find("Yee")>0

name = "Benson Yee"
print( x(name) )


brotherlist = ["benson yee","cleon yee","jon matsukawa","andy matsukawa"]
# lambda functions usually used in filters as anonymous single use functions
x = filter( lambda x: x.find("matsukawa")>0, brotherlist)

# filter returns filter object that can be made into a list
print( list(x) )

# example lambda to filter out vowels from string
samplestring ='abcdefghijklmnopqrstuvwxyz'
x = filter( lambda x: x not in ['a','e','i','o','u'], samplestring)

print ( list(x))

