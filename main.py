import os
import random
import time

# n = random.randint(0,9)
# s =+ str(n)
NB_MAX = 9
NB_SECONDE = 3 
longueur_sequence = 4 
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

def sequence_alearetoire(longueur_sequence ,sequence): 
    
    for i in range(longueur_sequence) :
        nombre_int = random.randint(0,NB_MAX)
        sequence += str(nombre_int)
    return sequence


sequence = sequence_alearetoire(longueur_sequence , "")

while True : 
    print("Retenez la séquence ")
    print(sequence)
    wait_and_clear()
    reponse = input("Votre réponse : ")
    if reponse ==sequence : 
        print("Bonne réponse")
        score+=1
        print(f"Votre score :  {score}")
        sequences= sequence_alearetoire(1 , sequence)
        sequence = sequences
        clear_screen()

    else :
        print(f"Mauvais réponse, la séquence était : {sequences}")
        print(f"Votre score final  :  {score}")
        break  
      


