# **Interrogation – Python (avec ordinateur) : listes, tuples, dictionnaires ( Pratique )**

**Instructions :** Vous pouvez exécuter et tester votre code. Appelez moi après chaque question/exercice pour que je vérifies.

---

## **Exercice 1 – Informations sur des jeux vidéos**

On veut stocker les informations de plusieurs jeux vidéos dans une liste de dictionnaires.
Chaque dictionnaire contient :

```python
{
    "nom": ... ,
    "date_de_sortie": ... ,
    "genre": ... , 
    "notes": [...]   # une liste de notes obtenues par la critique
}
```

On vous donne :

```python
bibliotheque = [
    {"nom": "Clash Royale",  "date_de_sortie": 2016, "genre": "Mobile", "notes": [14, 12, 15]},
    {"nom": "Clair Obscur", "date_de_sortie": 2025, "genre": "RPG", "notes": [18, 19, 17]},
    {"nom": "League of Legends",  "date_de_sortie": 2009, "genre": "Moba", "notes": [10, 19, 14]}
]
```

1. Grace à la notation avec les crochets, afficher la **première note** du jeu `"Clair Obscur"`.
2. Ajouter la note `16` à la liste de notes de `"League of Legends"`.
3. Créer une fonction `moyenne(notes)` qui retourne la moyenne d’une liste de notes ( on ne va pas chercher la liste dans le dicitonnaire, simplement calculer la moyenne d'une liste ).
4. Compléter la fonction suivante qui renvoie le jeu avec la meilleure moyenne.

```python
def gotm():
    meilleur_moyenne = 0
    meilleur = ""
    for jeu in bibliotheque:
        if moyenne(jeu[...]) > ... :
            meilleur_moyenne = ...
            meilleur = jeu[...]
    return meilleur
```

## **Exercice 2 – Base de données miniaturisée**

On veut représenter une mini base de données d'albums par genre musical.
Chaque genre est une **clé du dictionnaire**, et la valeur associée est une **liste de tuples** :

```python
mediatheque = {
    "Rap": [("333", "Chilla", 2024), ("Trone", "Booba", 2017)],
    "Rock": [("Ummagumma", "Pink Floyd", 1969), ("Highway to Hell", "AC/DC", " 1979)],
    "Electro": [("Random Access Memories", "Daft Punk", 2013), ("What Came Before", "Chase & Status", 2022)]
}
```

1. Afficher l’année de sortie de l'album `"Trone"` de `"Booba"`.
2. Ajouter dans `"Rap"` l'album `"To pimp a butterfly"` de `"Kendrick Lamar"` (2015).
3. Recopier et compléter la fonction `tous_les_albums(theque)` qui retourne **une liste contenant tous les titres**, tout genres confondus.
```python
def tous_les_albums(theque):
    res = []
    for liste in theque. ...:
        for titre, artiste, date in ...:
            res...
    return res
```


## **Exercice 3 – Gestion des salles informatiques**

Un professeur de NSI souahiterai organiser ses salles pour avoir les meilleurs conditions de travail.
Chaque salle est représenté par un **tuple** :

```python
(salle, nombre_dordinateurs)
```

Et l'ensemble des salles est stocké dans une **liste**.

On vous donne :

```python
lycee = [
    ("B101-103", 9),
    ("B109-111", 13),
    ("B106", 22),
    ("B107", 24),
    ("B105", 25)
]
```

1. Afficher le nombre d'ordinateurs de la salle `"B106"` en utilisant la liste et le tuple.
2. Ajouter à la liste, une nouvelle salle `"B102"` contenant `1` seul ordinateur.
3. Recopier et compléter la fonction `meilleure()` qui renvoie la salle ayant le plus d'ordinateurs dans lycée.
```python
def meilleure():
    maxi = lycee[0][1]
    salle = lycee[0][0]
    for salle, nombre in ...:
        if ...:
            maxi = ...
            salle = ...
    return ...
```
4. Écrire une fonction `recherche(salle)` qui renvoie le nombre d'ordinateurs de la salle passée en paramètre.
   
