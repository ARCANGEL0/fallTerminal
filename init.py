import fallout as fall
from playsound import playsound
import os

dir = os.path.realpath(os.path.join(
    os.getcwd(), os.path.dirname(__file__)))  # pega o diretorio do arquivo
playsound(os.path.join(dir, "audio/boot.mp3"))

### iniciar
if fall.iniciar():
    senha = fall.login()
    if senha != None:
        print(fall.menu())
    else:
        fall.bloquearTela()
