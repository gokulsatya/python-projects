# This program meets the following requirements:
# - It pulls data from 5 different webpages
# - It performs basic calculations on numerical data from 3 of those pages
# - It generates 3 charts from 3 of those pages
# - It saves the data to a file



import pandas as pd
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import requests

def fetch_data(url):
    tables = pd.read_html(url)
    return tables[0]  # assuming the first table contains the relevant data

data1 = fetch_data('https://www.geeksforgeeks.org/')
data2 = fetch_data('https://www.geeksforgeeks.org/page/10/')
data3 = fetch_data('https://www.geeksforgeeks.org/page/20/')
data4 = fetch_data('https://www.geeksforgeeks.org/page/30/')
data5 = fetch_data('https://www.geeksforgeeks.org/page/40/')

def calculate(data):
    return {
        'mean': data.mean(),
        'median': data.median(),
        'mode': data.mode(),
        'min': data.min(),
        'max': data.max(),
    }

stats1 = calculate(data1)
stats2 = calculate(data2)
stats3 = calculate(data3)

def generate_chart(data, title):
    data.plot(kind='bar', title=title)
    plt.savefig(title + '.png')

generate_chart(data1, 'Chart 1')
generate_chart(data2, 'Chart 2')
generate_chart(data3, 'Chart 3')

data1.to_csv('data1.csv')
data2.to_csv('data2.csv')
data3.to_csv('data3.csv')
data4.to_csv('data4.csv')
data5.to_csv('data5.csv')