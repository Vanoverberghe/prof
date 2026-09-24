class Livre:
    def __init__(self, titre, auteur, annee, nb_pages, genre):
        self.titre    = titre
        self.auteur   = auteur
        self.annee    = annee      # année de publication
        self.nb_pages = nb_pages   # nombre de pages
        self.genre    = genre      # genre littéraire

livres = [
    Livre("Le Comte de Monte-Cristo",   "Alexandre Dumas",        1844, 1276, "aventure"),
    Livre("Les Misérables",             "Victor Hugo",            1862, 1488, "roman historique"),
    Livre("Germinal",                   "Émile Zola",             1885,  591, "roman social"),
    Livre("L'Étranger",                 "Albert Camus",           1942,  186, "philosophique"),
    Livre("Le Petit Prince",            "Antoine de Saint-Exupéry",1943, 96,  "conte"),
    Livre("Madame Bovary",              "Gustave Flaubert",       1857,  468, "roman"),
    Livre("Les Fleurs du mal",          "Charles Baudelaire",     1857,  336, "poésie"),
    Livre("Voyage au bout de la nuit",  "Louis-Ferdinand Céline", 1932,  505, "roman"),
    Livre("La Modification",            "Michel Butor",           1957,  238, "roman"),
    Livre("Bonjour tristesse",          "Françoise Sagan",        1954,  189, "roman"),
]
