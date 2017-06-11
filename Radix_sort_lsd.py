d = 0
def radix_s(L, exp):
    exp_t = exp
    t_d = 0
    global d

    while exp_t != 0:
        t_d+=1
        exp_t/=10

    if t_d > d:
        return L

    buckets_f = []
    buckets = []

    for i in range(10):
        buckets.append([])

    for i in L:
        inc = int(i/exp)
        buckets[(i/exp)%10].append(i)

    bucket_t = []
    for i in buckets:
        for j in i:
            bucket_t.append(j)

    temp_L = radix_s(bucket_t, exp*10)

    return temp_L

L = [301628, 772137, 942485, 6088150, 566, 86199, 2611, 590, 99, 1, 0]
max_no = max(L)
d = 0

while max_no != 0:
    d+=1
    max_no/=10
print("Array in sorted form: ")
print(radix_s(L, 1))
