import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://www.iplt20.com/auction/2022"
r=requests.get(url)
print(r)

soup=BeautifulSoup(r.text,"lxml")
print(soup)

table=soup.find("table", class_="ih-td-tab auction-tbl")
header=table.find_all("th")
print(table)
print(header)

# Storing the header as a list
col_header=[]

for i in header:
    name=i.text
    col_header.append(name)
print(col_header)

# storing as a dataframe
df=pd.DataFrame(columns=col_header)
print(df)

rows=table.find_all("tr")
print(rows)

# Prints all team names
# for i in rows[1:]:
#     data=i.find_all("td")
#     print(data)
#     for j in data:
#       row=j.text
#       print(row) 

# Prints entire list
for i in rows[1:]:
    first_td=i.find_all("td")[0].find("div", class_="ih-pt-ic").text.strip()
    data=i.find_all("td")[1:]
    row=[tr.text for tr in data]
    # Prints the 2nd, 3rd and 4th column
    # print(row)
    row.insert(0,first_td)
    l=len(df)
    df.loc[l]=row
print(df)

df.to_csv("IPL Auction Stats.csv") 