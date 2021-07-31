#!/usr/bin/env python
# coding: utf-8

# # Springboard Data Science Career Track Unit 4 Challenge - Tier 3 Complete
# 
# ## Objectives
# Hey! Great job getting through those challenging DataCamp courses. You're learning a lot in a short span of time. 
# 
# In this notebook, you're going to apply the skills you've been learning, bridging the gap between the controlled environment of DataCamp and the *slightly* messier work that data scientists do with actual datasets!
# 
# Here’s the mystery we’re going to solve: ***which boroughs of London have seen the greatest increase in housing prices, on average, over the last two decades?***
# 
# 
# A borough is just a fancy word for district. You may be familiar with the five boroughs of New York… well, there are 32 boroughs within Greater London [(here's some info for the curious)](https://en.wikipedia.org/wiki/London_boroughs). Some of them are more desirable areas to live in, and the data will reflect that with a greater rise in housing prices.
# 
# ***This is the Tier 3 notebook, which means it's not filled in at all: we'll just give you the skeleton of a project, the brief and the data. It's up to you to play around with it and see what you can find out! Good luck! If you struggle, feel free to look at easier tiers for help; but try to dip in and out of them, as the more independent work you do, the better it is for your learning!***
# 
# This challenge will make use of only what you learned in the following DataCamp courses: 
# - Prework courses (Introduction to Python for Data Science, Intermediate Python for Data Science)
# - Data Types for Data Science
# - Python Data Science Toolbox (Part One) 
# - pandas Foundations
# - Manipulating DataFrames with pandas
# - Merging DataFrames with pandas
# 
# Of the tools, techniques and concepts in the above DataCamp courses, this challenge should require the application of the following: 
# - **pandas**
#     - **data ingestion and inspection** (pandas Foundations, Module One) 
#     - **exploratory data analysis** (pandas Foundations, Module Two)
#     - **tidying and cleaning** (Manipulating DataFrames with pandas, Module Three) 
#     - **transforming DataFrames** (Manipulating DataFrames with pandas, Module One)
#     - **subsetting DataFrames with lists** (Manipulating DataFrames with pandas, Module One) 
#     - **filtering DataFrames** (Manipulating DataFrames with pandas, Module One) 
#     - **grouping data** (Manipulating DataFrames with pandas, Module Four) 
#     - **melting data** (Manipulating DataFrames with pandas, Module Three) 
#     - **advanced indexing** (Manipulating DataFrames with pandas, Module Four) 
# - **matplotlib** (Intermediate Python for Data Science, Module One)
# - **fundamental data types** (Data Types for Data Science, Module One) 
# - **dictionaries** (Intermediate Python for Data Science, Module Two)
# - **handling dates and times** (Data Types for Data Science, Module Four)
# - **function definition** (Python Data Science Toolbox - Part One, Module One)
# - **default arguments, variable length, and scope** (Python Data Science Toolbox - Part One, Module Two) 
# - **lambda functions and error handling** (Python Data Science Toolbox - Part One, Module Four) 

# ## The Data Science Pipeline
# 
# This is Tier Three, so we'll get you started. But after that, it's all in your hands! When you feel done with your investigations, look back over what you've accomplished, and prepare a quick presentation of your findings for the next mentor meeting. 
# 
# Data Science is magical. In this case study, you'll get to apply some complex machine learning algorithms. But as  [David Spiegelhalter](https://www.youtube.com/watch?v=oUs1uvsz0Ok) reminds us, there is no substitute for simply **taking a really, really good look at the data.** Sometimes, this is all we need to answer our question.
# 
# Data Science projects generally adhere to the four stages of Data Science Pipeline:
# 1. Sourcing and loading 
# 2. Cleaning, transforming, and visualizing 
# 3. Modeling 
# 4. Evaluating and concluding 
# 

# ### 1. Sourcing and Loading 
# 
# Any Data Science project kicks off by importing  ***pandas***. The documentation of this wonderful library can be found [here](https://pandas.pydata.org/). As you've seen, pandas is conveniently connected to the [Numpy](http://www.numpy.org/) and [Matplotlib](https://matplotlib.org/) libraries. 
# 
# ***Hint:*** This part of the data science pipeline will test those skills you acquired in the pandas Foundations course, Module One. 

# #### 1.1. Importing Libraries

# In[83]:


# Let's import the pandas, numpy libraries as pd, and np respectively. 
import pandas as pd
import numpy as np

# Load the pyplot collection of functions from matplotlib, as plt 
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# #### 1.2.  Loading the data
# Your data comes from the [London Datastore](https://data.london.gov.uk/): a free, open-source data-sharing portal for London-oriented datasets. 

# In[84]:


# Use  https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls

url_LondonHousePrices = "https://data.london.gov.uk/download/uk-house-price-index/70ac0766-8902-4eb5-aab5-01951aaed773/UK%20House%20price%20index.xls"
properties = pd.read_excel(url_LondonHousePrices, sheet_name='Average price', index_col= None)


