# Activité réseau

### Le logiciel Filius

⚠️ Sélectionner Français

![fr](./img/capture_install_Filius.png)

Le logiciel dispose de deux modes ; on passe d’un mode à l’autre en cliquant sur l’icône correspondante :

- le mode conception, activé par l’icône « marteau »
![marteau](./img/iconmarteau.png)
- le mode simulation, activé par l’icône « flèche verte »
![sim](./img/iconsimul.png)

>Astuces : vérifier en cas de problèmes avec le logiciel Filius
>
>   - Etre en mode simulation pour ajouter lignes de commandes
>   - Les lignes de commandes doivent êre installées des deux côtés pour un ping
>   - Pour ping : les 2 doivent être configurés
>   - DHCP ne doit pas être configuré par DHCP mais en statique. Vérifier que son IP a bien été configurée
>   - Pour que DHCP fonctionne : appuyer sur la flèche verte simulation
>   - Pour mettre les adresses passerelles : décocher DHCP
>   - Pour reconnaître un fil, cliquer sur l’interface, cela apparaît en vert
>   - Les serveurs doivent être démarrés (mode simulation)
>   - Les cases "utiliser l'adresse IP comme nom" doivent être cochées pour que les IP visibles soient les bonnes.
>   - Si un cable ne s'allume jamais en vert, vous pouvez essayer de le supprimer, et d'en remettre un nouveau.




### Comment communiquer entre deux ordinateurs ?

Nous utiliserons le logiciel Filius.

- En mode conception, créer un ordinateur portable seul par « glisser-déposer ». Un double-clic sur cet ordinateur permet d’accéder à sa configuration réseau. Son adresse IP par défaut est 192.168.0.10. Changer cette adresse en 192.168.1.1 puis cocher Utiliser l’adresse IP comme nom (à faire sur chaque machine à l’avenir). Nous conservons comme masque 255.255.255.0

- Créer un second ordinateur portable. Changer son adresse IP en lui attribuant l’adresse 192.168.1.2.

- Relier les deux ordinateurs par un câble ethernet (prise RJ45).

<img src="./img/cable.png" width = 30%/>  

Observer qu’un câble posé peut ensuite être supprimé : clic-droit puis « supprimer ».

- Penser à sauvegarder votre travail régulièrement dans votre dossier Documents

- Passer en mode simulation. Par un double-clic sur la première machine (192.168.1.1), ouvrir l’installateur de logiciels.

![ordis](./img/deux_ordis.png)

- Installer la ligne de commande en la faisant passer à gauche avec

![fleche](./img/fleche.png)

⚠️ Ne pas oublier de cliquer sur « appliquer la modification »

- Ouvrir la ligne de commande (double-clic) et saisir l’instruction ipconfig.

1) Quelles informations nous apporte cette commande ipconfig ?

- Saisir la commande arp à l’invite de commande.

2) Que donne le tableau affiché ?

> Une adresse MAC (Media Access Control), parfois nommée adresse physique ou adresse Ethernet, est un identifiant physique stocké dans une carte réseau ou une interface réseau similaire. À moins qu'elle n'ait été modifiée par l'utilisateur, elle est unique au monde.
Elle est constituée de 6 octets écrits sous forme hexadécimale, chacun séparé par " : " (par exemple : 00:13:A9:58:32:EB).
Les 3 premiers octets définissent le constructeur de la carte réseau (ici Sony Corporation), les 3 derniers le numéro de fabrication. On peut retrouver le constructeur à partir de l’adresse MAC.


- Effectuer un ping vers la machine 192.168.1.2, la commande à saisir est : ping 192.168.1.2.
    
- Si tout va bien, on observe que le câble se colore en vert (parfois trop rapide pour être visible) le temps du transfert de données et qu’aucun paquet n’est perdu à ce stade.

3) Saisir à nouveau la commande arp à l’invite de commande Qu’est ce qui a changé depuis le ping ?

>Lorsque l’ordinateur 192.168.1.1 fait un ping vers 192.168.1.2 (couche réseau) et qu’il passe la requête à la couche liaison de données, cette couche a besoin de l’adresse MAC pour réaliser cette requête. Or il ne la connait pas. Un échange avec le protocole ARP permet de l’obtenir.

- Faire un clic-droit sur la machine 192.168.1.1 et afficher les échanges de données. Sélectionner la ligne du haut et lire les explications qui s’affichent dans la fenêtre du bas.

