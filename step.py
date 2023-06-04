

n = int(input("n = "))
prime = True
f = 2

while (f*f <= n):

    if n % f == 0:
        prime = False

    f += 1

print(prime)

"""
x = 0
y = 0

a = 0
b = 0
c = 0


while (a < 5):

    c += 1
    if a == b:
        b = 0
        a += 1
    
    if c % 2 == 0:
        b += 1

    print(a, b)


x = 0

step = 0
counter = 0
turn = 0

while(step <= 10):

    if counter % 2 == 0:
        step += 1
        
    print(step)
    counter += 1
"""























