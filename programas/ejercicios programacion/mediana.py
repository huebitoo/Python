num1 = [1, 2]
num2 = [3, 4]

final = num1 + num2
x = len(final)
final.sort()


if x%2 == 0:
    x = x/2
    x = int(x)
    a = final[(x-1)]
    b = final[(x)]
    media = (a + b)/2
    print(media)
else:
    x /= 2
    x = int(x)
    media = final[x]
    print(media)

