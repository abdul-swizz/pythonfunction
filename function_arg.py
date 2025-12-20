def add (a, *b): # Variable length argument accepting multiple data and change the
    print(a)
    print (b)
    for i in b:
        a = a + i
        print ('this is i', i)
    print(a)

#add(3,6,8,6,7) #Remove  first hash in front of add for the funtion to work




def whale ():
    def update(num):
        num[1] = 9
        return num

    lst = [5, 10, 15, 20, 25]
    value = update(lst)
    value_attach = []
    for i in range(len(value)):
        value_attach.append(value[i] - 2)
    print (value_attach)
#whale() #Remove  first hash in front of whale for the funtion to work

age = int(input('Enter your age: '))
city = input('Enter your city: ').capitalize()
def person(name = 'alias', **data):
    print ('name', name)
    for i,j in data.items():
        print (i,j)

person('sadiq', age= age , city = city, gender =  'male')