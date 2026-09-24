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
    voisins = voisinage(len(grille), ligne, colonne)
    for l, c in voisins:
        if grille[l][c] != -1:
            grille[l][c] += 1
            
def genere_grille(bombes):
    n = len(bombes)
    
    grille = [[0 for colonne in range(n)] for ligne in range(n)]
    
    for ligne, colonne in bombes:
        grille[ligne][colonne] = -1
        incremente_voisins(grille, ligne, colonne)
    
    return grille

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

# Exercice 14

def recherche2(a: int, tab: list) -> int:
    res = 0
    for e in tab:
        if e == a:
            res+=1
    return res

# Exercice 15

def mini(releve: list, date: list) -> tuple:
    temp_min = float('inf') # L'infini en python
    annee = 0
    for i in range(len(releve)):
        if temp_min > releve[i]:
            temp_min = releve[i] # recherche de la température minimale
            annee = date[i]
    return temp_min, annee

# Exercice 16

def inverse_chaine(chaine: str) -> str:
    result = ''
    for caractere in chaine:
        result = caractere + result # on ajoute à l'envers
    return result

def est_palindrome(chaine: str) -> bool:
    inverse = inverse_chaine(chaine)
    return inverse == chaine

def est_nbre_palindrome(nbre: int) -> bool:
    chaine = str(nbre)
    return est_palindrome(chaine)

# Exercice 17

def recherche_indices_classement(elt: int, tab: list) -> (list,list,list):
    inferieurs = []
    egaux = []
    superieurs = []
    for i in range(len(tab)):
        if tab[i] < elt:
            inferieurs.append(i)
        elif tab[i] == elt:
            egaux.append(i)
        else:
            superieurs.append(i)
    return inferieurs, egaux, superieurs

# Exercice 18

def moyenne(nom: str, dico_result: dict) -> float:
    if nom in dico_result:
        notes = dico_result[nom]
        total_points = 0
        total_coefficients = 0
        for valeurs in notes.values():
            note, coefficient = valeurs
            total_points = total_points + note * coefficient
            total_coefficients = total_coefficients + coefficient
        return round(total_points / total_coefficients, 1)
    else:
        return -1
    
# Exercice 19

def max_et_indice(tab: list) -> (int, int):
    maxi = -float('inf')
    ind = 0
    for i in range(len(tab)):
        if maxi < tab[i]:
            maxi = tab[i]
            ind = i
    return maxi, ind

# Exercice 20

def recherche3(tab: list, n: int) -> int:
    debut = 0 #premier indice
    fin = len(tab)-1 #dernier indice
    while debut <= fin:
        milieu = (debut+fin) // 2 # indice du milieu
        if n == tab[milieu]:
            return milieu
        elif n > tab[milieu]:
            debut = milieu + 1
        else:
            fin = milieu - 1
    return -1
    
# Exercice 21

def ajoute_dictionnaires(d1: dict, d2: dict) -> dict:
    d = {}
    for k,v in d1.items():
        d[k] = v # On ajoute tout les couples clés valeurs de d1
    for k,v in d2.items():
        if k in d: #Si la clé a deja été ajoutée, (présente dans d1)
            d[k] += v
        else:
            d[k] = v
    return d

# Exercice 22

def nbre_coups():
    n = 0
    cases_vues = [0]
    case_en_cours = 0
    nbre_cases = 12
    while len(cases_vues) < nbre_cases:
        x = randint(1,6)
        case_en_cours = (case_en_cours + x) % 12
        if not case_en_cours in cases_vues:
            cases_vues.append(case_en_cours)
        n = n + 1
    return n

# Exercice 23

def delta(liste: list) -> list:
    res = [liste[0]]# On met le premier élément puisqu'on ne va pas le prendre dans le parcours
    for i in range(1, len(liste)): #On commence à un pour éviter que liste[i-1] pose problème
        res.append(liste[i] - liste[i-1])
    return res
    
# Exercice 24

def selection_enclos(table_animaux: list, num_enclos: int) -> list:
    res = []
    for dico in table_animaux:
        if dico['enclos'] == num_enclos:
            res.append(dico)
    return res

# Exercice 25

def enumere(L: list) -> dict:
    d = {}
    for i in range(len(L)):
        if L[i] not in d: # Si je n'ai pas encore croisé l'élément
            d[L[i]] = [i] # J'ajoute une nouvelle clé avec l'indice dans une liste en valeur
        else: # Si je l'ai deja croisé
            d[L[i]].append(i) # J'ajoute l'indice dans la liste deja existante
    return d

# Exercice 26

def dichotomie(tab: list, x: int) -> bool:
    debut = 0
    fin = len(tab) - 1
    while debut <= fin:
        m = (debut + fin) //2
        if x == tab[m]:
            return True
        if x > tab[m]:
            debut = m + 1
        else:
            fin = m - 1
    return False

# Exercice 27

def binaire(a: int) -> str:
    bin_a = str(a%2)
    a = a//2
    while a > 0:
        bin_a = str(a%2) + bin_a
        a = a//2
    return bin_a

# Exercice 28

def tri_selection(tab: list) -> None:
    N = len(tab)
    for k in range(N):
        imin = k
        for i in range(k, N):
            if tab[i] < tab[imin]:
                imin = i
        tab[k], tab[imin] = tab[imin], tab[k]
        
# Exercice 29

def ecriture_binaire(n: int) -> list: # Meme que l'exercice 27 mais avec une liste
    res = [n%2]
    n = n//2
    while n > 0:
        res.append(n%2)
        n = n//2
    return res

# Exercice 30

def rangement_valeurs(notes_eval: list) -> list:
    res = [0 for _ in range(11)] # initialisation de la liste avec 0 notes
    for e in notes_eval:
        res[e] += 1
    return res

def notes_triees(eff: list) -> list:
    res = []
    for i in range(len(eff)):
        for j in range(eff[i]):
            res.append(i)
    return res