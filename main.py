import os
import random
import time

# n = random.randint(0,9)
# s =+ str(n)

nb_lettre = 4 
NB_MAX = 9
NB_SECONDE = 3 
score = 0 

def wait_and_clear() :
    wait_seconde()
    clear_screen() 


def wait_seconde():
    time.sleep(NB_SECONDE )

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def nombre_alearetoire(nb_lettre ,nombre): 
    
    for i in range(nb_lettre) :
        nombre_int = random.randint(0,NB_MAX)
        nombre += str(nombre_int)
    return nombre


nombre = nombre_alearetoire(nb_lettre , "")

while True : 
    print("Retenez la séquence ")
    print(nombre)
    wait_and_clear()
    reponse = input("Votre réponse : ")
    if reponse ==nombre : 
        print("Bonne réponse")
        score+=1
        print(f"Votre score :  {score}")
        nombres= nombre_alearetoire(1 , nombre)
        nombre = nombres
        clear_screen()

    else :
        print(f"Mauvais réponse, la séquence était : {nombre}")
        print(f"Votre score :  {score}")
        break  
      


