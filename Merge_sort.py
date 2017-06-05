
def merge(a,b):
    c=[]
    while len(a)!=0 and len(b)!=0:
        if a[0]<b[0]:
            c.append(a[0])
            del a[0]
        else:
            c.append(b[0])
            del b[0]
    if len(a)==0:
        c+=b
    else:
        c+=a
    return c

def mergesort(x):
    if len(x)==0 or len(x)==1:
        return x
    else:
        m=int(len(x)/2)
        a=mergesort(x[:m])
        b=mergesort(x[m:])        
	return merge(a,b)

n_arr=[]
n=int(input("Enter no of elements:"))
print("Enter the numbers:")
for i in range(n):
    n_arr.append(int(input("Num:")))

s_arr=[]
s_arr=mergesort(n_arr)

print("Your array in sorted form:")
print(s_arr)
