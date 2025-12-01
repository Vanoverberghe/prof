<b><h2 style="text-align:center">Modèle relationnel</h2></b>

# Exercice 1 : Loueur de voitures  

Deux relations modélisent la flotte de voitures d'un réseau de location de voitures.  

![agences](./img/agences.png)  

1. La relation `Voitures` :  

- [ ]  comporte 3 attributs  
- [ ] comporte 6 attributs  
- [ ] est de cardinal 3  
- [ ] est de cardinal 6  

2. Le domaine de l'attribut `id_agence` dans la relation `Voitures` est :  
- [ ] Agences  
- [ ] les entiers naturels  
- [ ] les chaînes de caractères  
- [ ] Voitures  

3. Le schéma relationnel de la relation `Agences` est :  
- [ ] (id_agence, Ville, Département)  
- [ ] (1, "Paris", 75)  
- [ ] ((id_agence, Entier ), (Ville, Chaine ), (Département, Chaine))  
- [ ] ((id_agence, Entier ), (Ville, Chaine ), (Département, Entier))  

4. La relation `Agences` : 
- [ ] ne comporte pas de clé primaire  
- [ ] a `id_agence` pour clé primaire  
- [ ] a `Ville` pour clé primaire  
- [ ]  a `Département` pour clé primaire  

5. La relation `Voitures `:  
- [ ] ne comporte pas de clé primaire  
- [ ] comporte `id_agence` comme clé primaire  
- [ ] comporte  `id_voiture` comme  clé primaire  
- [ ] comporte  `id_agence` comme clé étrangère  

6. La relation `Agences` :  
- [ ] est bien modélisée  
- [ ] ne respecte pas les contraintes d'intégrité de relation  
- [ ] présente des informations redondantes 

7. La relation `Voitures` :  
- [ ] est bien modélisée  
- [ ] ne respecte pas les contraintes d'intégrité référentielles  
- [ ] présente des informations redondantes  


# Exercice 2  Ressources humaines

Soit une base de données dont le schéma relationnel est le suivant :

