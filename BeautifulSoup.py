# If you want to scrape the website
# 1. Use the API
# 2. HTML Web Scraping using some tool like bs4

# Install all requirements
# 1.pip install requests
# 2.pip install bs4
# 3.pip install html5lib

import requests
from bs4 import BeautifulSoup

# url of site from where we to scrap content
url = "https://codewithharry.com"

# Step1: Get the HTML
r = requests.get(url);
htmlContent = r.content
# print(htmlContent)

# Step2: Parse the HTML
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup)
# print(soup.prettify)

# Step3: HTML Tree traversal
#
# Commomly used types of Objects:
# 1.print(type(title)) --> Tag
# 2. print(type(title.string)) --> NavigableString
# 3. print(type(soup)) --> BeautifulSoup
# 4. Comment --> # markup = "<p><!-- this is a comment --></p>"
                 # soup2 = BeautifulSoup(markup)
                 # print(soup2.p)
                 # print(soup2.p.string)
                 # print(type(soup2.p.string))
                 #exit()  # Profram will not run further

# Get the title of html page
title = soup.title
# print(title)

# Getting all para tag
paras = soup.find_all('p')
# print(paras)

# Getting all anchor tag
anchor = soup.find_all('a')
# print(anchor)

# Get first element in html page
#print(soup.find('p'))

# Get classes of any eement in the html page
print(soup.find('p')[
          'class'])  # gives the value of classes for the first para in dom,if no class attribute is there it gives keyError
# print(soup.find('p')['id'])#keyError

# find all he elements with class lead
#print(soup.find_all("p", class_="lead"))

# Get the text from the tag/soup
# print(soup.find('p').get_text())
# print(soup.get_text())#Returns the content of whole javascript

# GET all the links on the page:
all_links = set()  # an empty set
for link in anchor:
    if (link.get('href') != '#'):
        linkText = "https://codewithharry.com" + link.get('href')
        all_links.add(linkText)
        print(linkText)

navbarSupportedContent = soup.find(id='navbarSupportedContent')#return element with this id
#print(navbarSupportedContent)
print(navbarSupportedContent.children)#get all contents of div
print(navbarSupportedContent.contents)#get all contents of div,both contents & childrens gives the same reult but are different as

#.contents-->A tag's children are available as a list and get stored in memory from where we can fetch it
#.childrens --> A tag's children are available as a generator ,not stored in memory ,can be get using loop

#iterating contents of print(navbarSupportedContent.children)

# for item in navbarSupportedContent.strings:
#      print(item)

# for item in navbarSupportedContent.stripped_strings:#spaces r removed
#     print(item)

for item in navbarSupportedContent.parents:
    print(item.name)

# for item in navbarSupportedContent.parent:
#     print(item)

#Getting previous and next siblings
print(navbarSupportedContent.next_sibling)#counts space as a sibling too
print(navbarSupportedContent.next_sibling.next_sibling)
print(navbarSupportedContent.previous_sibling.previous_sibling)

#CSS Selectors
print(soup.select('#loginModal'))#A div tag

#We can insert also read beautiful soup documentation

