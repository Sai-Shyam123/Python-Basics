import pandas as pd
import requests
from bs4 import BeautifulSoup

page = requests.get('https://corona.e.gov.kw')
soup = BeautifulSoup(page.content, 'html.parser')
div = soup.find(class_='containers-div')
items =  div.find_all(class_='col-md-3 col-sm-6 col-6')

period_names = [item.find(class_='count-text').get_text() for item in items]
cs_num = [num.find(class_='timer count-title count-number').get_text() for num in items]

whole_stuff = pd.DataFrame(
    {
        'period': period_names,
        'short_desc': cs_num,
    })

print(whole_stuff)