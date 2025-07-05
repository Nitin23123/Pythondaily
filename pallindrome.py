a = "BOOB"

b = ""

for i in range(len(a)-1,-1,-1):
    b = b + a[i]
    
if b == a:
    print("The string is a palindrome")
else:
    print("its not a pallindrome")