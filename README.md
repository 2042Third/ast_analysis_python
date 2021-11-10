# AST Analysis of Python

This project mines a large Python repository and extract statistics using various methods.

## Table of Contents
  * [Introduction](#introduction)
  
  * [Mining](#mining)
  * [Requirements](#requirements)
  * [Download Results](#download-results)

## Introduction

The begining of this project aimed to analyze a randomly sorted large repository of Python programs to see the uses of dynamic features (`eval()`,`getattr()` and so on). Later the project extended to also include functional features (`lambda()`,`yield()` and so on) and decorators (`@property`,`@classmethod` and so on). Uses of some features like `eval` directly disables Python run-time to optimize a program. At the same time, there are many languages, such as `c/c++` and even `Javascript`, that can do the same while still having the capability for more optimization.  Using the AST library in Python3, enables us to mine millions of programs written in Python. 


## Mining Program


In the root folder of this project input command
```
./run.sh
```
Then input the folder name 
to start the mining.
The result will be written a file named "ast_analysis_data.csv" in the root folder.

### Load into SQL
The provided sql script "ast_analysis.sql" will load the result into a database called "astmine" in table "output".
Some query script are provided in the file "sql_scripts.sql"

## Requirements

- python3
- Unix Environment
- numpy(ml, diagram)
- matplot(diagram)
- panda(ml)
- scikit-learn(ml)
- squarify(treemap)
- c++ boost(json reader)

## Download Results

<a href="https://pdm.pw/mine/downloads/" target="_blank" rel="noopener noreferrer">list of all data used</a>


