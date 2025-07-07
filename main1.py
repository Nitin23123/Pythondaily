# a = {10:100,20:200,30:300,40:400}


# # or a[50] = 500
# # or a.update({50:500})

# del a[30] #for deleting

# print(a)

# for i in a:
#     print(i,":")
#     print(a[i])
    
d1 = {10:100,20:200,30:300}
d2 = {40:400,50:500,60:600}

for i in d2:
    d1[i]= d2[i]
    
print(d1)