![arp1](./img/arp1.png)

![osi](./img/osi.png)

Source de l’image : https://cisco.goffinet.org/ccna/fondamentaux/modeles-tcp-ip-osi/
Légendes des icônes utilisées : (source : https://www.edrawsoft.com/fr/cisco-network-topology-icons.html) 

![legende](./img/legende.png)

>Les protocoles ARP et ICMP
>
>   - Les protocoles ARP et ICMP sont de la couche 3 du modèle OSI, c’est-à-dire de la couche internet du modèle TCP/IP
>    - Le protocole ARP : Adresse Resolution Protocol permet de lier à une adresse logique IP une adresse physique MAC.
>    - Le protocole ICMP : Internet Control Message Protocol permet de véhiculer des messages de contrôle et d'erreur.

👉 Nous allons étudier plus précisément les lignes de l’échange de données.

4) Expliquer comment 192.168.1.1 obtient l’adresse MAC de 192.168.1.2. En particulier à qui envoie-t-il la demande ?

   - La machine 1 envoie sur le réseau (à toutes les machines : adresse de diffusion) une demande de l'adresse MAC de la machine 2. (ligne 1 de l'image, avec l'explication en bas.)
   - La machine concernée lui renvoie son adresse MAC (ligne 2 de l'image).

5) Quelle est l’adresse IP de diffusion ?

6) Quel est le protocole utilisé par le ping ? Dans quelle couche du modèle TCP/IP se situe-t-il ?

7) A l’issue du ping, comment l’ordinateur 192.168.1.1 sait-il que l’ordinateur 192.168.1.2 est bien connecté ?


### Comment créer un réseau avec davantage d’ordinateurs ?

- Revenir en mode conception et créer un troisième puis un quatrième ordinateur portable.

Sur Filius les « portables » servent à simuler des ordinateurs, et les « ordinateurs » servent à simuler des serveurs.

- Vérifier alors qu’il est impossible de les relier aux autres par un câble (« il n’y a plus de connecteur disponible »). Pour créer un réseau avec plus de 2 ordinateurs il faut utiliser des switchs (ou commutateur).

- Câbler 4 ordinateurs autour d’un switch puis donner à ces nouveaux ordinateurs des adresses IP pertinentes.
- Tester les connexions de votre réseau local en faisant des « ping » entre les ordinateurs.
- Sauvegarder votre projet sous un nom pertinent (ex : `ReseauLocalAvecSwitch.fls`)


### Ajout d’un serveur DHCP

Si vous voulez ajouter des matériels dans votre réseau, sans avoir à paramétrer manuellement chacune des adresses IP de votre réseau, vous devez ajouter un serveur DHCP.

- Revenir en mode conception.

- Ajoutez un nouveau périphérique Ordinateur, le nommer Serveur DHCP, le relier au switch, le configurer avec l’adresse IP 192.168.1.253 .

- Double-cliquez sur le serveur DHCP que vous venez d’installer.

- Cliquez sur « configuration du service DHCP » : Une fenêtre s’ouvre et permet de définir les IP locales maximales et minimales parmi celles autorisées par le masque. Renseignez les IP comme indiqué ci-dessous :
    - Pour le début de plage, tapez : 192.168.1.10
    - Pour la fin de plage, tapez : 192.168.1.50
    - Cocher la case « activer le service DHCP »
    - Tapez OK

- Double-cliquez sur chaque ordinateur du réseau, cocher « adressage automatique par serveur DHCP » sauf sur le serveur DHCP qui doit être configuré en statique.

- Lancez à nouveau une simulation. Si vous avez bien gardé les adresses IP comme noms de vos matériels, vous voyez immédiatement l’adresse IP assignée par le serveur DHCP.

- Ajouter un portable dans ce réseau, le configurer automatiquement grâce au DHCP, et vérifier les connexions avec les autres matériels avec des ping.

Résultat obtenu : 

![dhcp1](./img/dhcp1.png)

## Deux réseaux

>De nombreuses raisons peuvent amener à connecter plusieurs réseaux entre eux. Pour notre activité, nous prendrons l’exemple de deux réseaux locaux internes à notre lycée (réseau pédagogique et réseau administratif).
>Pour des questions matérielles et de sécurité, il est préférable de séparer ces deux réseaux, tout en créant une liaison entre eux pour les relier (car on peut parfois avoir besoin d’échanges de données entre ces réseaux). Le lien entre ces réseaux se fait matériellement à l’aide d’un routeur. 

