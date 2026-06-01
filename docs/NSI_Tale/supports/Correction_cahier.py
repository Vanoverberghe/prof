# Exercice 1

def verifie(l: list) -> bool:
    for i in range(len(l)-1): # Je m'arrete 1 avant la fin pour éviter que le [i+1] pose problème
        if l[i] > l[i+1]: # Si un seul cas ne respecte pas l'ordre c'est faux
            return False
    return True# Si je vais au bout du parcours sans jamais rencontré de cas faux, alors c'est vrai

def verifie2(l: list) -> bool:
    for i in range(1, len(l)): # Je commence à 1 au lieu de 0 pour éviter que le [i-1] pose problème
        if l[i] < l[i-1]: 
            return False
    return True

# Exercice 2

def a_doublon(l: list) -> bool:
    for i in range(len(l)-1):
        if l[i] == l[i+1]:  # Je peux vérifier uniquement les nombres consécutifs dans la liste puisqu'on me dit que la liste est triée dans l'ordre croissant
            return True
    return False # C'est l'inverse de l'exercice 1 en logique
# Si je vais au bout sans rencontrer de cas vrai, alors c'est faux
    
# Exercice 3

def voisinage(n, ligne, colonne):
    voisins = []
    for l in range(max(0,ligne-1), min(n, ligne+2)):
        for c in range(max(0, colonne-1), min(n, colonne+2)):
            if (l,c) != (ligne, colonne):
                voisins.append((l,c))
    return voisins

def incremente_voisins(grille, ligne, colonne):
    pass

# Exercice 4

def moyenne(l):
    s = 0
    c = 0
    for note, coeff in l:
        s += note*coeff
        c += coeff
    return s/c if c != 0 else None

# Exercice 5

from random import randint
## import random

def lancer(n: int) -> list:
    res = []
    for _ in range(n):
        res.append(randint(1,6))
        ##res.append(random.randint(1,6))
    return res

def lancer_comprehension(n: int) -> list:
    return [randint(1,6) for _ in range(n)]

# Exercice 6

def recherche(tab: list, n: int) -> int:
    res = len(tab)
    for i in range(len(tab)):
        if tab[i] == n:
            res = i
    return res # Je return après la boucle pour bien avoir la dernière occurence

# Exercice 7

def fusion_recursive(tab1: list, tab2: list) -> list:
    if tab1 == []:
        return tab2
    if tab2 == []:
        return tab1
    if tab1[0] > tab2[0]:
        return [tab2[0]] + fusion_recursive(tab1, tab2[1:])
    return [tab1[0]] + fusion_recursive(tab1[1:], tab2)

def fusion_iterative(tab1: list, tab2: list) -> list:
    res = []
    while tab1 != [] or tab2 != []:
        if tab1[0] > tab2[0]:
            res.append(tab2[0])
            tab2.pop(0)
        else:
            res.append(tab1[0])
            tab1.pop(0)
    if tab1 == []:
        return res + tab2
    else:
        return res + tab1
    
# Exercice 8

def max_dico(dico: dict) -> tuple:
    res = ()
    maxi = 0
    for k,v in dico.items():
        if v > maxi:
            maxi = v
            res = (k,v)
    return res

# Exercice 9

def multiplication(n1: int, n2: int) -> int:
    res = 0
    for i in range(abs(n1)): # abs est la valeur absolue
        res += n2
    if n1<0:
        return -res
    else:
        return res

# Exercice 10

def convertir(tab: list) -> int:
    num = ""
    for bit in tab:
        num += str(bit)
    return int(num, 2) #int(a, 2) transforme la chaine de caractère a en nombre si elle est écrite en binaire

def convertir_parcours(tab: list) -> int:
    res = 0
    tab = tab[::-1] #Retourne l'ordre de la liste
    for i in range(len(tab)):
        res += tab[i] * 2 ** i
    return res

# Exercice 11

def tri_insertion(tab: list) -> None:
    n = len(tab)
    for i in range(1,n):
        valeur_insertion = tab[i]
        j = i
        while j > 0 and valeur_insertion < tab[j-1]:
            tab[j] = tab[j-1]
            j = j-1
        tab[j] = valeur_insertion

# Exercice 12

def empaqueter(liste_masses, c):
    n = len(liste_masses)
    nb_boites = 0
    boites = [0]*n
    for masse in liste_masses:
        i = 0
        while i<= nb_boites and boites[i] + masse > c:
            i = i+1
        if i == nb_boites + 1:
            nb_boites = i
        boites[i] = boites[i] + masse
    return nb_boites + 1

# Exercice 13

pieces = [1,2,5,10,20,50,100,200]

def rendu_monnaie(somme_due, somme_versee):
    rendu = []
    a_rendre = somme_due - somme_versee
    i = len(pieces) - 1
    while a_rendre > 0:
        if pieces[i] <= a_rendre:
            rendu.append(pieces[i])
            a_rendre = a_rendre - pieces[i]
        else:
            i = i-1
    return rendu