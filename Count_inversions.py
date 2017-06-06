count=0

def inv_count(a,b):
    c=[]
    global count
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            c.append(a[0])
            del a[0]
        else:
            c.append(b[0])
            count+=len(a)
            del b[0]
    if len(a)==0:
        c+=b
    else:
        c+=a
    return c

def divide(x):
    if len(x)==0 or len(x)==1:
        return x
    else:
        m=int(len(x)/2)
        a=divide(x[:m])
        b=divide(x[m:])
    return inv_count(a,b)

n_arr=[]
n=int(input("Enter no of elements:"))
print("Enter the numbers:")
for i in range(n):
    n_arr.append(int(input("Num:")))

s_arr=[]
s_arr=divide(n_arr)

print("Total no of inversions:")
print(count)