### Deux réseaux séparés

![td2](./img/td2_res1.png)

- En mode conception, ajouter un routeur (sélectionner 2 interfaces, c’est à dire deux prises RJ45) puis ajouter un switch, une machine de type portable et une autre de type ordinateur « tour ». Paramétrer leurs interfaces réseaux avec les adresses IP 192.168.2.1 pour le portable et 192.168.2.2 pour l’ordinateur « tour », et avec les masques 255.255.255.0

- En mode simulation, sur la machine 192.168.1.10, tester les connexions vers les autres machines avec la commande ping.

8) Quelles sont les machines qui ne peuvent pas être atteintes ?

> Chaque ordinateur d’un réseau doit connaitre l’adresse IP du routeur pour pouvoir lui transmettre les paquets n’appartenant pas à son réseau. Cette adresse est renseignée dans le champ Gateway (ou passerelle) de chaque ordinateur.

- En mode conception, Faire un clic droit sur le routeur puis configurer ses deux interfaces (c’est-à-dire les fils) en leur assignant la dernière adresse disponible de chaque réseau concerné. Quand vous cliquez sur une interface, elle apparaît en vert, ce qui permet de ne pas se tromper d’adresse.

- En mode simulation, sur la machine 192.168.1.10, tester à nouveau les connexions vers les machines injoignables avant la configuration du routeur. Le problème est-il résolu ?

- Il faut donc finaliser la configuration de ces réseaux. En mode conception, renseigner la passerelle (ou gateway en anglais) de chaque ordinateur. Pour cela, il faut commencer par décocher l’adressage automatique par serveur DHCP. Vous pourrez tous les recocher à la fin lorsque vous aurez terminé.

⚠️ Attention, chaque réseau possède sa propre passerelle !

L’adresse IP de la passerelle pour un matériel donné est la première qui est rencontrée sur le routeur utilisé pour « sortir » du réseau. Par exemple la passerelle pour le portable 192.168.1.10 est 192.168.1.254

- En mode simulation, vérifier que toutes les machines peuvent désormais être atteintes depuis 192.168.1.10 avec la commande ping.

- Effectuer un traceroute (ligne de commande) de la machine 192.168.1.10 vers le portable 192.168.2.1. Noter le chemin parcouru par les paquets de données entre ces deux machines.

- Effectuer de même d’autres essais de traceroute de la machine 192.168.2.1 vers des machines du réseau 192.168.1.0

9) Effectuer un traceroute (ligne de commande) de la machine 192.168.2.1 vers la machine 192.168.2.2. Que constatez-vous ?

Sauvegarder le fichier `ReseauxAvecRouteur.fls`.

### On relie un réseau à un serveur

Sauvegarder le fichier précédent sous un autre nom, par exemple ReseauxAvecRouteurServeur.fl. Le modifier pour obtenir la configuration suivante:

![dhcp](./img/dhcp.png)

Compléter les configurations sachant que :

Réseau du serveur : 200.200.200.0  
Serveur : 200.200.200.200  
Masque 255.255.255.0  
Passerelle : 200.200.200.254

Tester des ping d’une machine du réseau 192.168.1.0 vers le serveur, et inversement.

## Le WEB et les échanges.
### Comment ajouter un serveur DNS ?

Dans cette section, nous allons ajouter un serveur DNS qui va traduire des noms de domaines en adresse IP.

![td3](./img/td3_res1.png)

- Nous voulons créer la configuration ci-dessus. En mode conception, ajouter l’ordinateur « tour » et essayer de le relier au routeur. Le message « Il n’y a plus de port disponible » apparaît.

Double-cliquer sur le routeur puis Configurer > Gérer les connections. En cliquant sur +, ajouter une troisième interface locale. Cliquer sur le bouton situé en bas Fermer (et pas sur la croix) et se rendre dans l’onglet correspondant pour lui attribuer l’adresse IP 192.168.0.254.

![connexions](./img/connexions.png)

- Relier l’ordinateur ajouté au routeur. Attribuer l’adresse IP 192.168.0.1 à cet ordinateur et n’oubliez pas de renseigner l’adresse de la passerelle.

- En mode simulation, vérifier avec quelque ping la bonne connexion entre les différentes machines.

- En mode simulation, ajouter un serveur DNS à ce nouvel ordinateur.


![dns](./img/dns.png)

