l = [12,13,4,3,5,6,4,3,333,4,5,66]

greatest = l[0]

for i in range(len(l)):
    if l[i] > greatest:
        greatest = l[i]
        index = i
    
print(f"{greatest} is the greatest number at index {index+1}")