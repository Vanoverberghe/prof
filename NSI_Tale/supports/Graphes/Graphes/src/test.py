from graphviz import Graph

# Dictionnaire représentant le graphe
graph_dict = {
    'A': ['B', 'C'], 
    'B': ['A', 'C', 'D'], 
    'C': ['A', 'B', 'E'],  
    'D': ['B', 'E'],  
    'E': ['C', 'D', 'F'],  
    'F': ['E'],
}

# Création d'un graphe non orienté
g = Graph(engine = "circo", format='png')

# Pour éviter les doublons d'arêtes (car le graphe est non orienté)
added_edges = set()

# Ajouter les arêtes
for node, neighbors in graph_dict.items():
    for neighbor in neighbors:
        edge = tuple(sorted([node, neighbor]))
        if edge not in added_edges:
            g.edge(node, neighbor)
            added_edges.add(edge)

# Afficher ou enregistrer le graphe
g.render('graphe', view=True)  # Cela crée 'graphe.png' et l'affiche
