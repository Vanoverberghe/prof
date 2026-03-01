# Synthèse ABR Cormen
L'extrait du Cormen fourni traite des arbres binaires de recherche, des structures de données qui supportent diverses opérations sur des ensembles dynamiques telles que RECHERCHER, MINIMUM, MAXIMUM, PRÉDÉCESSEUR, SUCCESSEUR, INSÉRER et SUPPRIMER. Un arbre binaire de recherche peut servir de dictionnaire ou de file de priorités. Les opérations de base ont un temps d'exécution proportionnel à la hauteur de l'arbre.

Lorsqu'un arbre binaire de recherche est complet à n nœuds, les opérations de base s'exécutent en O(log n) dans le pire des cas. En revanche, si l'arbre se réduit à une chaîne linéaire, le temps nécessaire est O(n) dans le pire des cas. Le texte mentionne que la hauteur attendue d'un arbre binaire de recherche construit aléatoirement est O(log n), permettant ainsi des opérations de base en O(log n) en moyenne.

Certaines variantes d'arbres binaires de recherche, comme les arbres rouge-noir, garantissent de bonnes performances même dans le pire des cas. Les B-arbres, présentés plus tard, sont efficaces pour gérer des bases de données sur des espaces de stockage secondaire.

Le Cormen introduit une conception possible d'un arbre binaire de recherche organisé comme un arbre binaire où chaque nœud contient une clé et des références vers ses enfants gauche et droite, ainsi que son parent. La propriété d'arbre binaire de recherche assure que les clés du sous-arbre gauche sont inférieures ou égales à la clé du nœud, et celles du sous-arbre droit sont supérieures ou égales.

On aborde ensuite les opérations de requête dans un arbre binaire de recherche, mettant en lumière la recherche de clés ainsi que les opérations MINIMUM, MAXIMUM, SUCCESSEUR et PRÉDÉCESSEUR. Les procédures présentées sont conçues pour s'exécuter en temps O(h), où h est la hauteur de l'arbre.

1. **Recherche (ARBRE-RECHERCHER) :** La procédure recherche un nœud avec une clé donnée dans un arbre binaire de recherche. Elle suit un chemin descendant en comparant la clé à chaque nœud rencontré, atteignant un temps d'exécution O(h).

2. **Minimum et Maximum (ARBRE-MINIMUM et ARBRE-MAXIMUM) :** Ces procédures trouvent respectivement le nœud avec la clé minimale et maximale dans un sous-arbre. Elles suivent les pointeurs gauche ou droit à partir de la racine jusqu'à NIL, et leur temps d'exécution est O(h).

3. **Successeur et Prédécesseur (ARBRE-SUCCESSEUR et ARBRE-PRÉDÉCESSEUR) :** Ces procédures trouvent le successeur et le prédécesseur d'un nœud, respectivement, dans l'ordre déterminé par un parcours infixe. Le successeur est trouvé en suivant le chemin vers le bas dans le sous-arbre de droite ou en remontant l'arbre. Ces procédures s'exécutent en temps O(h).

On conclut en démontrant que les opérations de recherche, minimum, maximum, successeur et prédécesseur peuvent toutes s'effectuer en temps O(h) sur un arbre binaire de recherche de hauteur h.

La partie suivante traite de l'insertion et la suppression:

1. **Insertion :** La procédure ARBRE-INSÉRER permet d'ajouter un nouvel élément à l'arbre binaire de recherche. Elle suit un chemin descendant de la racine jusqu'à la position d'insertion souhaitée, en bifurquant à gauche ou à droite en fonction des comparaisons de clés. La complexité de cette opération est O(h), où h est la hauteur de l'arbre.

ARBRE-INSÉRER(T,z)
1 y ← NIL
2 x ← racine[T]
3 tant que x fi NIL
4 faire y ← x
5 si clé[z] < clé[x]
6 alors x ← gauche[x]
7 sinon x ← droite[x]
8 p[z] ← y
9 si y = NIL
10 alors racine[T] ← z  arbre T était vide
11 sinon si clé[z] < clé[y]
12 alors gauche[y] ← z
13 sinon droite[y] ← z

2. **Suppression :** La procédure ARBRE-SUPPRIMER prend comme argument un pointeur sur un nœud z à supprimer de l'arbre. Elle gère trois cas : si z n'a pas d'enfant, si z a un seul enfant, et si z a deux enfants. La suppression est réalisée en détachant correctement le nœud z, et la complexité de cette opération est également O(h), où h est la hauteur de l'arbre.

ARBRE-SUPPRIMER(T,z)
1 si gauche[z] = NIL ou droite[z] = NIL
2 alors y ← z
3 sinon y ← ARBRE-SUCCESSEUR(z)
4 si gauche[y] fi NIL
5 alors x ← gauche[y]
6 sinon x ← droite[y]
7 si x fi NIL
8 alors p[x] ← p[y]
9 si p[y] = NIL
10 alors racine[T] ← x
11 sinon si y = gauche[p[y]]
12 alors gauche[p[y]] ← x
13 sinon droite[p[y]] ← x
14 si y fi z
15 alors clé[z] ← clé[y]
16 copier données satellites de y dans z
17 retourner y

Encore une fois on peut conclure en affirmant que les opérations d'insertion et de suppression peuvent être exécutées en temps O(h) sur un arbre binaire de recherche de hauteur h.