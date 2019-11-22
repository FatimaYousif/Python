#task5

a=[10,10,20,20,30]
a.sort()
for i in range(len(a)-1):
    if a[i]==a[i+1]:
        print(a[i])