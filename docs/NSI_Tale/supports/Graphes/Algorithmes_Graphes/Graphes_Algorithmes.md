## IV. Parcours de graphes

### 1. Parcours en profondeur (DFS)

Le parcours en profondeur (ou "depth-first search" en anglais) est une méthode utilisée pour parcourir un graphe. Il s'agit d'une stratégie qui commence par un sommet racine, puis explore autant en profondeur que possible le long de chaque branche avant de passer à la branche suivante. C'est à dire qu'on explore les voisins des voisins d'abord.

1. On commence par choisir le sommet racine.
2. On avance dans une branche au choix jusqu'à arriver à un sommet qui n'a pas de voisins pas encore explorés.
3. On revient au sommet le plus proche ayant un voisin non exploré.
4. On répète les étapes 2 et 3 jusqu'à ce que tout les sommets soient visités.

### 2. Parcours en largeur (BFS)

Le parcours en largeur (ou "breadth-first search" en anglais) est également une méthode utilisée pour parcourir un graphe. Il s'agit d'une stratégie qui commence par un sommet racine, puis explore toutes les branches partant de cette racine avant de passer au prochain sommet. C'est à dire qu'on explore tous les voisins de la racine avant d'avancer vers les autre voisins.

1. On commence par choisir le sommet racine.
2. On explore tous les voisins de la racine et on les garde dans une file d'attente.
3. On explore les voisins des noeuds dans l'ordre de la file d'attente.
4. On répète les étapes 2 et 3 jusqu'à ce que tout les sommet soient visités.

## V. Algorithmes sur les graphes

### 1. Algorithme de Dijkstra

- Trouve le plus court chemin entre deux sommets dans un graphe pondéré.

### 2. Algorithme de Bellman-Ford

- Trouve le plus court chemin entre un sommet source et tous les autres sommets dans un graphe pondéré (peut gérer les poids négatifs).

