## Qu’est-ce que le DOM ?

Le **DOM (Document Object Model)** est une représentation **en forme d’arbre** d’une page HTML.

Quand le navigateur charge une page web, il transforme le code HTML en une structure hiérarchique composée de **nœuds** :

* Le document (racine)
* Les balises HTML (`<html>`, `<body>`, `<div>`, etc.)
* Le texte
* Les attributs

Chaque élément devient un **nœud** relié aux autres (parent, enfant, frère).

---

## Visualisation d’un arbre DOM

![Image](https://www.w3schools.com/js/pic_htmltree.gif)

![Image](https://www.tutorialspoint.com/html/images/html_dom.jpg)

![Image](https://upload.wikimedia.org/wikipedia/commons/5/5a/DOM-model.svg)

Exemple de code HTML :

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Ma page</title>
  </head>
  <body>
    <h1>Bienvenue</h1>
    <p>Bonjour tout le monde</p>
  </body>
</html>
```

Structure DOM simplifiée :

```
Document
 └── html
      ├── head
      │    └── title
      └── body
           ├── h1
           └── p
```

---

## Notions importantes

### Parent

Un élément qui contient un autre élément.

### Enfant

Un élément contenu dans un autre.

### Frères (siblings)

Deux éléments ayant le même parent.

### Nœud racine

C’est l’objet `document`.

---

# Exercices

---

## Exercice 1 – Comprendre la structure

Observe ce code :

```html
<body>
  <div>
    <h2>Titre</h2>
    <p>Texte 1</p>
    <p>Texte 2</p>
  </div>
</body>
```

### Questions :

1. Quel est le parent de `<h2>` ?
2. Combien d’enfants possède `<div>` ?
3. Les deux `<p>` sont-ils frères ?
4. Quel est le parent direct du `<div>` ?

---

## Exercice 2 – Dessiner l’arbre DOM

Dessine l’arbre DOM correspondant à :

```html
<ul>
  <li>Pomme</li>
  <li>Banane</li>
  <li>Orange</li>
</ul>
```

---

## Exercice 3 – Manipulation en JavaScript

Soit le HTML :

```html
<p id="message">Bonjour</p>
```

### Questions :

1. Quelle instruction JavaScript permet de sélectionner le paragraphe ?
2. Comment modifier son texte en "Bonsoir" ?
3. Comment changer sa couleur en rouge ?

---

## Exercice 4 – Relations entre éléments

Avec le code :

```html
<section>
  <article>
    <h3>Titre article</h3>
  </article>
</section>
```

1. Quel est le parent de `<article>` ?
2. Quel est l’enfant de `<article>` ?
3. `<section>` est-il ancêtre de `<h3>` ?

---

# Exercices Bonus (niveau avancé)

## Exercice 5 – Parcours du DOM

Explique la différence entre :

* `parentNode`
* `children`
* `firstElementChild`
* `nextElementSibling`

---

## Exercice 6 – Ajout d’élément

Écris un script JavaScript qui :

1. Crée un nouvel élément `<li>`
2. Lui ajoute le texte "Fraise"
3. L’ajoute dans une liste `<ul>`