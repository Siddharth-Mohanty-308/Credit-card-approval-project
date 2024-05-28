![banner](readme_assets/banner.png)

![Python version](https://img.shields.io/badge/Python%20version-3.10%2B-lightgrey)
![GitHub repo size](https://img.shields.io/github/repo-size/Siddharth-Mohanty-308/Credit-card-approval-project)
![Type of ML](https://img.shields.io/badge/Type%20of%20ML-Binary%20Classification-red)

Badge [source](https://shields.io/)

## Authors

- [@siddharth](https://github.com/Siddharth-Mohanty-308)

## Table of content

- [Problem Statement](#Problem-Statement)
- [Data Scource](#Data-Scource)
- [Methods](#Methods)
- [Tech Stack](#Tech-Stack)
- [Graphs and Results]()  

## Problem Statement

## Data Source

[dataset_link](https://www.kaggle.com/datasets/keitazoumana/aercreditcard)

## Process

- Data Cleaning and Transfomation
- Model Training and Evaluation
- Building UI
- Model Deployment using Flask

## Data Cleaning and Transfomation
# Add heatmap

- AER_credit_card_data is first cleaned for training the decision tree model. The dataset has 12 columns ('card','reports','age','income,'share','expenditure','owner','selfemp','dependents','months','majorcards','active').
- I dropped 'share' and 'majorcards' columns as there was not any information regarding those columns on kaggle. 'card' is the label column and all the remaining ones are features. 
- There were no NULL values or duplicate columns found in the dataset
- Column names are updated as follows
  # Add table
- All values in 'age' column are updated to int and 'yearly_income' is multiplied by 10000 to get the actual values. As I am going to use a decision tree scaling is not required
- I map the values of categorical columns ('card','owner_of_house','selfemp') to 0 and 1

## Model Training and Evaluation
