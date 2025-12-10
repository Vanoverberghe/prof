## 1. Rappels théoriques

### 1.1 Listes (`list`)

* **Syntaxe** : `ma_liste = [1, 2, 3]`
* **Indexation** : `ma_liste[0]` → premier élément
* **Mutables** : on peut modifier, ajouter, supprimer des éléments
* **Méthodes utiles** :

  * `append(x)` : ajoute à la fin
  * `insert(i, x)` : insère à l’index `i`
  * `pop(i)` : supprime et renvoie l’élément à l’index `i` (ou le dernier si i omis)
  * `remove(x)` : supprime la première occurrence de `x`
  * `sort()` / `sorted(ma_liste)` : tri
* **Utilisation typique** : collection ordonnée d’objets qui **change** dans le temps (liste d’utilisateurs, tâches, etc.)

---

### 1.2 Tuples (`tuple`)

* **Syntaxe** :

  * `mon_tuple = (1, 2, 3)`
  * ou `mon_tuple = 1, 2, 3`
  * tuple à un seul élément : `t = (42,)`
* **Indexation** : `mon_tuple[0]`
* **Immutables** : on ne peut pas modifier les éléments après création.
* **Utilisation typique** :

  * Regrouper plusieurs valeurs qui vont ensemble (coordonnées, date `(jour, mois, année)`, etc.)
  * Comme clés de dictionnaire si les éléments sont eux-mêmes immuables.

---

### 1.3 Dictionnaires (`dict`)

* **Syntaxe** : `mon_dict = {"clé": valeur, "nom": "Alice", "age": 30}`
* **Accès par clé** : `mon_dict["nom"]` → `"Alice"`
* **Mutables** : on peut ajouter/modifier/supprimer des paires clé/valeur
* **Méthodes utiles** :

  * `mon_dict["nouvelle_cle"] = valeur` : ajout / modification
  * `mon_dict.get("cle", valeur_par_defaut)` : accès sécurisé
  * `keys()`, `values()`, `items()` : vues sur clés, valeurs, paires
  * `pop("cle")` : supprime et renvoie la valeur associée
* **Utilisation typique** : stocker des **informations structurées** associées à des **clés** (comme un mini enregistrement / objet).

---

### 1.4 Tableau comparatif

| Type         | Syntaxe     | Mutable ? | Accès     | Usage typique                        |
| ------------ | ----------- | --------- | --------- | ------------------------------------ |
| Liste        | `[1, 2, 3]` | Oui       | Par index | Suite ordonnée d’éléments modifiable |
| Tuple        | `(1, 2, 3)` | Non       | Par index | Regrouper des valeurs fixes          |
| Dictionnaire | `{"a": 1}`  | Oui       | Par clé   | Associer des clés à des valeurs      |

---

## 2. Exercices courts

### 2.1 Listes

**Exercice 1**
On a la liste suivante :

```python
nombres = [10, 20, 30]
```

1. Ajoute le nombre `40` à la fin de la liste.
2. Remplace le `20` par `25`.
3. Supprime le premier élément de la liste (celui à l’index 0).
4. Trie la liste dans l’ordre décroissant.

---

**Exercice 2**
On a :

```python
lettres = ["a", "b", "c", "d"]
```

1. Affiche la longueur de la liste.
2. Affiche le deuxième élément.
3. Affiche les deux derniers éléments avec un **slice**.

---

### 2.2 Tuples

**Exercice 3**
On a le tuple suivant :

```python
point = (3, 5)
```

1. Affecte la valeur `3` à une variable `x` et `5` à une variable `y` à partir de ce tuple (unpacking).
2. Essaie (en pensée) de faire `point[0] = 10`. Que se passe-t-il ? Pourquoi ?

---

**Exercice 4**
On a :

```python
date_naissance = (15, 8, 1990)
```

1. Crée une phrase `"Né(e) le 15/8/1990"` en utilisant le tuple.
2. Crée un tuple `seul = ("Python",)` puis vérifie son type avec `type(seul)`.

