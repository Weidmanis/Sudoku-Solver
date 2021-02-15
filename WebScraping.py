# basic HTML web scraping

# Libraries used
from bs4 import BeautifulSoup
import requests
import re
import numpy as np


html = requests.get('https://en.sudoku-online.net/')
webpage = BeautifulSoup(html.content, 'html5lib')

t1 = webpage.find('body').find('div').find('div').find('div')
t2 = t1.find('main').find('section').find('div')
t3 = t2.find('div', class_=re.compile("sudoku")).find('div').find('div')
t4 = t3.find('div', class_=re.compile('row')).find('div')
print(t4)


















# # gets the frame of the puzzle html tag
# body = soup.find('body')

# sq1 = body.find('div', class_ = 'w1_d1')
# print(sq1.prettify())


# for col in range(3):
#     for row in range(3):
#         data = sq1.find('div', {'id':f'c_{col}_{row}'})
#         numb = data.find('div')
#         print(numb)
