import time; import audioplayer

n =  int(input("Hola: "))
for x in range(n):
    print(f"¡¡QUEDAN {n} SEGUNDOS!!"); n -= 1; time.sleep(1)
audioplayer.AudioPlayer("C:/Users/campo/OneDrive/Escritorio/python/imagenes/y2mate.com - PUM sonido meme.mp3").play(block=True) # CAMBIAR BACKSLASH POR SLASH NORMALES