- Configurer ce serveur DNS en cliquant sur « DNS Serveur DNS ».

![config_dns](./img/config_dns.png)

Dans le champ "Nom de domaine" ajouter le nom de domaine www.nsi.fr et dans le champ Adresse IP ajouter 192.168.2.2 (l’autre ordinateur « tour » de notre réseau qui sera notre serveur web). Cliquer sur « Ajouter ».

- Démarrer le serveur DNS.

- Configurer le champ DNS des différents ordinateurs portables en précisant l’adresse IP du serveur DNS créé.


### Comment ajouter un serveur web sur notre réseau ?

On veut maintenant héberger nos pages web sur un serveur de notre réseau. Ce serveur devra être accessible par toutes nos machines, via l’URL www.nsi.fr. Nous choisissons la machine 192.168.2.2 comme serveur.

Sur le serveur 192.168.2.2 :

- Enregistrer le précédent réseau, comprenant le serveur DNS, sous un autre nom (ex : ServeurWeb.fls)
- Passer en mode simulation et installer un serveur Web et un éditeur de texte sur la machine 192.168.2.2.


![inst_web](./img/inst_web.png)

- Démarrer le serveur web.

- A l’aide de l’éditeur de texte (Menu Fichier / Ouvrir), modifier le code HTML du fichier index.html dans le dossier webserver qui est la page retournée par défaut aux clients et ENREGISTRER la modification (avec Fichier puis enregistrer)

- En mode simulation, effectuer un ping www.nsi.fr à partir de différentes machines du réseau (sur lesquelles on aura installé la ligne de commande). Vers quel ordinateur vont-ils se connecter ?

- Si tout va bien, l’aventure se termine avec 0 paquet perdu !

Sur le client 192.168.1.10 :

- Installer un client Web (navigateur web) sur la machine 192.168.1.10.
- Démarrer le navigateur et saisir l’URL www.nsi.fr dans la barre d’adresse, pour envoyer une requête HTTP au serveur Web. La page d’accueil modifiée du serveur devrait s’afficher.

![page](./img/page.png)

### Observation des échanges

- Activer l’affichage des données sur la machine 192.168.1.10 avec un clic droit
- Au besoin, relancer la requête HTTP précédente (www.nsi.fr) à l’aide du navigateur puis analyser l’échange de données.

Vous devriez obtenir un échange équivalent à celui-ci-dessous.

Pour la suite des questions, on se servira des numéros de ligne de cette capture d’écran. Notre machine 192.168.1.10 a dans la simulation ci-dessous l’adresse IP 192.168.1.1

![echanges](./img/echanges.png)

10) A quoi servent les échanges lignes 1 et 2 (protocole ARP) ?
Cocher la ou les affirmations correctes

    ☐Récupérer l'@ MAC du routeur
    ☐Récupérer l'@ MAC du serveur DNS
    ☐Interroger le serveur DNS pour récupérer l'@ IP de nsi.fr
    ☐Afficher la page web NSI



11) A quoi servent les échanges lignes 3 et 4 ?
Cocher la ou les affirmations correctes

    ☐Interroger le serveur web nsi
    ☐Interroger le serveur DNS pour récupérer l'@ IP de nsi.fr
    ☐Afficher la page web NSI
    ☐Récupérer l'@ MAC du serveur DNS



On s'intéresse à la ligne 3 et plus particulièrement aux 4 couches du modèle TCP/IP qui forme la trame Ethernet suivante.
![encapsulation](./img/encaps.png)


12) En partant de la machine 192.168.1.1   
Dans quel sens s'encapsulent les données pour former la trame Ethernet ?
Cocher la ou les affirmations correctes:

    ☐Internet Réseau Transport Application
    ☐Application Transport Internet Réseau
    ☐Réseau Internet Transport Application
    ☐Réseau Transport Internet Application


13) Inscrire dans les cases le nom de la couche TCP/IP
![trame](./img/trame.png)

On peut représenter l’ouverture d’une connexion TCP par le schéma ci-dessous. 
![syn](./img/syn.png)

14) Retrouver les lignes correspondant à cette ouverture de connexion TCP

15) Quelles lignes envoient le fichier index.html que l'on a modifié sur le serveur NSI ?

## Protocole du bit alterné

Ce paragraphe a été réalisé par Gilles LASSUS

Ce protocole est un exemple simple de fiabilisation du transfert de données.

###  Contexte

