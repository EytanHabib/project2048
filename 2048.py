import random


def creation_grille(longueur_grille):
    grille = []
    for i in range(longueur_grille):
        lignegrille = []
        for j in range(longueur_grille):
            lignegrille.append("|")
            lignegrille.append("   ")  
        lignegrille.append("|")  
        grille.append(lignegrille)
    return grille


def placementtuile(grille, longeurligne):
    empty_tiles = []
    for i in range(len(grille)):
        for j in range(1, longeurligne * 2, 2):
            if grille[i][j] == "   ":
                empty_tiles.append((i, j))
    if empty_tiles:
        x, y = random.choice(empty_tiles)
        grille[x][y] = f" {random.choice([2, 4])} "


def affichezgrille(grille):
    afichegrille = ""
    for ligne in grille:
        afichegrille += "-" * (len(grille[0]) * 2) + "\n"  
        afichegrille += "".join(ligne) + "\n"  
    afichegrille += "-" * (len(grille[0]) * 2)  
    print(afichegrille)


def joueur_grille():
    while True:
        try:
            longeurgrille = int(input("Quelle taille de la grille voulez-vous? (minimum 3): "))
            if longeurgrille >= 3:
                return longeurgrille
            else:
                print("Veuillez entrer une taille de grille d'au moins 3.")
        except ValueError:
            print("Entrée invalide. Veuillez entrer un nombre.")


def choixdirection():
    bonnedirection = {"gauche", "droite", "haut", "bas"}
    while True:
        choixdirection = input("Quelle direction (gauche, droite, haut, bas) : ")
        if choixdirection in bonnedirection:
            return choixdirection
        else:
            print("Choix invalide, veuillez réessayer.")


def deplacementtuile(grille, direction):
    
    def combine_and_shift(line):
       
        new_line = [x for x in line if x != "   "]

        
        for i in range(len(new_line) - 1):
            if new_line[i] == new_line[i + 1]:
                new_line[i] = f" {int(new_line[i]) * 2} "  
                new_line[i + 1] = "   "  

       
        new_line = [x for x in new_line if x != "   "]

        
        while len(new_line) < len(line):
            new_line.append("   ")

        return new_line

    if direction in ("gauche", "droite"):
        for i in range(len(grille)):
            line = [grille[i][j] for j in range(1, len(grille[i]), 2)]  
            if direction == "droite":
                line.reverse()  
            new_line = combine_and_shift(line)
            if direction == "droite":
                new_line.reverse()  
            for j in range(len(new_line)):
                grille[i][1 + 2 * j] = new_line[j] 

    elif direction in ("haut", "bas"):
        for j in range(1, len(grille[0]), 2):
            line = [grille[i][j] for i in range(len(grille))]  
            if direction == "bas":
                line.reverse()  
            new_line = combine_and_shift(line)
            if direction == "bas":
                new_line.reverse()  
            for i in range(len(new_line)):
                grille[i][j] = new_line[i]  


def jeu_2048():
    longueur_grille = joueur_grille()
    grille = creation_grille(longueur_grille)
    placementtuile(grille, longueur_grille)
    placementtuile(grille, longueur_grille)
    affichezgrille(grille)

    while True:
        for ligne in grille:
            if 2048 in ligne :  
                    print("Félicitations ! Vous avez gagné en créant une tuile 2048 !")
                    return
            
            
        direction = choixdirection()
        deplacementtuile(grille, direction)
        placementtuile(grille, longueur_grille)  
        affichezgrille(grille)

       
        if not any_move_possible(grille):
            print("Game Over! Plus aucun déplacement possible.")
            break


def any_move_possible(grille):
    
    for i in range(len(grille)):
        for j in range(1, len(grille[i]), 2):
            if grille[i][j] == "   ":
                return True  
            if j + 2 < len(grille[i]) and grille[i][j] == grille[i][j + 2]:
                return True 
            if i + 1 < len(grille) and grille[i][j] == grille[i + 1][j]:
                return True 
    return False



jeu_2048()













































