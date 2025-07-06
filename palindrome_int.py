a = int(input("enter ur number   "))

copy = a

rev = 0

while a > 0:
    rev = rev * 10 + a % 10
    a = a // 10

if copy == rev:
    print("palindrome")
else:
    print("not palindrome")
    