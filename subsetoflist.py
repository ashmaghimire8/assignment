a = [1,4,34,56,3,2,4]
a.sort() #descending order in same list
a = sorted(key= len,reverse=True) #returns new list
b = [34,4]

check = True
for i in b:
    if i not in a:
        check = False
        break        

if check:
    print("b is subset of a")
else:
    print("b is not subset of a")

a = set([1,4,34,56,3,2,4])
b = set([34,5])
print(b.issubset(a))

newSet = a.union(b)
print(newSet)