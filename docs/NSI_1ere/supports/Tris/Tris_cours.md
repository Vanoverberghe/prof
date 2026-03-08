# 1. Les algorithmes de tri

Un **algorithme de tri** est une méthode qui permet de **trier automatiquement une liste**.

Il existe de nombreux algorithmes :

* tri par sélection
* tri par insertion
* tri à bulles
* tri rapide (quicksort)
* tri fusion

On va se concentrer sur les 2 premiers:

* **tri par sélection**
* **tri par insertion**

# 2. Le tri par sélection

## Principe

Le **tri par sélection** consiste à :

1. Chercher le **plus petit élément** de la liste.
2. Le placer **au début de la liste**.
3. Recommencer avec le reste de la liste.

On répète jusqu'à ce que toute la liste soit triée.

## Exemple pas à pas

Liste :

```
[7, 3, 9, 2, 5]
```
<br>
<br>
<br>
<br>
<br>
<br>

### Étape 1

On cherche le plus petit élément :

```
7, 3, 9, 2, 5
```

Le minimum est **2**.

On échange avec le premier élément.

```
[2, 3, 9, 7, 5]
```

### Étape 2

On cherche le plus petit dans la partie restante :

```
3, 9, 7, 5
```

Minimum = **3**

La liste reste :

```
[2, 3, 9, 7, 5]
```

### Étape 3

Dans :

```
9, 7, 5
```

Minimum = **5**

On échange avec 9 :

```
[2, 3, 5, 7, 9]
```

Liste triée.

<br>

# 4. Le tri par insertion

## Principe

Le **tri par insertion** fonctionne comme lorsque l'on **trie des cartes à jouer dans sa main**.

On prend les éléments **un par un** et on les **insère au bon endroit dans la partie déjà triée**.

## Exemple pas à pas

Liste :

```
[7, 3, 9, 2, 5]
```


### Étape 1

On considère que le premier élément est trié :

```
[7] 3 9 2 5
```

### Étape 2

On prend **3** et on l’insère dans la partie triée.

```
[3 7] 9 2 5
```

### Étape 3

On prend **9** :

```
[3 7 9] 2 5
```

Déjà bien placé.

<br>
<br>

### Étape 4

On prend **2** :

```
[2 3 7 9] 5
```

### Étape 5

On insère **5**

```
[2 3 5 7 9]
```

### Résultat

```
[2, 3, 5, 7, 9]
```