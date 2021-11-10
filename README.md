# AST Analysis of Python

This project mines a large Python repository and extract statistics using various methods.

## Table of Contents
  * [Introduction](#introduction)
  * [Methods](#methods)
    * [Data](#data)
    * [Mining](#mining)
    * [Analysis](#analysis)
      * [Overall](#overall)
      * [Relationship Between Features](#relationship-between-features)
      * [Dynamic Feature](#dynamic-feature)
  * [Results](#results)
  * [Requirements](#requirements)
  * [Download Results](#download-results)

## Introduction

The begining of this project aimed to analyze a randomly sorted large repository of Python programs to see the uses of dynamic features (`eval()`,`getattr()` and so on). Later the project extended to also include functional features (`lambda()`,`yield()` and so on) and decorators (`@property`,`@classmethod` and so on). Uses of some features like `eval` directly disables Python run-time to optimize a program. At the same time, there are many languages, such as `c/c++` and even `Javascript`, that can do the same while still having the capability for more optimization.  Using the AST library in Python3, enables us to mine millions of programs written in Python. 
The analysis is on Dynamic features, functional features, and decorators of Python programs.


## Methods

We aquired around 1.3 million python files from Github. 

### Data

A bash script that goes through the Github repository downloads the files satisfying `has .py extension`, `is not sorted`, and `is public`.
(to be continued...)

### Mining Program


In the root folder of this project input command
```
./run.sh
```
Then input the folder name to start the mining.
The result will be written a file named "ast_analysis_data.csv" in the root folder.

### Load into SQL

The provided sql script "ast_analysis.sql" will load the result into a database called "astmine" in table "output".
Some query script are provided in the file "sql_scripts.sql".

### Analysis

We use SQL, Python, and Excel to analyze and present the data. Few questions we aim to answer include: What percentage of Python programs have used Dynamic features? Are the dynamic features need for the given tasks, or can they be replaced by static methods? For a given organization, is the use of decorators/dynamic/functional features increase the probability of using one of the features again?
Four AI models are choosen to generate and study the data. 

#### Overall

The initial theory is that most/larger proportions of programers would not use dynamic/functional/decorators in their programs. In those programs that do use one of them, there is a greater probability that they would use one other features out of the three.
The result will be presented with diagrams and tables.

#### Relationship Between The Features

In our initial analysis, it seems to be a corelation between the features. AI models may disqualify or verify our theory by the giving the prediction probability number. If the given probability on a prediction supports our theory, then we can conclude that there is a strong corelation between the features presented.
We define this number as:
"Given an organization have used one of f, d, or c; there is x probability that the organization would use another feature out of the three." 

#### Dynamic Features

Another goal of our study is to see whether most programers' uses of Python Dynamic features are justified. Our theory is most uses of dynamic features in Python can be replaced with static ones in reasonable amount of rewrite. 
We randomly choose 40 programs in the repository and read the source code to determine if they are nessesarry or not. If a large proportion of the source code shows that they are not nessesarry, it proves our theory is correct. Otherwise, our theory is not correct.  

## Results

### Overall 


<img src="./diagrams/overall_proportions.png" alt="Drawing" />

Out of 1,385,873 files, 

feature | count | %
-- | -- | --
none | 912,878 | 65.8%
func | 213,313 | 15.4%
dec | 96,178 | 6.9%
dyn | 50,185 | 3.6%
func & dec | 49,837 | 3.6%
func & dyn | 32,484 | 2.3%
func & dyn & dec | 16,918 | 1.2%
dyn & dec | 13,080 | 0.9%

<img src="./diagrams/organization/index.png" alt="Drawing" /> 
<img src="./diagrams/project/index.png" alt="Drawing" /> 

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


