  
import fallout as fall


### iniciar 

if fall.iniciar():
  senha = fall.login()
  if senha != None:
        print(fall.menu())
  else:
        fall.bloquearTela()


