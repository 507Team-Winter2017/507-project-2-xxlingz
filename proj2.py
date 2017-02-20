#proj2.py


#### Problem 1 ####
print('\n*********** PROBLEM 1 ***********')
print('New York Times -- First 10 Story Headings\n')

### Your Problem 1 solution goes here

import requests
from bs4 import BeautifulSoup, SoupStrainer
 
base_url1 = 'http://www.nytimes.com'
r1 = requests.get(base_url1)
soup1 = BeautifulSoup(r1.text,"html.parser")

for story_heading in soup1.find_all(class_="story-heading")[:10]: 
    if story_heading.a: 
        print(story_heading.a.text.replace("\n", " ").strip())
    else: 
        print(story_heading.contents[0].strip())

#### Problem 2 ####
print('\n*********** PROBLEM 2 ***********')
print('Michigan Daily -- MOST READ\n')

### Your Problem 2 solution goes here
base_url2 = 'https://www.michigandaily.com'
r2 = requests.get(base_url2)
soup2 = BeautifulSoup(r2.text,"html.parser")
panel_div = soup2.find_all(class_="panel-pane pane-mostread")
for headline in panel_div[0].find_all("a"): 
 	print(headline.text.replace("\n", " ").strip())


#### Problem 3 ####
print('\n*********** PROBLEM 3 ***********')
print("Mark's page -- Alt tags\n")

### Your Problem 3 solution goes here
base_url3 = 'http://newmantaylor.com/gallery.html'
r3 = requests.get(base_url3)
soup3 = BeautifulSoup(r3.text,"html.parser")
for img in soup3.find_all("img"):
	if len(img.get('alt', '')):
		print(img.get('alt', ''))
	else:
		print("No alternative text provided!")

#### Problem 4 ####
print('\n*********** PROBLEM 4 ***********')
print("UMSI faculty directory emails\n")

### Your Problem 4 solution goes here
contact = []
for i in range(6):
    base_ur4 = "https://www.si.umich.edu/directory?field_person_firstname_value=&field_person_lastname_value=&rid=4&page={}".format(i)
    r4 = requests.get(base_ur4,headers={'User-Agent': 'SI_CLASS'})
    soup_link = BeautifulSoup(r4.text,"html.parser")
    links_bs = soup_link.find_all(class_="field field-name-contact-details field-type-ds field-label-hidden")
    for links in links_bs:
        a = links.find_all("a")
        if a[0].has_attr('href'):
            contact.append(a[0]['href'])
for professor in contact:
    base_ur5 = "https://www.si.umich.edu"+professor
    r5 = requests.get(base_ur5,headers={'User-Agent': 'SI_CLASS'})
    soup_email = BeautifulSoup(r5.text,"html.parser")
    links_email = soup_email.find_all(class_="field field-name-field-person-email field-type-email field-label-inline clearfix")
    for email in links_email[0].find_all("a"): 
        print(email.text)


