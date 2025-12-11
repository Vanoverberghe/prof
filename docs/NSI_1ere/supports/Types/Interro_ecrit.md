# **Interrogation – Python : listes, tuples et dictionnaires ( Partie écrite )**

## **Exercice 1 – Définitions et notions théoriques**

Répondre brièvement aux questions suivantes :

1. (a) Qu’est-ce qu’une **liste** en Python ?
   (b) Donner un exemple de liste contenant trois éléments.

2. (a) Qu’est-ce qu’un **tuple** en Python ?
   (b) Donner un exemple de tuple contenant trois éléments.

3. (a) Qu’est-ce qu’un **dictionnaire** en Python ?
   (b) Donner un exemple de dictionnaire contenant au moins deux couples clé-valeur.

4. Citer **une différence** entre une liste et un tuple.

5. Citer **un point commun** entre une liste et un dictionnaire.

6. Citer **une différence** entre un tuple et un dictionnaire.

---

## **Exercice 2 – Manipulation de listes**

On donne la liste suivante :

```python
notes = [12, 15, 9, 18, 14]
```

1. Donner la valeur de :
   (a) `notes[0]`
   (b) `notes[3]`
   (c) `notes[-1]`

2. Ajouter la note `16` à la liste (écrire le code).

3. Remplacer la note `9` par `10` (écrire le code).

4. Afficher la **longueur** de la liste (écrire le code).

5. Expliquer en une phrase ce que signifie : *une liste est mutable*.

---

## **Exercice 3 – Manipulation de tuples**

On considère le tuple suivant :

```python
coord = (4, 7)
```

1. Donner la valeur de `coord[1]`.
2. Peut-on modifier la valeur du premier élément du tuple ? Justifier.
3. Créer un tuple appelé `info` contenant : votre prénom, votre âge, et votre classe.
4. À partir du tuple suivant :

   ```python
   t = ("python", 3, "NSI", 2025)
   ```

   Donner :

   * le premier élément
   * Un *dépaquetage* avec 4 variables `theme`, `interro`, `spe`et `annee`.

---

## **Exercice 4 – Manipulation de dictionnaires**

On donne le dictionnaire :

```python
eleve = {"nom": "Durand", "age": 16, "classe": "1ère"}
```

1. Donner la valeur associée à la clé `"age"`.
2. Ajouter une clé `"option"` associée à la valeur `"NSI"`.
3. Modifier l’âge pour qu’il devienne `17`.
4. Écrire une ligne de code pour afficher **toutes les clés** du dictionnaire.
5. Expliquer en une phrase ce qu’est une **clé** dans un dictionnaire.

---

## **Exercice 5 – Comparaisons et analyse**

1. Classer les trois structures selon qu’elles sont **mutables** ou **immutables**.
2. Pour chaque structure (liste, tuple, dictionnaire), dire si les éléments sont :

   * **ordonnés** ou **non ordonnés**,
   * **accessibles par indice**, **par clé**, ou les deux.
3. Parmi les trois structures, laquelle est la plus adaptée pour représenter :
   (a) des coordonnées `(x, y)` ? Pourquoi ?
   (b) un ensemble de notes d’un élève ? Pourquoi ?
   (c) les informations d’une personne (nom, âge, adresse) ? Pourquoi ?