#!/usr/bin/python3

import pandas
import csv
from datetime import datetime
def process_pandas():
  # time_cols=['PRICING_EFFECTIVE_DATE']
  # ,parse_dates=time_cols
  df = pandas.read_csv('prices.csv')
  return print(df['PRODUCT_PRICE'].mean())

def process_csv():
  with open('prices.csv', newline='') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    total=0
    count=0
    for row in csv_reader:
      total+= float(row['PRODUCT_PRICE'])
      count+=float(1)
  return total/count

def process_py():
  with open('prices.csv', 'r') as file:
    count=0
    total=0
    
    # turns lines into lists comma seperated
    lines = [line.strip().split(',') for line in file]
    Headers=lines[0]
    Data=lines[1:]
    
    # Creates a dictionary for each line with the headers as keys 
    Data=[dict(zip(Headers,data_line)) for data_line in Data]
    
    # Goes through each line/dictionary and adds up the product prices as well as the number of lines
    for n in Data:
      total+=float(n['PRODUCT_PRICE'])
      count+=float(1)
  return total/count

def process_csv_dict():
  # makes effective date a date not object
  # time_cols= ['PRICING_EFFECTIVE_DATE']
  # ,parse_dates=time_cols

  # extracts data via pandas
  df = pandas.read_csv('prices.csv')
  Category_Averages= df.groupby('ITEM_CATEGORY_NAME')['PRODUCT_PRICE'].mean()
  return Category_Averages.to_dict()
# {'Wine': 231.77917462743028, 
# 'Spirits': 1375.8744982699216, 
# 'Refreshment Beverages': 15.805849056603703, 
# 'Beer': 17.476013667425885, 
# 'General Merchandise': 13.038000000000002}

def process_pandas_groupby():
  # makes effective date a date not object
  # time_cols= ['PRICING_EFFECTIVE_DATE']
  # ,parse_dates=time_cols
  # extracts data via pandas
  df = pandas.read_csv('prices.csv')
  Category_Averages= df[['ITEM_CATEGORY_NAME','PRODUCT_PRICE']].groupby('ITEM_CATEGORY_NAME').mean()
 
  return Category_Averages

if __name__ == "__main__":
    print("Average price using pure python: ", end='')    
    print(process_py())
    print("Average price using csv module: ", end='')    
    print(process_csv())
    print("Average price using pandas module: ", end='')    
    print(process_pandas())
    print(process_csv_dict())
    print(process_pandas_groupby())