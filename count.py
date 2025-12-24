def count (n):
    even = 0
    odd = 0
    num1 = []
    num2 = []
    for i in n:
        if i % 2 == 0:
            even += 1
            num1.append(i)
        else:
            odd += 1
            num2.append(i)
    return even, odd, num1, num2
lst = [4, 7, 6, 10,15,11,18,21,22,30,31,34]

even, odd, num1, num2 = count(lst)
print('Even is {}, Odd is {}'.format(even, odd))
for i in num1:
    print(i)