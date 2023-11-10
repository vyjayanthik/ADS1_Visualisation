# -*- coding: utf-8 -*-
"""
Created on Thu Nov  9 20:32:05 2023

@author: kvyja
"""

import pandas as pd  # Inputing file (eg, pd.read_csv), Data-processing
import matplotlib.pyplot as plt  # Visualisation

# Reading the dataset by dataframe as 'df':
df = pd.read_csv("export.csv", index_col=0)  # Reading the file

# Generates lineplot for Dataframe


def linePlot(linePlotData):
    '''Creating a line plot to visualize trends over the years for countries 
       including China, Malaysia, Thailand, Fiji, Indonesia, and Palau. 
       Using circular markers ('o') for data points. Plot size is set to 10x4.'''
    linePlotData.plot(x='Years', y=['China', 'Malaysia', 'Thailand',
                                    'Fiji', 'Indonesia', 'Palau'],
                      kind='line', figsize=(10, 4), marker='o')

# Set title and labels
    plt.title('Exports of Goods and Services')
    plt.xlabel('Years')
    plt.ylabel('Export rate')
    plt.legend()
    plt.show()


# Generates barplot for Dataframe

def barPlot(barData):
    '''Creating a bar plot to compare the export rates of China, Thailand
    and Indonesia over the years. The plot is titled 'Comparison of China and
    Thailand Export Rate' with labeled x and y axes. Bar colors are set to 
    orange for China, green for Thailand, and blue for Indonesia. Legend is 
    enabled, and the bar width is adjusted to 0.45 for better visibility.'''
    barData.plot(x='Years', y=['China', 'Thailand', 'Indonesia'], kind='bar',
                 title='Comparison of China and Thailand Export Rate',
                 xlabel='Years', ylabel='Export rate',
                 color=('orange', 'green', 'blue'), legend=True, width=0.45)
    plt.figure(figsize=(10, 5))  # Setting up a new figure with a size of 10x5
    plt.show()


'''Defining a function scatterPlot to generate a scatter plot with 
specifieddata, x and y features,title,x and y axis labels,and marker position.'''


def scatterPlot(data, x_feature, y_feature, title, x_label, y_label, position):
    ax = plt.subplot(2, 3, position)
    data.plot(x=x_feature, y=y_feature, kind='scatter', ax=ax, marker='o',
              figsize=(10, 5))

# Set title and labels
    plt.title(title)
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.tight_layout()  # To adjust the space between subplots


# Selecting the valuable rows because last 5 rows are nugatory
df = df.iloc[:-5]

# Droping the unwanted columns from the dataset:
df1 = df.drop(['Country Code', 'Series Code', 'Series Name'], axis=1)


# Renaming the column into relevant way:
def extract_years(column):
    return column.split(' ')[0]


df1.columns = df1.columns.to_series().apply(extract_years)
df1.head()

# Transpoing the dataframe to access the country as column variable:
df1_trans = df1.transpose()

# Resetting the index and dropping the original index
df2 = df1_trans.reset_index(drop=True)

# Adding a column of 'Years' to the dataframe:
year = pd.Series([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021],
                 dtype=object)
df2['Years'] = year

# df_final is a new DataFrame where the last column is moved to the first one
df_final = pd.concat([df2.iloc[:, -1:], df2.iloc[:, :-1]], axis=1)


'''Creating a new DataFrame 'df_new' by selecting all rows and
 columns from the second column onward (index 1 and onwards) from 
 the original DataFrame 'df_final'.'''
df_new = df_final.iloc[:, 1:]

'''Visualising the lineplot '''
linePlot(df_final)

'''Visualising the barplot'''
barPlot(df_final)


'''Generating scatter plots for export rates of different countries over the
 years using the 'scatterPlot' function. Each subplot corresponds to a 
 specific country, with labels and positions specified accordingly.'''

scatterPlot(df_final, 'Years', 'China', 'China', 'years', 'Export rate', 1)
scatterPlot(df_final, 'Years', 'Malaysia',
            'Malaysia', 'years', 'Export rate', 2)
scatterPlot(df_final, 'Years', 'Thailand',
            'Thailand', 'years', 'Export rate', 3)
scatterPlot(df_final, 'Years', 'Fiji', 'Fiji', 'years', 'Export rate', 4)
scatterPlot(df_final, 'Years', 'Indonesia',
            'Indonesia', 'years', 'Export rate', 5)
scatterPlot(df_final, 'Years', 'Palau', 'Palau', 'years', 'Export rate', 6)
