# 2. Arbres binaires

### 🔹 Définition
Un **arbre binaire** est un arbre dans lequel chaque nœud a **au plus deux enfants** (gauche et droit).

### Implémentation récursive (Python)

```python
from __future__ import annotations

class ArbreBinaire:
    """Structure de donnée d'arbre binaire"""

    def __init__(self, étiquette: str, gauche: ArbreBinaire, droit: ArbreBinaire):
        self.étiquette = étiquette
        self.gauche = gauche
        self.droit = droit
````

Chaque nœud contient :

* une **étiquette**,
* un **sous-arbre gauche**,
* un **sous-arbre droit**.

### 📍 Parcours d’un arbre binaire

Il existe plusieurs façons de parcourir ou visiter les nœuds :

#### ➤ Parcours en largeur d’abord

Visite les nœuds **de haut en bas** puis **de gauche à droite** (comme la lecture d’un texte).([lyceum][1])

#### ➤ Parcours en profondeur d’abord

| Type                        | Ordre                                         |
| --------------------------- | --------------------------------------------- |
| **Préfixe** (ou préordre)   | Visite le nœud → gauche → droit.([lyceum][1]) |
| **Infixe** (ou en-ordre)    | Gauche → nœud → droit.([lyceum][1])           |
| **Postfixe** (ou postordre) | Gauche → droit → nœud.([lyceum][1])           |

---

## 3) Arbres binaires de recherche (ABR)

### 🔹 Définition

Un **arbre binaire de recherche** est un **arbre binaire** où :

* dans le **sous-arbre gauche**, **toutes les valeurs sont inférieures** à la racine,
* dans le **sous-arbre droit**, **toutes les valeurs sont supérieures ou égales** à la racine.([lyceum][1])

### 💡 Propriétés

* Un ABR permet des **recherches rapides**, car les valeurs y sont **ordonnées**.([lyceum][1])

### ⛓️ Implémentation (concept)

On peut ajouter une méthode `insérer` dans la classe pour placer les nœuds correctement en fonction de leur valeur.([lyceum][1])

---

## 🧠 Applications & Exercices suggérés

### ✨ Vocabulaire & structure

* Identifier racine, feuilles, père et fils dans un arbre.([lyceum][1])

### 📏 Measures

* Calculer taille et hauteur d’un arbre.([lyceum][1])

### 🐍 Python

* Construire un **arbre binaire** avec la classe donnée.([lyceum][1])
* Accéder à l’étiquette d’un nœud en partant de la racine.([lyceum][1])

### 🔄 Parcours

* Générer les séquences de **parcours préfixe, infixe, postfixe** et en largeur d’un arbre.([lyceum][1])

### 🔍 ABR

* Construire différents **ABR** avec tous les entiers de 1 à 6 ou de 1 à 15.([lyceum][1])
* Comparer les stratégies d’insertion pour obtenir des arbres **complets** ou **parfaits**.([lyceum][1])

### 📊 Analyse

* Comparer **complexité** de recherche dans un ABR vs un arbre non structuré.([lyceum][1])

---

## 📌 Références utiles

* Programme officiel NSI – Structures de données (Arbres)([lyceum][2])
* Exercices complémentaires sur les arbres binaires et ABR([lyceum][3])

---

```

---

Si tu veux, je peux aussi générer une **version PDF** ou une **étude interactive** de ce chapitre (par exemple avec des diagrammes ou des quiz). Veux-tu ça ?
::contentReference[oaicite:28]{index=28}
```

[1]: https://www.lyceum.fr/tg/nsi/1-structures-de-donnees/4-arbres/?utm_source=chatgpt.com "Chapitre 4: Arbres – lyceum"
[2]: https://www.lyceum.fr/tg/nsi/?utm_source=chatgpt.com "NSI – lyceum"
[3]: https://www.lyceum.fr/tg/nsi/1-structures-de-donnees/4-arbres/exo/?utm_source=chatgpt.com "Exercices – lyceum"