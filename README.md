# Disaster Response Pipeline Project 2

## 1. Project Motivation

This project is part of the second project of the Data science course at Udacity. I have applied knowledge of data engineering, natural language processing and machine learning to analyze data from the messages people send during disasters in order to build a model for an API to classify disaster messages. It is a project that will have a social focus, which makes it a very meaningful project for society.

## 2. File Description
* app:

    + run.py: Flask file to run the web application.
    + templates contains html file for the web applicatin.
* data:
    + disaster_categories.csv: dataset including all the categories.
    + disaster_messages.csv: dataset including all the messages.
    + process_data.py: ETL pipeline scripts to read, clean, and save data into a database.
* models:
    + ML_Pipeline_Preparation.ipynb: Jupyter Notebook, tokenize messages from clean data and create new columns through feature engineering. The data with new features are trained with a ML pipeline and pickled.
    + train_classifier.py: Script to tokenize messages from clean data and create new columns through feature engineering. The data with new features are trained with a ML pipeline and pickled.

## 3. Instructions
Run the following commands in the project's root directory to set up your database and model.

To run ETL pipeline that cleans data and stores in database python data/process_data.py data/disaster_messages.csv data/disaster_categories.csv data/DisasterResponse.db
To run ML pipeline that trains classifier and saves python models/train_classifier.py data/DisasterResponse.db models/classifier.pkl
Run the following command in the app's directory to run your web app. python run.py

Go to http://0.0.0.0:3001/

## 4. Author and Acknowledgements
The author of this project is Gustavo Venegas Segura, Statistician with a specialization in statistics from the National University of Colombia, currently working at Banco Davivienda. Special thanks to Jorge Andrés Escobar and Udacity for their help in this project.