# ### 2. Cleaning, transforming, and visualizing
# This second stage is arguably the most important part of any Data Science project. The first thing to do is take a proper look at the data. Cleaning forms the majority of this stage, and can be done both before or after Transformation.
# 
# The end goal of data cleaning is to have tidy data. When data is tidy: 
# 
# 1. Each variable has a column.
# 2. Each observation forms a row.
# 
# Keep the end goal in mind as you move through this process, every step will take you closer. 
# 
# 
# 
# ***Hint:*** This part of the data science pipeline should test those skills you acquired in: 
# - Intermediate Python for data science, all modules.
# - pandas Foundations, all modules. 
# - Manipulating DataFrames with pandas, all modules.
# - Data Types for Data Science, Module Four.
# - Python Data Science Toolbox - Part One, all modules

# **2.1. Exploring your data** 
# 
# Think about your pandas functions for checking out a dataframe. 

# In[85]:


# looking at the number of rows and columns, and checking out the dataframe
print(properties.shape)
properties.head()


# **2.2. Cleaning the data**
# 
# You might find you need to transpose your dataframe, check out what its row indexes are, and reset the index. You  also might find you need to assign the values of the first row to your column headings  . (Hint: recall the .columns feature of DataFrames, as well as the iloc[] method).
# 
# Don't be afraid to use StackOverflow for help  with this.

# In[86]:


# Transpose dataframe so borough names will become the row indices and the date time objects will become the column headers
properties_T = properties.T
properties_T.head()


# In[87]:


# Set up right index
# Goal: Each column to represent Month and Year, and each cell-value represent the average price of houses sold in borough of the corresponding row.
properties_T = properties_T.reset_index()
properties_T.columns = properties_T.iloc[0]
properties_T = properties_T.drop(0)
properties_T.head()


# **2.3. Cleaning the data (part 2)**
# 
# You might we have to **rename** a couple columns. How do you do this? The clue's pretty bold...

# In[88]:


# Rename columns
properties_T = properties_T.rename(columns = {'Unnamed: 0':'London_Borough', pd.NaT: 'ID'})
properties_T.columns


# **2.4.Transforming the data**
# 
# Remember what Wes McKinney said about tidy data? 
# 
# You might need to **melt** your DataFrame here. 

# In[89]:


# Check datatypes for any necessary conversions
properties_T.dtypes


# In[90]:


# Change average price to format float64
tidy_properties = properties_T.iloc[:,:2].join(properties_T.iloc[:,2:].astype("float64"))
tidy_properties.dtypes


# In[91]:


tidy_properties = pd.melt(properties_T, id_vars= ['London_Borough', 'ID'])
tidy_properties.columns
tidy_properties = tidy_properties.rename(columns = {0: 'Month', 'value': 'Average_price'})


# In[92]:


tidy_properties['Average_price'] = pd.to_numeric(tidy_properties['Average_price'])
tidy_properties.head()


# In[93]:


# Check for missing values
tidy_properties.count()


# **2.5. Cleaning the data (part 3)**
# 
# Do we have an equal number of observations in the ID, Average Price, Month, and London Borough columns? Remember that there are only 32 London Boroughs. How many entries do you have in that column? 
# 
# Check out the contents of the London Borough column, and if you find null values, get rid of them however you see fit. 

# In[94]:


# Since there are only 32 London boroughs, check out the unique values of the 'London_Borough' column to see if they're all there
tidy_properties['London_Borough'].unique()


# In[95]:


#The strings that don't belong:

#'Unnamed: 34'
#'Unnamed: 37'
#'NORTH EAST'
#'NORTH WEST'
#'YORKS & THE HUMBER'
#'EAST MIDLANDS'
#'WEST MIDLANDS'
#'EAST OF ENGLAND'
#'LONDON'
#'SOUTH EAST'
#'SOUTH WEST'
#'Unnamed: 47'
#'England'

# Delete unncessary rows/emtpy values
tidy_properties[tidy_properties['ID'].isna()]


# In[96]:


# filtering the data with NaN values
NaNFreeDF = tidy_properties.dropna()
NaNFreeDF['London_Borough'].unique()


# In[97]:


# Compare dimensions of clean_properties and NaNFreeDF2 using the .shape attribute
print(tidy_properties.shape)
print(NaNFreeDF.shape)


# In[98]:


# List of non-boroughs. 
nonBoroughs = ['Inner London', 'Outer London', 
               'NORTH EAST', 'NORTH WEST', 'YORKS & THE HUMBER', 
               'EAST MIDLANDS', 'WEST MIDLANDS',
              'EAST OF ENGLAND', 'LONDON', 'SOUTH EAST', 
              'SOUTH WEST', 'England']


# In[99]:


# Filter NanFreeDF on the condition that the rows' values for London_Borough is in the nonBoroughs list. Put in negation operator before filter statement, then reassign 
NaNFreeDF = NaNFreeDF[~NaNFreeDF.London_Borough.isin(nonBoroughs)]

# final-stage dataframe df
df = NaNFreeDF
df.head()


