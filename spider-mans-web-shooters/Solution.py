import math

n = int(input())
x = list(map(int, input().split()))

MAX = 3*(10**5) + 5
# MAX = 8

def fft(a, inv):
    n = len(a)

    if(n==1):
        return
    
    a0 = [0]*(n//2)
    a1 = [0]*(n//2)

    for i in range(n//2):
        a0[i] = a[2*i]
        a1[i] = a[2*i+1]
    
    fft(a0, inv)
    fft(a1, inv)

    ang = 2 * math.pi / n * (-1 if inv else 1)

    w = 1
    wn = complex(math.cos(ang), math.sin(ang))

    for i in range(n//2):
        a[i] = a0[i] + w*a1[i]
        a[i+n//2] = a0[i] - w*a1[i]
        if (inv):
            a[i] /= 2
            a[i+n//2] /= 2
        w = w*wn
    return 


def resize(a):
    n = 1
    while(n < len(a)):
        n <<= 1
    # n <<= 1

    temp = [0]*n
    for i in range(len(a)):
        temp[i] = a[i]
    return temp


max_val = max(x)
min_val = min(x)

a = [0] * MAX
b = [0] * MAX

for i in x:
    a[i - min_val] = 1
    b[max_val - i] = 1

a = resize(a)
b = resize(b)

n = len(a)

fft(a, False)
fft(b, False)

for i in range(n):
    a[i] *= b[i]

fft(a, True)

c = [int(val.real+0.1) for val in a]

count = 0

for i in range(max_val-min_val+1, len(c)):
    if c[i] > 0:
        count += 1

print(count)