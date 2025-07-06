l = [12,23,1,3,5,53,32,2,3,4,5,5,56,222,23,4,65]

largest= l[0]
selarge= l[0]

for i in l:
    if i > largest:
        selarge = largest
        largest = i
    elif i > selarge:
        selarge = i

print(f"the second largest{selarge} and  greatest is {largest}")