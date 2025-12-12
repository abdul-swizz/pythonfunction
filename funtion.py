def func():
    it = int(input(" You're required to add multiple number, How manny do you want to add: "))
    list1 = []
    for i in range(it):
        hold = int(input ("Enter a number: "))
        list1.append(hold)

    return list1
    #This code section receive multiple data in number from user

lst = func()

def num_reverse():
    lst1 = []
    for n in range(len(lst) - 1, -1, -1):
        lst1.append(lst[n])
    return lst1
    #This code section reverse the user input user

final = num_reverse()
print (final)