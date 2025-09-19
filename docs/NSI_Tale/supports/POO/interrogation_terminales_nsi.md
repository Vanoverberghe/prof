#  Interrogation de Python – POO et Récursivité 

## Exercice 1 – Classe simple (5 points)

On veut représenter un **cercle** en POO.

1. Crée une classe `Cercle` avec un attribut `rayon`.
2. Ajoute une méthode `perimetre()` qui retourne le périmètre du cercle.
3. Ajoute une méthode `aire()` qui retourne l’aire du cercle.
4. Instancie un objet `c1` de rayon 5 et affiche son périmètre et son aire.

(*Rappel : périmètre = 2 × π × r ; aire = π × r²\
 On peut utiliser `pi` avec `from math import pi`*)

---

## Exercice 2 – Récursivité

1. Écris une fonction récursive `factorielle(n)` qui calcule la factorielle de `n`.
   (*Rappel : n! = n × (n-1) × … × 1, et 0! = 1*)

2. Écris une fonction récursive `somme_liste(liste)` qui calcule la somme des éléments d’une liste.
   Exemple : `somme_liste([2, 4, 6])` doit renvoyer `12`.

3. Écris une fonction récursive `fibonacci(n)` qui calcule le n-ième terme de la suite de Fibonacci.
   (*Rappel : F(0) = 0, F(1) = 1 et F(n) = F(n-1) + F(n-2) pour n ≥ 2*)

---

## Exercice 3 – POO + récursivité

On veut modéliser un **dossier contenant des fichiers et d’autres dossiers**.

Complète le code à trous ci-dessous :

```python
class Noeud:
    def __init__(self, nom):
        self.nom = nom

class Fichier(Noeud):
    pass

class Dossier(Noeud):
    def __init__(self, nom):
        super().__init__(nom)
        self.elements = []

    def ajouter(self, element):
        # Ajouter un fichier ou un sous-dossier
        ______________________

def afficher_dossier(dossier, niveau=0):
    print("  " * niveau + "Dossier " + dossier.nom)
    for element in dossier.elements:
        if isinstance(element, Fichier):
            print("  " * (niveau + 1) + "Fichier " + ________________)
        else:
            _______________________________
```

Exemple attendu :

```
Dossier racine
  Fichier notes.txt
  Dossier images
    Fichier photo1.png
    Fichier photo2.png
```