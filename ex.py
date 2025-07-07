
def cout(c):
    a = [1,1,1,1,12,2,2,2,2,2,3,3,3,3,4,4,4,5,55,5,66,6,6,6,6,6,6,6]

    count = 0
    for i in a:
        if i == c:
            count += 1
    print(count)
    
cout(1)
cout(6)