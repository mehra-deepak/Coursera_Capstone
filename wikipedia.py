from bs4 import BeautifulSoup
import requests
import csv
import pandas as pd

source =requests.get("https://en.wikipedia.org/wiki/List_of_postal_codes_of_Canada:_M").text
soup=BeautifulSoup(source,'lxml')

# print(soup.prettify())



my_table=soup.find('table',{'class':'wikitable sortable'})

table_rows=my_table.find_all("tr")

res=[]

for tr in table_rows:
    td=tr.find_all('td')
    row = [tr.text.strip() for tr in td if tr.text.strip()]
    if row:
        res.append(row)

df=pd.DataFrame(res,columns=["Postcode","Borough","Neighbourhood"])
print(df)