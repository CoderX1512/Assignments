# Python program to illustrate the intersection
# of two lists in most simple way
# Logic -1
def intersection(lst1, lst2):
	lst3 = [value for value in lst1 if value in lst2]
	return lst3

# Logic-2
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Logic-3
def Intersection(lst1, lst2):
    return set(lst1).intersection(lst2)


# Driver Code
lst1 = [4, 9, 1, 17, 11, 26, 28, 54, 69]
lst2 = [9, 9, 74, 21, 45, 11, 63, 28, 26]
print(intersection(lst1, lst2))

