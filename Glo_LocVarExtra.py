#This code isn't person take but showing how the Global and Local variable works
glo = 'This is global variable'
glo1 = 5
glo2 = 6
local = 'This is Global variable'
local1 = 5
local2 = 6

def localvar ():
    clas = globals() ['local']
    local = ' This is local variable'
    # noinspection PyShadowingNames
    glo = 'This is Local variable assign to GLO name'
    new = globals() ['glo']
    local1 = 3
    return clas, glo, glo1, local, local1, new


for i in range(1):
    new = localvar()
    for j in new:
        print (j)