- Alice veut envoyer à Bob un message M, qu'elle a prédécoupé en sous-messages M0, M1, M2,...
- Alice envoie ses sous-messages à une cadence Δt fixée (en pratique, les sous-messages partent quand leur acquittement a été reçu ou qu'on a attendu celui-ci trop longtemps : on parle alors de timeout)

### Situation idéale

![ideal](./img/ideale_copie.jpg)

Dans cette situation, les sous-messages arrivent tous à destination dans le bon ordre. La transmission est correcte.

### Situation réelle

Mais parfois, les choses ne se passent pas toujours aussi bien. Car si on maîtrise parfaitement le timing de l'envoi des sous-messages d'Alice, on ne sait pas combien de temps vont mettre ces sous-messages pour arriver, ni même (attention je vais passer dans un tunnel) s'ils ne vont pas être détruits en route.

![realite](./img/realite_copie.jpg)

Le sous-message M0 est arrivé après le M1, le message M2 n'est jamais arrivé...

Que faire ?

Écartons l'idée de numéroter les sous-messages, afin que Bob puisse remettre dans l'ordre les messages arrivés, ou même redemander spécifiquement des sous-messages perdus. C'est ce que réalise le protocole TCP (couche 4 — transport), c'est très efficace, mais cher en ressources. Essayons de trouver une solution plus basique.

### Solution naïve...

Pourquoi ne pas demander à Bob d'envoyer un signal pour dire à Alice qu'il vient bien de recevoir son sous-message ? Nous appelerons ce signal ACK (comme acknowledgement, traduisible par «accusé de réception»). Ce signal ACK permettra à Alice de renvoyer un message qu'elle considérera comme perdu :

N'ayant pas reçu le ACK consécutif à son message M1, Alice suppose (avec raison) que ce message n'est pas parvenu jusqu'à Bob, et donc renvoie le message M1.

### Mais peu efficace...

![conv](./img/naivebad_copie.jpg)

Le deuxième ACK de Bob a mis trop de temps pour arriver (ou s'est perdu en route) et donc Alice a supposé que son sous-message M1 n'était pas arrivé. Elle l'a donc renvoyé, et Bob se retrouve avec deux fois le sous-message M1. La transmission est incorrecte. En faisant transiter un message entre Bob et Alice, nous multiplions par 2 la probabilité que des problèmes techniques de transmission interviennent. Et pour l'instant rien ne nous permet de les détecter.

### Bob prend le contrôle

Bob va maintenant intégrer une méthode de validation du sous-message reçu. Il pourra décider de le garder ou de l'écarter. Le but est d'éviter les doublons.

Pour réaliser ceci, Alice va rajouter à chacun de ses sous-messages un bit de contrôle, que nous appelerons FLAG (drapeau). Au départ, ce FLAG vaut 0. Quand Bob reçoit un FLAG, il renvoie un ACK égal au FLAG reçu.

Alice va attendre ce ACK contenant le même bit que son dernier FLAG envoyé :

- tant qu'elle ne l'aura pas reçu, elle continuera à envoyer le même sous-message, avec le même FLAG.
- dès qu'elle l'a reçu, elle peut envoyer un nouveau sous-message en inversant («alternant») le bit de son dernier FLAG (d'où le nom de ce protocole).

Bob, de son côté, va contrôler la validité de ce qu'il reçoit : il ne gardera que les sous-messages dont le FLAG est égal à l'inverse de son dernier ACK. C'est cette méthode qui lui permettra d'écarter les doublons.

Observons ce protocole dans plusieurs cas :
#### Cas où le sous-message est perdu

![alt2](./img/alt2_copie.jpg)

#### Cas où le ACK est perdu

![alt1](./img/alt1_copie.jpg)

Le protocole a bien détecté le doublon du sous-message M1.

#### Cas où un sous-message est en retard

![alt3](./img/alt3_copie.jpg)

Le protocole a bien détecté le doublon du sous-message M1... mais que se passerait-il si notre premier sous-message M1 était encore plus en retard ?

### Conclusion

Le protocole du bit alterné a longtemps été utilisé au sein de la couche 2 du modèle OSI (distribution des trames Ethernet). Simple et léger, il peut toutefois être mis en défaut, ce qui explique qu'il ait été remplacé par des protocoles plus performants.

## Interconnexion de deux réseaux

Rappel:  
Les « routeurs » sont aussi nommés « passerelles » ou « gateway ».


### Interconnexion de deux réseaux.

On donne le réseau ci-dessous :

⚠️ Ne pas lancer de simulation avec le logiciel Filius avant d’avoir complété les questions a), b) et c)