>EMPLOYE (<u>NumEmp</u>, Nom, Prénom, Adresse, Téléphone, Qualification)  
SERVICE (<u>NomService</u>, #Responsable, Téléphone)  
PROJET (<u>NomProjet</u>, DateDeb, DateFin, #NumEmp)  


1. Réécrire ce schéma sous forme de diagramme.
2. Un employé peut il avoir plusieurs qualifications ?
3. Un employé peut il faire plusieurs projets en même temps ?
4. Une personne peut elle être responsable de plusieurs services ?
5. Un service peut il avoir plusieurs responsables ?

# Exercice 3  Aéroport

Soit une base de données dont le schéma relationnel est le suivant :

>Pilote (<u>PLNUM</u>, PLNOM, PLPRENOM, VILLE, SALAIRE)  
Avion (<u>AVNUM</u>, AVNOM, CAPACITE, LOCALISATION)  
Vol (<u>VOLNUM</u>, #PLNUM, #AVNUM, VILLEDEP, VILLEARR, HEUREDEP, HEUREARR)  

Réécrire ce schéma sous forme de diagramme.

\newpage  

# Exercice 4 

1. En partant de la relation Films ci-dessous, créer une relation Réalisateurs  (id, nom, prenom et annee_naissance).  
2. Modifier la relation Films afin d’établir un lien avec les Réalisateurs. Préciser l’attribut qui jouera le rôle de clef étrangère.  

![films](./img/films.png)

# Exercice 5  
On considère la relation `Stock` qui recense des produits disponibles à la vente :

|code|	produit	|prix_unitaire|	quantité|
|:---:|:---:|:---:|:---:|
|3147281941305	|agenda 1j/p classique 12x18|	6.69|	21|
|3020122873556|cahier 24x32 96p 90g 5x5 marge	|4.20	|38|
|3045058208753	|chemise top file a4	|0.61	|56|
|3154140107154	|gomme blanche dessin	|0.70	|21|
|3154142291202	|stylo bille 4 couleurs	|2.99	|42|
|3270220000112	|2 crayons graphite hb	|2.15	|75|
|3037920310282	|50 pochettes perforées |2.50	|46|  

1. Donnez le nom de la relation correspondant à cette table.  
2. Citez les attributs de cette relation en précisant leur domaine.  
3. Donnez les tuples dont l'attribut prix_unitaire est inférieur à 1 €.  
4. Donnez le schéma relationnel, sous forme littérale,  de cette relation.  

# Exercice 6  
On considère la table `Etudiant` qui suit :

|numero|	nom	|inscription|	faculte|
|:---:|:---:|:---:|:---:|
|20201975	|Louis Dors|	05/09/2020|	sciences|
|20200811|	Tom Eigeri|	02/09/2020|	droit|
|20202368|	José Parentré|	06/09/2020|	lettres|
|20190493	|Anne Hémie	|02/09/2019|	médecine|
|20201832|	Jacques Célair	|05/09/2020	|staps|
|20192105	|Aubin Sahalor|	04/09/2019|	sciences|
|20191128	|Thibaud Monfils|	03/09/2019|	lettres|
|20200751|	Sarah Freichi|	02/09/2019	|droit|

1. Donnez le nom de la relation correspondant à cette table.  
2. Citez les attributs de cette relation en précisant leur domaine.  
3. Le tuple (20192105, "Thibaud Monfils", 03/09/2019; "sciences")  appartient-il à cette relation ? Justifiez votre réponse.  
4. Quel rôle peut-on donner à l'attribut `numero` dans cette relation ?  
5. Donnez le schéma relationnel de cette relation.
6.  Cette table présente-t-elle des redondances ? Si oui, lesquelles ?  
7. A-t-on intérêt à scinder cette table en créant une table pour l'attribut `inscription` ?  
8. Sachant que pour coder une date d’inscription il serait nécessaire de réserver :
   - 5 bits pour coder le jour de 1 à 31 ($`2^5`$ = 32 valeurs différentes),
   - 4 bits pour coder le mois de 1 à 12 ($`2^4`$ = 16 valeurs différentes),
   - 16 bits pour l'année de -32768 à 32767 ($`2^{16}`$  = 65536 valeurs),
justifiez que l’utilisation d’une clé étrangère ne serait pas nécessaire.  
9. A-t-on intérêt à scinder cette table en créant une table pour l'attribut faculte ?  
10. Proposez une autre conception de la base de données en scindant cette table en deux tables Etudiant et Faculte.  
11. Donnez le schéma relationnel, forme littérale, de la nouvelle base de données.
12. Si on supprime le tuple d'attribut faculte égal à sciences dans la relation Faculte, quelles en sont les conséquences ?

# Exercice 7  
On considère la table Internaute renseignée lors de l'inscription à un site :  

|nom	|naissance	|email	|pseudo|
|:---:|:---:|:---:|:---:|
|Anna Conda	|21/01/1990	|a.conda@liberte.fr	|Croc15|
|Luc Ratif|	14/11/1995	|lratif@tropcool.com|	Skyrythm|
|Amandine Aheurfix	|05/12/2001	|amandix@zone51.org	|Ufologue|
|Marc Assin	|18/06/2000	|m.assin3@liberte.fr|	Quileur0|
|Béa Bas	|09/05/1998	|bbas@aloha.net	|Sunnyx|
|Agathe Zeblues	|16/02/1992	|piano@musique.fr|	Piano|
|Charles Magne|	23/04/1997	|cmagne2@historia.org	|Durandal|
|Paul Ichinel|	12/08/2002|	paulic@tropcool.com|	Flask34|  

1. Indiquez pour chaque attribut s'il peut servir de clé primaire.  
2. Donnez deux schémas relationnels possibles pour la relation Internaute.  

# Exercice 8  
On considère la table suivant qui rassemble les notes sur 10 accordées à différents films par les abonnés au site cine.fr :  

|id	|titre	|sortie	|nom	|internaute	|note|
|:---:|:---:|:---:|:---:|:---:|:---:|
|1	|Idiocracy|	2007	|Anne Oraque|	aoraque@cine.fr|	7|
|2	|Avatar	|2009|	Maud Tete|	mtete2@cine.fr|	9|
|3|	Minority Report|	2002|	Eva Poret|	eporet@cine.fr|	5|
|4|	L'Homme bicentenaire|	2002| 	Guy Bol|	gbol1@cine.fr|	7|
|5|	Minority Report|	2002|	Maud Tete|	mtete2@cine.fr	|8|
|6|	Avatar	|2009|	Guy Bol|	gbol1@cine.fr|	10|
|7|	Idiocracy|	2007|	Eva Poret|	eporet@cine.fr|	6|
|8|	Minority Report	|2002|	Alain Di|	adi5@cine.fr	|4|
|9|	Avatar|	2009|	Eva Poret|	eporet@cine.fr|	8|
|10	|Avatar|	2009|	Anne Oraque|	aoraque@cine.fr|	3|
|11|	L'Homme bicentenaire|	2002|	Maud Tete|	mtete2@cine.fr|	7|
|12|	Idiocracy|	2007|	Maud Tete|	mtete2@cine.fr|	9|
|13	|Minority Report|	2002|	Ray Nette	|rnette@cine.fr|	4|
|14|	Avatar|	2009|	Alain Di|	adi5@cine.fr	|10|
|15|	Idiocracy|	2007|	Ray Nette	|rnette@cine.fr|	5|
|16|	L'Homme bicentenaire|	2002|	Alain Di|	adi5@cine.fr|	7|  
 
1. En combien de relations peut-on scinder cette table ? Justifier votre réponse.  
2. En déduire le schéma relationnel qui en découle.  
3. Et donc le contenu des tables qui en découle.  
