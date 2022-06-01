
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


## General Information
This project 

Ce projet a été créé pour permettre de partager facilement les scripts de fonctions utilisées dans les projets clients Fastercom. 

Un autres buts étaient de permettre de tester ces fonctions.
C'est possible en roulant runTests.js. Vous serez en mesure de voir le résultat de tous les tests dans la console.

Pour les devs, vous pourrez écrire des tests pour chaque script de fonction selon un modèle précis. 


## Technologies
This project is created with : 

* Node version : 16.15.0
* NPM version : 8.5.5
* JS : ES2020 

## Standard de nomanclature & PLACEMENT FICHIER

Vous trouverez les fichiers scripts divisés en dossier nommé par type de fonctions.  

Chaque fichier continient un script enregistré sous le format .txt

Placer un courts summary de la fonction au début des fichiers .txt


```
// summary : To get a clear summary of items when you have item's name and quantity

let array = [];

for (let item of (docData['Sièges'] || [] )) {
    if (item['Sièges|2|Quantité'] && item['Sièges|1|Siège']){
        array.push(item['Sièges|2|Quantité'] +' '+ item['Sièges|1|Siège'].substring(3));
    }
}
return docData['Sièges'] ? { 'SiegeRésumé' : array.join('\n') } : undefined

```



test/ Tests
même nom scripts Js
dossier

## Scripts functions

- Emplacement de script function dans ordi : path 
- comment ils sont classés
- comment utiliser l'interface
- nommage : comment nommer et où placer le texte


## Setup test interface
To run testing interface, you need to install node and npm on your computer.

To launch a test, you need to run runTests.js

```
$ node runTests.js 
```
<!-- To launch a test, install it locally using npm: À MODIFIER -->


## How to write a test
Pour les devs, vous pourrez écrire des tests pour chaque script de fonction selon un modèle précis. 


## Code Examples


## Project status 
This project is in progress 
