import requests
from bs4 import BeautifulSoup
import csv
url = "https://www.scholarships.com/financial-aid/college-scholarships/scholarship-directory/academic-major/computer-science"
r = requests.get(url)
# print(r.content)
# print(r.status_code)
soup = BeautifulSoup(r.content, 'html5lib')
# print(soup.prettify())
scholar = []
top1 = soup.find('div')
top2 = top1.find('div', attrs = {'id': 'divoutercontainer'})
top3 = top2.find('table', attrs = {'class': 'scholarshiplistdirectory'})
table = top3.find('tbody')
# table = top2.find('tbody')
# # print(table)
# for row in table.find_all('tr'): 
#     quote = {} 
#     quote['info'] = row.text
    
#     scholar.append(quote) 
    
for link in table.find_all('a'):
        quote = {}
        quote['name'] = link.text
        quote['link'] = 'https://www.scholarships.com/' + link.get('href')
        scholar.append(quote) 
    
# for link in top3.find_all('tr'):
#     quote = {}
#     price = link.find('td', attrs = {'class': 'scholamt'})
#     quote['price'] = 
#     date = link.find('td', attrs = {'class': 'scholdd'})
#     quote['date'] = date
#     scholar.append(quote) 

# To get all the links
# anchor = table.find_all('a')
# for link in anchor:
#     quote = {} 
#     if link.get('href') != '#':
#         quote['LINK'] = link.get('href')
#         scholar.append(quote) 
# print(scholar)

filename = 'Scholarships_final.csv'
with open(filename, 'w', newline='') as f: 
    w = csv.DictWriter(f,['name','link']) 
    w.writeheader() 
    for quote in scholar: 
        w.writerow(quote) 