![deux](./img/deux_res.png)

Pour chaque réseau, on choisit :

Pour les adresses IP des routeurs : les dernières possibles.  
Pour l’adresse IP du serveur DHCP : la dernière possible, une fois celle des routeurs attribuées.

Compléter les adresses IP ci-dessous

14) Pour le réseau 192.168.1.0

Passerelle :  
Serveur DHCP :  

15) Pour le réseau 10.0.0.0

Passerelle « Routeur 0 » :  
Passerelle « Routeur 1 » :  

16) Pour le réseau 192.168.2.0

Passerelle :  
Serveur DHCP :  

Construire le réseau ci-dessus, et configurer tous les équipements. (Utiliser le DHCP) Pour les routeurs, dans l’onglet général, il ne faut pas cocher « routage automatique »

17) Vérifier avec des ping, la connexion entre :

deux postes du réseau 192.168.1.0  
deux postes du réseau 192.168.2.0  
un poste du réseau 192.168.1.0, et un poste du réseau 192.168.2.0 . Que constatez-vous ?


#### Table de routage

A chaque routeur, il faut indiquer l’adresse des réseaux distants (réseaux non reliés au routeur), et celle de la passerelle : la première adresse IP du routeur (entrée) qu’il faudra choisir. L'interface est l'adresse IP par laquelle on sort du routeur pour aller vers le réseau distant.


18) Compléter ci-dessous pour le routeur 0:
|Réseau de destination |	Masque |	Passerelle |	Via l’interface |
|----------------------|-----------|---------------|--------------------|
|192.168.2.0 |	255.255.255.0 | | |	


19) Compléter ci-dessous pour le routeur 1:
|Réseau de destination |	Masque |	Passerelle |	Via l’interface |
|----------------------|-----------|---------------|--------------------|
|192.168.1.0 |	255.255.255.0 | | |	

En mode conception, compléter les tables de routage de chaque routeur. Dans l’onglet Général, la case « routage automatique » doit être décochée. Dans l’onglet « table de routage », observez les lignes déjà remplies. Il n’est pas possible de les modifier. Vous pourrez par la suite décocher « Afficher toutes les lignes ».
Remarque

> Pour la première fois nous avons utilisé l’adresse des réseaux.

Vérifier avec des pings la connexion entre un poste du réseau 192.168.1.0, et un poste du réseau 192.168.2.0. La mise à jour de la table de routage est parfois lente.

### Interconnexion de quatre réseaux.

Enregistrer sous un autre nom le fichier du I. , puis le modifier pour obtenir le réseau suivant. Procéder de manière analogue à celle utilisée au I. Configurer tous les matériels, puis vérifier avec des pings.

Commencer par compléter ci-dessous avant de créer le projet.

![quatre](./img/quatre_res.png)

20) Compléter ci-dessous pour le réseau 192.168.1.0

Passerelle « Routeur 0 » :  
Serveur DHCP :
 
21) Compléter ci-dessous pour le réseau 10.0.0.0

Passerelle « Routeur 0 » :  
Passerelle « Routeur 2 » :


22) Compléter ci-dessous pour le réseau 172.16.0.0

Passerelle « Routeur 2 » :  
Passerelle « Routeur 1 » :


23) Compléter ci-dessous pour le réseau 192.168.2.0

Passerelle « Routeur 1 » :  
Serveur DHCP :


24) Compléter ci-dessous pour le routeur 0 :
|Réseau de destination |	Masque |	Passerelle |	Via l’interface |
|----------------------|-----------|---------------|--------------------|
|192.168.2.0 |	255.255.255.0 | | |	
|172.16.0.0  |	255.255.0.0  | | |

25) Compléter ci-dessous pour le routeur 1 :
|Réseau de destination |	Masque |	Passerelle |	Via l’interface |
|----------------------|-----------|---------------|--------------------|
|192.168.1.0 |	255.255.255.0 | | |		
|10.0.0.0 |	255.0.0.0 | | |	
			
		
26) Compléter ci-dessous pour le routeur 2 :
|Réseau de destination |	Masque |	Passerelle |	Via l’interface |
|----------------------|-----------|---------------|--------------------|
|192.168.1.0 |	255.255.255.0 | | | 		
|192.168.2.0 |	255.255.255.0 | | |		