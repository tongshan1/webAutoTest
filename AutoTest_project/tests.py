from django.test import TestCase

# Create your tests here.


b = [1,2,3,]
d = []

for i in range(len(b)):

    c = (i+1, b[i])

    # print(c)

    d.append(c)

    # c[i] = b[i]


print(tuple(d))