---

### 2.3 Dictionnaires

**Exercice 5**
On a le dictionnaire :

```python
personne = {"nom": "Dupont", "age": 30}
```

1. Ajoute une clé `"ville"` avec la valeur `"Paris"`.
2. Modifie l’âge pour qu’il devienne `31`.
3. Affiche toutes les clés du dictionnaire.
4. Affiche toutes les paires clé/valeur.

---

**Exercice 6**
On a :

```python
notes = {"maths": 15, "français": 12, "histoire": 14}
```

1. Affiche la note en **maths**.
2. Ajoute une matière `"physique"` avec la note `16`.
3. Supprime la matière `"histoire"` du dictionnaire.
4. Vérifie si `"anglais"` est une clé du dictionnaire.

---

### 2.4 Choisir entre liste, tuple et dict

**Exercice 7**
Pour chaque situation, choisis le type le plus adapté (**liste**, **tuple** ou **dictionnaire**) et explique rapidement pourquoi.

1. Stocker les coordonnées `(x, y)` d’un point dans un plan.
2. Stocker la liste de courses d’un utilisateur.
3. Représenter un élève avec son nom, son âge et sa classe.
4. Représenter une date (jour, mois, année).
5. Stocker les capitales des pays d’Europe, accessibles par le nom du pays.

---

## 3. Exercices plus construits

### 3.1 Gestion de notes d’élèves (listes + dictionnaires)

On veut représenter une classe d’élèves et leurs notes.

**Consigne :**

1. Crée une liste `eleves` contenant 3 dictionnaires, chacun représentant un élève avec la structure :

   ```python
   {
       "nom": "Alice",
       "age": 20,
       "notes": [15, 12, 18]
   }
   ```

2. Écris une boucle qui :

   * parcourt la liste `eleves`
   * calcule la moyenne des notes de chaque élève
   * affiche : `"Alice a une moyenne de X"` (remplace Alice et X).

3. Ajoute un nouvel élève à la liste, puis relance la boucle de calcul.

---

### 3.2 Gestion d’un stock de produits (dictionnaires de dictionnaires)

On gère un mini stock.

**Consigne :**

1. Crée un dictionnaire `stock` de la forme :

   ```python
   stock = {
       "pomme": {"prix": 1.2, "quantite": 30},
       "banane": {"prix": 2.0, "quantite": 20},
       "orange": {"prix": 1.5, "quantite": 25},
   }
   ```

2. Écris une fonction `valeur_stock(produit)` qui :

   * prend en paramètre le nom d’un produit (ex : `"pomme"`)
   * renvoie la **valeur totale** de ce produit en stock (`prix * quantite`).

3. Utilise cette fonction pour afficher la valeur totale du stock pour **tous** les produits.

4. Écris une fonction `ajouter_stock(produit, quantite)` qui :

   * augmente la quantité d’un produit existant
   * si le produit n’existe pas, affiche un message d’erreur.

---

### 3.3 Transformation de données (tuples + listes + dicts)

Tu reçois des données d’utilisateurs sous forme de tuples :

```python
donnees = [
    ("alice", 25, "Paris"),
    ("bob", 30, "Lyon"),
    ("charlie", 22, "Marseille"),
]
```

Chaque tuple contient : `(pseudo, age, ville)`.

**Consigne :**

1. Transforme cette liste de tuples en une liste de dictionnaires avec la structure :

   ```python
   {"pseudo": "...", "age": ..., "ville": "..."}
   ```

2. À partir de cette liste de dictionnaires, construis un **dictionnaire** `utilisateurs_par_ville` de la forme :

   ```python
   {
       "Paris": ["alice", ...],
       "Lyon": ["bob", ...],
       "Marseille": ["charlie", ...]
   }
   ```

3. Affiche la liste des pseudos pour une ville donnée, par exemple `"Paris"`.