# **2.6. Visualizing the data**
# 
# To visualize the data, why not subset on a particular London Borough? Maybe do a line plot of Month against Average Price?

# In[100]:


# Visualize price shift of average price of one borough
southwark_prices = df[df['London_Borough'] == 'Southwark']

ax = southwark_prices.plot.line (x = 'Month', y='Average_price')
plt.xlabel('Year')
ax.set_ylabel('Average_Price')
plt.title('Average House prices of Southwark')


# To limit the number of data points you have, you might want to extract the year from every month value your *Month* column. 
# 
# To this end, you *could* apply a ***lambda function***. Your logic could work as follows:
# 1. look through the `Month` column
# 2. extract the year from each individual value in that column 
# 3. store that corresponding year as separate column. 
# 
# Whether you go ahead with this is up to you. Just so long as you answer our initial brief: which boroughs of London have seen the greatest house price increase, on average, over the past two decades? 

# In[101]:


import warnings
warnings.simplefilter(action='ignore', category=RuntimeWarning)

# Apply lambda function to extract the year from every value in your Month column
df['Year'] = df['Month'].apply(lambda t: t.year)
df.tail()


# In[102]:


# Group by the London_Borough and Year columns
dfg = df.groupby(by=['London_Borough', 'Year']).mean()
dfg.sample(10)


# In[103]:


#dfg.columns = dfg.columns.droplevel(0)
dfg.columns = dfg.columns.ravel()
list(dfg.columns)


# In[104]:


# Reset the index for the new dataframe
dfg = dfg.reset_index()
dfg.head()


# **3. Modeling**
# 
# Consider creating a function that will calculate a ratio of house prices, comparing the price of a house in 2018 to the price in 1998.
# 
# Consider calling this function create_price_ratio.
# 
# You'd want this function to:
# 1. Take a filter of dfg, specifically where this filter constrains the London_Borough, as an argument. For example, one admissible argument should be: dfg[dfg['London_Borough']=='Camden'].
# 2. Get the Average Price for that Borough, for the years 1998 and 2018.
# 4. Calculate the ratio of the Average Price for 1998 divided by the Average Price for 2018.
# 5. Return that ratio.
# 
# Once you've written this function, you ultimately want to use it to iterate through all the unique London_Boroughs and work out the ratio capturing the difference of house prices between 1998 and 2018.
# 
# Bear in mind: you don't have to write a function like this if you don't want to. If you can solve the brief otherwise, then great! 
# 
# ***Hint***: This section should test the skills you acquired in:
# - Python Data Science Toolbox - Part One, all modules

# In[130]:


# A function that gives the ratio and average house price from '98' to 2018
def create_price_ratio(d):
    y1998 = float(d['Average_price'][d['Year']==1998])
    y2018 = float(d['Average_price'][d['Year']==2018])
    ratio = [y2018/y1998]
    return ratio

create_price_ratio(dfg[dfg['London_Borough']=='Barking & Dagenham'])


# In[131]:


# Get data of ratios and prices from '98' to 2018
dict_price_ratio = {}

for b in dfg['London_Borough'].unique():
    borough = dfg[dfg['London_Borough'] == b]
    dict_price_ratio[b] = create_price_ratio(borough)
print(dict_price_ratio)


# In[132]:


#Ordered/organized dictionary for dict_price_ratio
dict_price_ratio = dict(sorted(dict_price_ratio.items(), key=lambda item: item[1]))
dict_price_ratio


# In[133]:


# Ordered/organized dictionary
df_ratios = pd.DataFrame(dict_price_ratio)
df_ratios_T = df_ratios.T
df_ratios = df_ratios_T.reset_index()


# In[134]:


# Rename the 'index' column as 'London_Borough', and the '0' column to '2018'.
df_ratios.rename(columns={'index':'Borough', 0:'2018'}, inplace=True)


# In[135]:


# Sort in descending order and select the top 15 boroughs.
top15 = df_ratios.sort_values(by='2018',ascending=False).head(15)
print(top15)


# In[136]:


# Plot the boroughs that have seen the greatest changes in price
ax = top15[['Borough','2018']].plot(kind='bar')
ax.set_xticklabels(top15.Borough)
plt.ylabel('Avgerage Prices')
plt.xlabel('2018')
plt.title('Housing Price Ratios for London Boroughs from 1998 to 2018')
plt.show()


# In[137]:


top3 = list(dict_price_ratio)[-3:]
last3 = list(dict_price_ratio)[0:3]
print("Top 3 Boroughs with highest ratios: ", top3)
print("Bottom 3 Boroughs: ", last3)


# ### 4. Conclusion
# What can you conclude? Type out your conclusion below. 
# 
# Look back at your notebook. Think about how you might summarize what you have done, and prepare a quick presentation on it to your mentor at your next meeting. 
# 
# We hope you enjoyed this practical project. It should have consolidated your data hygiene and pandas skills by looking at a real-world problem involving just the kind of dataset you might encounter as a budding data scientist. Congratulations, and looking forward to seeing you at the next step in the course! 
