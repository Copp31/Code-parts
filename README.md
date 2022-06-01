
Launch
runTests.js
test.js test.txt
parler des tests individuels : Avons-nous besoin de données d'entrée ? Si oui, sous quel format ?


# FasterWeb functions repository and testing interface
> In this project, you will find repository for FasterWeb functions scripts and a testing interface.

## Table of Contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup test interface](#setup)


## General Info

Ce projet a été créé pour permettre de partager facilement les scripts de fonctions utilisés dans les projets clients Fastercom. 

Il est aussi possible de tester les fonctions en roulant runTests.js. Vous serez en mesure de voir le résultat de tous les tests dans la console.

Pour les devs, vous pourrez écrire des tests pour chaque script de fonction selon un modèle précis. 


## Scripts functions
### Emplacement des scripts 
Vous trouverez les fichiers scripts répertorié sous des dossiers nommés par type de fonctions (autofill, autohide, search).
```
scripts / autofill
        / autohide 
        / search
```

### Caractéristique des fichier scripts
- Les scripts sont en format .txt 

- Chaque fichier contient un script

- Le nom doit être clair et en camelCase

- Écrire un court résumé de la fonction en //commentaire au début  chaque fichiers .txt

```
// To get a clear summary of items when you have item's name and quantity

let array = [];

[...]
```


## Les tests 

Chaque fonction.txt peut être testé grâce à l'interface de terminal runTests.js.

Pour qu'un test fonctionne, il est important d'avoir un fichier.js dans un dossier miroir à celui des scripts. 
        L'emplacement et le nom doivent être identique :
```
scripts / autofill
            /test.txt
        / autohide 
        / search

tests   / autofill
            /test.js
        / autohide 
        / search
```

Important : le fichier.js doit être écrit selon le modèle EasyTest.js se trouvant dans le dossier /dev.


### Technologies
This project is created with : 

* Node version : 16.15.0
* NPM version : 8.5.5
* JavaScript : ES2020 


### Setup test interface
To run testing interface, you need to install [Node](https://nodejs.org/en/download/) on your computer.


To launch a test, you need to run **runTests.js**

```
$ node runTests.js 
```

## How to write a test
Pour les devs, il est nécessaire de suivre un modèle précis pour écrire un test.

modèle EasyTest : classe 
    changer type et classNameString

### nommanclature 
test/ Tests
même nom scripts Js


### Code Examples


### Project status 
This project is in progress 
