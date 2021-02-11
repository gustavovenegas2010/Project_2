#!/usr/bin/env python
# coding: utf-8

# # ETL Pipeline
# 
# In this code you will find the ETL pipeline process (extract, transform and load)

# ## 1. load libraries
# 
# load the necessary libraries to execute the codes of the following parts

# In[ ]:


import requests
import sys
import numpy as np
import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from sqlalchemy import create_engine


# ## 2. Extract data
# 
# Extracts the database and its outputs are the dependent and independent variables and the key.

# In[ ]:


def load_data(messages_filepath, categories_filepath):
    '''
    INPUT 
        database_filepath 
    OUTPUT
        Returns the following variables:
        X - Returns the input features (messages)
        Y - Returns the categories of the dataset.  This will be used for classification based off of the input X
        y.keys - Just returning the columns of the Y columns
    '''
    messages = pd.read_csv(messages_filepath)
    categories = pd.read_csv(categories_filepath)
    df = pd.merge(messages, categories)
    df_temp_id = df['id']
    return df, df_temp_id


# ## 3. Clean Data
# 
# Clean the Dataframe from the previous step, the common identifier is used and the output is the set of clean variables.

# In[ ]:


def clean_data(df, df_temp_id):
    '''
    INPUT 
        df: Dataframe to be cleaned by the method
        df_temp_id: the id that is to be used when merging the messages and classifications together based off of the common id
    OUTPUT
        df: Returns a cleaned dataframe Returns the following variables:
    '''
    categories =  df['categories'].str.split(';', expand=True).add_prefix('categories_')
    messages = df[['message', 'genre', 'id']]
    row = categories.iloc[0]
    category_colnames = list()
    for x in row:
        #print(x[0:-2])
        category_colnames.append(x[0:-2])
    categories.columns = category_colnames
    categories.related.loc[categories.related == 'related-2'] = 'related-1'
    for column in categories:
        # set each value to be the last character of the string
        categories[column] =  categories[column].str[-1]
        # convert column from string to numeric
        categories[column] = categories[column].astype(int)
    
    
    # drop the original categories column from `df`
    df.drop(['categories'], axis=1, inplace = True)
    # concatenate the original dataframe with the new `categories` dataframe
    categories['id'] = df['id']

    df = pd.merge(messages, categories)
    # check number of duplicates
    print(df.duplicated().sum())
    # drop duplicates
    
    df.drop_duplicates(inplace = True)
    # check number of duplicates
    print(df.duplicated().sum())
    return df


# ## 4. Load
# 
# In the following code save the clean dataframe in SQLite

# In[ ]:


def save_data(df, database_filename):
    '''
    INPUT 
        df: Dataframe to be saved
        database_filepath - Filepath used for saving the database     
    OUTPUT
        Saves the database
    '''
    engine = create_engine('sqlite:///data//DisasterResponse.db')
    df.to_sql('DisasterResponse', engine, index=False, if_exists='replace')


# In[ ]:


def main():
    if len(sys.argv) == 4:

        messages_filepath, categories_filepath, database_filepath = sys.argv[1:]

        print('Loading data...\n    MESSAGES: {}\n    CATEGORIES: {}'
              .format(messages_filepath, categories_filepath))
        df, df_temp_index = load_data(messages_filepath, categories_filepath)

        print('Cleaning data...')
        df = clean_data(df, df_temp_index)
        
        print('Saving data...\n    DATABASE: {}'.format(database_filepath))
        save_data(df, database_filepath)
        
        print('Cleaned data saved to database!')
    
    else:
        print('Please provide the filepaths of the messages and categories '              'datasets as the first and second argument respectively, as '              'well as the filepath of the database to save the cleaned data '              'to as the third argument. \n\nExample: python process_data.py '              'disaster_messages.csv disaster_categories.csv '              'DisasterResponse.db')


if __name__ == '__main__':
    main()

