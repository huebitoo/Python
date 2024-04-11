while True:
    uwu=""
    x=60
    for i in range(x):
        z=i+30
        word=f"\033[{z}m hola carilta\033[0m"
        if i<x/2:
            uwu=word+uwu
        else:
            uwu=uwu[len(word):]
        print(uwu)