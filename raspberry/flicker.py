a=[1,2,3,4,5]
p = []
def swap(a,b):
    temp =a
    a=b
    b=temp
for i in a:
    if a[i]>a[i+1]:
        pass
    else:
        swap(a[i],a[i+1])


