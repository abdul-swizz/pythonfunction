x = 5
f = 1
for i in range (1,6 ):
    f = f*i

print (f)


def is_sorted(lst):
    return lst == sorted(lst)

print(is_sorted([1, 2, 3, 4]))  # Output: True
print(is_sorted([3, 2, 1]))    # Output: False
