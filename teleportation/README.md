# Teleportation

L'une des corvées agricoles que John le fermier déteste le plus est le 
transport massif de fumier. Afin de se faciliter la tâche, il a inventé
un objet génial : le téléporteur de fumier ! Au lieu de transporter le fumier
entre deux points dans un chariot attaché à son tracteur, il peut utiliser le
téléporteur pour transporter instantanément du fumier d'un endroit à un autre.

La ferme de John le fermier est située à côté d'une unique longue route, de
telle sorte que chaque endroit de sa ferme peut être décrit simplement par sa
position sur la route (c'est-à-dire par un nombre). Un téléporteur est décrit
par deux nombres x et y, le fumier apporté en position x pouvant être
instantanément transporté en position y, et réciproquement.

John le fermier veut transporter du fumier depuis la position a jusqu'à la
position b, et il a construit un téléporteur qui pourra lui être utile (bien
sûr, il n'a pas besoin d'utiliser le téléporteur si cela ne l'aide pas).
Veuillez l'aider à déterminer la distance minimale sur laquelle il a besoin de
transporter le fumier en utilisant son tracteur.

## FORMAT D'ENTRÉE

La première et seule ligne de l'entrée contient quatre entiers séparés par des
espaces : a et b, décrivant les positions de début et de fin, suivis par x et
y, décrivant le téléporteur. Ces positions sont comprises entre 0 et 100 et ne
sont pas forcément distinctes.

## FORMAT DE SORTIE (fichier

Afficher un unique entier donnant la distance minimale sur laquelle John le
fermier doit utiliser son tracteur.

## EXEMPLE D'ENTRÉE

```
3 10 8 2
```

## EXEMPLE DE SORTIE

```
3
```

Dans cet exemple, la meilleure stratégie est de transporter le fumier depuis
la position 3 jusqu'à la position 2, le téléporter jusqu'à la position 8, puis
le transporter jusqu'à la position 10. La distance totale nécessitant le
tracteur est donc 1 + 2 = 3.

Auteur du sujet : Brian Dean 
