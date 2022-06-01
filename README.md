# FasterWeb functions and testing interface
> In this project, you will find a repository for FasterWeb functions scripts and a testing interface.

## Table of Contents
* [General info](#general-info)
* [Functions script]()
* [Technologies](#technologies)
* [Setup test interface](#setup)


## General Info

The purpose of this project is to be able to easily **share the script functions** used in Fastercom's client projects. 

It's also possible to test all the functions or a precise one when you launch **runTests.js**. 
You will see the results of each test in the terminal. 

Each test needs to be written following a precise pattern and configuration.

## Script functions
### location

All the script files are listed under folders named by function type (autofill, autohide, search, dev)

```
scripts / autofill
        / autohide 
        / search
```


### Configuration of script files

- Script files use the extension .txt

- There's one script in each file

- Name of the file is written in camelCase

- There's a summary of the script at the beginning of each .txt file :

```
// To get a clear summary of items when you have item's name and quantity

let array = [];

[...]
```


## Test interface

Each script can be tested while running runTests.js. 

- Be sure that your .txt and .js files are in the **right folder** to run a test.
- It is also essential to use the **same name** for these 2 files.

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

**Important**: The js file will be written following the EayTest.js model in the /dev folder.


### Technologies
This project is created with : 

* Node version : 16.15.0
* NPM version : 8.5.5
* JavaScript : ES2020 


### Setup test interface
To run the testing interface, you need to install [Node](https://nodejs.org/en/download/) on your computer.


To launch a test, you need to run **runTests.js** from the FWfunctions folder

```
$ node runTests.js 

```

## How to write a test U+1F916	


Pour les devs, il est nécessaire de suivre un modèle précis pour écrire un test.

modèle EasyTest : classe 
    changer type et classNameString

### nommanclature 
test/ Tests
même nom scripts Js


### Code Examples
parler des tests individuels : Avons-nous besoin de données d'entrée ? Si oui, sous quel format ?

### Project status 
This project is in progress 
