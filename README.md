# FasterWeb functions and testing interface :computer:
> In this project, you will find a repository for FasterWeb script functions and a testing interface.

## Table of Contents
* [General info](#general-info)
* [Functions script]()
* [Technologies](#technologies)
* [Setup test interface](#setup)


## General Info

The purpose of this project is to be able to easily **share the script functions** used in Fastercom's client projects. 

It's also possible to test all the functions or a precise one when you launch **runTests.js** from the Command-line interface.
You will see the results of each test in the terminal. 

Each test needs to be written following a precise pattern and configuration.

## Script functions :memo:
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


## Testing interface :chart_with_upwards_trend:

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


### Command-line interface

To run the testing interface, you need to install [Node](https://nodejs.org/en/download/) on your computer.

To launch tests, you have to run **runTests.js** from the FWfunctions folder.


```
$ node runTests.js 
```

You should see this in your terminal : 

```
--------------- tests interface ---------------

1. Run all tests from all functions
2. Run all tests from one specific function
3. Exit test module


What do you want to test (1, 2, 3)? 
```

If you want to run all tests from one specific function, you will be asked the function type (autofill, autohide, search, dev) and the function name:

```
Write Function Type : dev
Write function name : EasyName
```


## Write a test 

If you write a test, it's necessary to follow the scripts/dev/EasyTest.js model.

The function **type** needs to be a string and the same name as the folder. It's essential because the path is related to it.

The **classNameString** is the name of your .txt and .js file. The class name also need to be the same. 

```
let type = *"dev"*;
let classNameString = *"EasyTest"*;
let scriptPath = `./scripts/${type}/${classNameString}.txt`; 

class *EasyTest* {
  constructor(type, classNameString, scriptPath) {
```

As you can see, each function has its class. In this class, you will find every test for a single script. 





### nommanclature 
test/ Tests
même nom scripts Js


### Code Examples
parler des tests individuels : Avons-nous besoin de données d'entrée ? Si oui, sous quel format ?

### Project status 
This project is in progress 
