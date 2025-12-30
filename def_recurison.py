import sys
sys.setrecursionlimit(100000) #Recursion automatically give a 1000 output, But it can also be adjusted

i = 1
#This is simple code on how recursion works
def greet():
    global i
    i += 1
    print('hello world', i)
    #here is when the function call itself inside a function
    greet()

greet()

def fac(n):
    while n == 0:
        return 1
    return n * fac(n-1)
print (fac(5))

factor = 5
result = 1
while factor > 0:
    result = result * factor
    factor = factor - 1

print (result)

