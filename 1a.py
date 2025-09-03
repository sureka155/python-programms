a=[(1,2,3),(4,5,6)]
b=[]
for i in a:
    sum=0
    for j in i:
        sum+=j
    b.append(sum)
print(b)    
