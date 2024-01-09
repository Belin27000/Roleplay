import random
import sys

WANNA_PLAY="Souhaitez-vous attaquer (1) ou utiliser une potion (2) ? "
POTION = 3
POTION_LIFE =random.randint(15,50)
PLAYER_ATTAQUE = random.randint(5,10)
ENNEMY_ATTAQUE = random.randint(5,15)
PLAYER_LIFE=50
print(PLAYER_LIFE)
ENNEMY_LIFE=PLAYER_LIFE

PLAYER_LIFE<=0 or ENNEMY_LIFE<=0

# Si l'utilisateur choisi la première option (1), vous infligez des points de dégât à l'ennemi.
while not PLAYER_LIFE<=0 or ENNEMY_LIFE<=0 :
    resultat = False
    while not resultat:
        choice=input(WANNA_PLAY)
        resultat = choice.isdigit() and (int(choice) == 1 or int(choice) == 2)

    if int(choice) ==1:
        ENNEMY_LIFE-=PLAYER_ATTAQUE
        PLAYER_LIFE-=ENNEMY_ATTAQUE
        if ENNEMY_LIFE<=0:
            print(f"""
Vous avez infligé {PLAYER_ATTAQUE} points de dégats à l'ennemi ⚔️
Tu as gagné 💪
Fin du jeu
""")
            sys.exit()
        elif PLAYER_LIFE <=0:

         print(f"""
L'ennemi vous a infligé {ENNEMY_ATTAQUE} points de dégats.
Tu as perdu 😔
Fin du jeu
""")
         sys.exit()

        print(
f"""
Vous avez infligé {PLAYER_ATTAQUE} points de dégats à l'ennemi ⚔️
L'ennemi vous a infligé {ENNEMY_ATTAQUE} points de dégats ⚔️
Il vous reste {PLAYER_LIFE} points de vie.
Il reste {ENNEMY_LIFE} points de vie à l'ennemi.
----------------------------------------------------------------
"""
)
    elif int(choice)==2:
        if POTION>0:
            POTION-=1
            PLAYER_LIFE+=POTION_LIFE
            PLAYER_LIFE-=ENNEMY_ATTAQUE
            if PLAYER_LIFE>50:
                PLAYER_LIFE=50
            print(
f"""
Vous récupérez {POTION_LIFE} points de ❤️({POTION} restantes)
L'ennemi vous a infligé {ENNEMY_ATTAQUE} points de dégats ⚔️
Il vous reste {PLAYER_LIFE} points de vie.
Il reste {ENNEMY_LIFE} points de vie à l'ennemi.
----------------------------------------------------------------
"""
)
            PLAYER_LIFE-=ENNEMY_ATTAQUE
            if PLAYER_LIFE<=0:
                PLAYER_LIFE=0
            print(
f"""
Vous passez votre tour...
L'ennemi vous a infligé {ENNEMY_ATTAQUE} points de dégats ⚔️
Il vous reste {PLAYER_LIFE} points de vie.
Il reste {ENNEMY_LIFE} points de vie à l'ennemi.
----------------------------------------------------------------
"""
            )
        elif POTION==0:
            print("Vous n'avez plus de potion...")

sys.exit()