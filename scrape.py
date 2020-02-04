# WEB SCRAPING GFG WEBSITE AND GETTING INFO ABOUT ALL THE 
# DP PROBLEMS , CONTENT AND THE COMMENTS

from bs4 import BeautifulSoup
import requests
import csv

source = requests.get('https://www.geeksforgeeks.org/category/dynamic-programming/').text
csv_file = open('dp.csv','w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['dp-problem','summary','tags'])
soup = BeautifulSoup(source,'lxml')
articles = soup.find_all('article')
for i in articles:
    try:
        title = i.a['title'][13:]
        print(title)
        para = i.p.text[:-13]
        print(para)
        tags = []
        for j in i.footer.find_all('div'):
            tag = j.a.text
            print(tag)
            tags.append(tag)
        csv_writer.writerow([title,para,tags])
    except Exception as e:
        print(e)
    print()
csv_file.close()

    


# from bs4 import BeautifulSoup
# import requests


# # with open('sample.html') as html_file:
# #     soup = BeautifulSoup(html_file,'lxml')
    
# # #print(soup.prettify()) -- getting the entire html with indented
# # #print(soup.title.text)  -- getting the text only of a tag
# # #print(soup.find('div',class_="class2"))   -- getting a particular div with has the class , class_ = given

# # divs = soup.find_all('div')
# # for i in divs:
# #     print(i.h1.text)

# source = requests.get('https://en.wikipedia.org/wiki/Biology').text

# soup = BeautifulSoup(source,'lxml')

# toc = soup.find('div',id='toc')

# for element in toc.ul.find_all('li'):
#     print(element.a.find('span',class_='toctext').text)




