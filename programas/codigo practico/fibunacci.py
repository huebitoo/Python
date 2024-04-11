# def hola(n):
#     a = 0
#     b = 1
#     for x in range(n):
#         yield a
#         a, b = b, a+b

# for t in hola(10):
#     print(t)

a = 1
b = 0
c = 0
x = int(input("a: "))
while x > 0:
    c = a+b
    b = a
    a = c
    print(c)
    x -= 1