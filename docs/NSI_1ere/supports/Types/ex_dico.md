# Fiche d’exercices – *Les dictionnaires en Python*

## Rappel de cours

Un **dictionnaire** est une structure de données qui associe des **clés** à des **valeurs**.

```python
mon_dict = {"nom": "Alice", "age": 25, "ville": "Paris"}
```

* Les clés doivent être **uniques**.
* On y accède via **la clé**, pas l’indice.
* Type : `dict`

### Méthodes principales

| Méthode          | Description        |
| ---------------- | ------------------ |
| `d[key]`         | Accès à la valeur  |
| `d.get(key)`     | Accès sécurisé     |
| `d[key] = value` | Ajout/modification |
| `d.pop(key)`     | Suppression        |
| `d.keys()`       | Liste des clés     |
| `d.values()`     | Liste des valeurs  |
| `d.items()`      | Paires clé/valeur  |

---

## Exercice 1 – Création de dictionnaire

1. Crée un dictionnaire `eleve` avec les clés : `"nom"`, `"age"`, `"moyenne"`.
2. Ajoute une nouvelle clé `"classe"` avec une valeur.
3. Affiche uniquement le nom de l’élève.

---

## Exercice 2 – Accès & modification

À partir du dictionnaire suivant :

```python
film = {"titre": "Inception", "realisateur": "Nolan", "année": 2010}
```

1. Affiche l’année de sortie.
2. Modifie la valeur `"année"` en `2012`.
3. Ajoute la clé `"notation"` avec la valeur `8.8`.

---

## Exercice 3 – Parcours d’un dictionnaire

```python
capitales = {"France": "Paris", "Allemagne": "Berlin", "Italie": "Rome"}
```

1. Affiche toutes les **clés**.
2. Affiche toutes les **valeurs**.
3. Affiche chaque phrase sous la forme :
   ➤ *La capitale de France est Paris.*

---

## Exercice 4 – Dictionnaire et condition

```python
notes = {"Maths": 14, "Français": 12, "Histoire": 9}
```

Écris un programme qui affiche uniquement les matières avec une note **supérieure ou égale à 12**.

---

## Exercice 5 – Fonction et dictionnaires

Écris une fonction `moyenne_notes(d)` qui prend un dictionnaire de notes et renvoie la moyenne des valeurs.

Exemple :

```python
{"Maths": 14, "Physique": 16}
→ 15
```

---

## Défi (niveau avancé)

Tu disposes de la liste suivante :

```python
fruits = ["pomme", "banane", "cerise"]
prix = [2.5, 1.8, 3.2]
```

1. Crée automatiquement un dictionnaire associant chaque fruit à son prix.
2. Demande à l'utilisateur un fruit et affiche son prix.
3. Si le fruit n’est pas dans le dictionnaire, propose d’ajouter un nouveau prix.

---

## Bonus – Dictionnaire imbriqué

```python
classe = {
    "Alice": {"age": 15, "moyenne": 14},
    "Bob": {"age": 16, "moyenne": 12}
}
```

1. Affiche l’âge de **Bob**.
2. Augmente la moyenne de **Alice** de 1 point.

