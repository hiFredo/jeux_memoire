import os
import random
import time

# n = random.randint(0,9)
# s =+ str(n)
NB_MAX = 9
longueur_sequence = 4 
score = 0 
sequence= ""

def wait_seconde(nb_seconde):
    time.sleep(nb_seconde )

def clear_screen():
    if(os.name == 'posix'):
        os.system('clear')
    else:
        os.system('cls')

def sequence_alearetoire(longueur_sequence ,sequence): 
    
    for i in range(longueur_sequence) :
        chiffre = random.randint(0,NB_MAX)
        sequence += str(chiffre)
    return sequence


sequence = sequence_alearetoire(longueur_sequence , sequence)

while True : 
    print("Retenez la séquence ")
    wait_seconde(1)
    print(sequence)
    wait_seconde(3)
    clear_screen()


    sq_utilisateur  = input("Votre réponse : ")
    
    if sq_utilisateur ==sequence :  
        score+=1
        print("Bonne réponse")
        print(f"Votre score :{score}")
        sequence = sequence_alearetoire( 1 , sequence)
        clear_screen()
        
    else :
        break 

print(f"Mauvais réponse, la séquence était : {sequence}")
print(f"Votre score final est : {score}") 
      


