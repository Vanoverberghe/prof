## 4. Corrigés / Pistes de solution

*(Tu peux essayer d’abord, puis revenir ici.)*

### 4.1 Listes

**Exercice 1 – corrigé possible**

```python
nombres = [10, 20, 30]

# 1
nombres.append(40)          # [10, 20, 30, 40]

# 2
nombres[1] = 25             # [10, 25, 30, 40]

# 3
nombres.pop(0)              # supprime 10 → [25, 30, 40]

# 4
nombres.sort(reverse=True)  # [40, 30, 25]
```

**Exercice 2 – corrigé possible**

```python
lettres = ["a", "b", "c", "d"]

# 1
print(len(lettres))     # 4

# 2
print(lettres[1])       # "b"

# 3
print(lettres[-2:])     # ["c", "d"]
```

---

### 4.2 Tuples

**Exercice 3 – corrigé possible**

```python
point = (3, 5)

# 1
x, y = point   # x = 3, y = 5
```

* 2 : Faire `point[0] = 10` provoque une **erreur** de type (`TypeError`) car les tuples sont **immutables** : on ne peut pas changer un élément.

---

**Exercice 4 – corrigé possible**

```python
date_naissance = (15, 8, 1990)

# 1
phrase = f"Né(e) le {date_naissance[0]}/{date_naissance[1]}/{date_naissance[2]}"
print(phrase)

# 2
seul = ("Python",)
print(type(seul))   # <class 'tuple'>
```

---

### 4.3 Dictionnaires

**Exercice 5 – corrigé possible**

```python
personne = {"nom": "Dupont", "age": 30}

# 1
personne["ville"] = "Paris"

# 2
personne["age"] = 31

# 3
print(personne.keys())     # dict_keys(['nom', 'age', 'ville'])

# 4
print(personne.items())    # dict_items([('nom', 'Dupont'), ('age', 31), ('ville', 'Paris')])
```

---

**Exercice 6 – corrigé possible**

```python
notes = {"maths": 15, "français": 12, "histoire": 14}

# 1
print(notes["maths"])   # 15

# 2
notes["physique"] = 16

# 3
notes.pop("histoire")

# 4
print("anglais" in notes)   # False
```

---

### 4.4 Choix du type – proposition

**Exercice 7 – réponses possibles**

1. Coordonnées `(x, y)` d’un point → **tuple**

   * Deux valeurs fixes qui vont ensemble, pas besoin de modifier.
2. Liste de courses → **liste**

   * Suite ordonnée d’éléments que l’on ajoute/supprime.
3. Un élève avec nom, âge, classe → **dictionnaire**

   * Données nommées, on accède par clé (`"nom"`, `"age"`, …).
4. Une date (jour, mois, année) → **tuple**

   * 3 valeurs fixes qui vont ensemble.
5. Capitales des pays d’Europe par nom de pays → **dictionnaire**

   * Accès direct à la capitale via le nom du pays comme clé.

---

### 4.5 Exercices construits

**3.1 – Gestion de notes d’élèves (solution possible)**

```python
eleves = [
    {"nom": "Alice", "age": 20, "notes": [15, 12, 18]},
    {"nom": "Bob", "age": 21, "notes": [10, 14, 16]},
    {"nom": "Charlie", "age": 19, "notes": [17, 13, 15]},
]

# 2. Calcul des moyennes
for eleve in eleves:
    notes = eleve["notes"]
    moyenne = sum(notes) / len(notes)
    print(f"{eleve['nom']} a une moyenne de {moyenne:.2f}")

# 3. Ajout d’un nouvel élève
nouvel_eleve = {"nom": "Diane", "age": 20, "notes": [14, 15, 16]}
eleves.append(nouvel_eleve)

# Recalcul
for eleve in eleves:
    notes = eleve["notes"]
    moyenne = sum(notes) / len(notes)
    print(f"{eleve['nom']} a une moyenne de {moyenne:.2f}")
```

---

**3.2 – Stock de produits (solution possible)**

```python
stock = {
    "pomme": {"prix": 1.2, "quantite": 30},
    "banane": {"prix": 2.0, "quantite": 20},
    "orange": {"prix": 1.5, "quantite": 25},
}

def valeur_stock(produit):
    if produit not in stock:
        return 0
    info = stock[produit]
    return info["prix"] * info["quantite"]

# 3. Valeur totale pour chaque produit
for produit in stock:
    valeur = valeur_stock(produit)
    print(f"Valeur du stock de {produit} : {valeur} €")

def ajouter_stock(produit, quantite):
    if produit in stock:
        stock[produit]["quantite"] += quantite
    else:
        print(f"Erreur : le produit '{produit}' n'existe pas dans le stock.")

# Exemple d'utilisation
ajouter_stock("pomme", 10)
ajouter_stock("fraise", 5)  # produit inexistant
```

---

**3.3 – Transformation de données (solution possible)**

```python
donnees = [
    ("alice", 25, "Paris"),
    ("bob", 30, "Lyon"),
    ("charlie", 22, "Marseille"),
]

# 1. Liste de dictionnaires
utilisateurs = []
for pseudo, age, ville in donnees:
    utilisateurs.append({
        "pseudo": pseudo,
        "age": age,
        "ville": ville
    })

# 2. Dictionnaire utilisateurs_par_ville
utilisateurs_par_ville = {}
for user in utilisateurs:
    ville = user["ville"]
    pseudo = user["pseudo"]
    if ville not in utilisateurs_par_ville:
        utilisateurs_par_ville[ville] = []
    utilisateurs_par_ville[ville].append(pseudo)

# 3. Affichage des pseudos pour une ville donnée
ville_cherchee = "Paris"
if ville_cherchee in utilisateurs_par_ville:
    print(f"Utilisateurs à {ville_cherchee} : {utilisateurs_par_ville[ville_cherchee]}")
else:
    print(f"Aucun utilisateur trouvé pour la ville {ville_cherchee}.")
```