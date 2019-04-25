def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a
#The line a, b = b, a % b actually stores the value of b in a and
#the value of a % b in b Return the value of a.
a = [4, 10, 16, 14]

result = a[0]
for i in a[1:]:
    result = gcd(result, i)

print(result)
