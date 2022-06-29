
import random
print('wellcome to try to win')

def again(win, lose):
    # win = str(win)
    # lose = str(lose)
    print(""" 
    la partida terminó
    el resultado fué:
     ganaste """, win," veces y perdiste ", lose," veces.")
    print('deseas intentarlo de nuevo?')
    intentos = str(input("yes? or not?"))
    
    if "yes" == intentos:
        win = 0
        lose = 0
        intento = True
        return win, lose
        
        
    elif "not" == intentos:
        intento = False
        print('vuelva pronto ') 
        exit()
    elif "not" != intentos:
        print('el valor no es correcto saliendo')
            
 

    print('vuelva pronto ') 


    
   

    
def run():
   
    win = 0
    lose= 0
    intento = True

    while(intento):
        valor = random.randint(1,3)
        user = int(input("""
        seleccion 
         1 ==> rock
         2==> papaer
         3 ==> cissors
        """))
        if win < 3 and lose < 3:     
            if user == 1 and valor == 1:
                print('piedra... empate')
                
            elif user == 1 and valor == 2:
                print('papel... perdiste')
                lose = lose +1
            elif user == 1 and valor == 3:
                print('seleccionaste piedtra, vs tijera...tú ganaste')
            
                win = win +1

            if user == 2 and valor == 1:
                print('seleccionaste papale, vs piedra... tú ganaste')
                win = win +1
            elif user == 2 and valor == 2:
                print('papel... empate')
            elif user == 2 and valor == 3:
                print('tijera... perdite')
                lose = lose +1

            if user == 3 and valor == 1:
                print('piedra... perdiste')
                lose = lose +1
            elif user == 3 and valor == 2:
                print('seleccionaste tijera vs papel... ganaste')
                win = win +1
            elif user == 3 and valor == 3:
                print('tijera... empate')
            
            
            

        if win == 3 or lose == 3:            
            again(win, lose )
           
           
      

if __name__ =='__main__':
    run()
