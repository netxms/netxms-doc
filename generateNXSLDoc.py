import requests
from bs4 import BeautifulSoup
import os

# function defenition

def getSubPage(link):
   content = requests.get('%s%s' % (linkBase,link)).text
   soupPage =  BeautifulSoup(content, "html.parser")
   #get div with mw-content-text
   mainDivElement = soupPage.find(id="mw-content-text")
   result = "";
   for child in mainDivElement:
      if "p" == child.name and child.text.strip() != "":
         result = result+child.text+"\n\n"
      if "h2" == child.name and child.text.strip() != "":
         result = result+child.text+"\n"
         for n in child.text:
            result = result+"~"
         result = result+"\n\n"
      if "dl" == child.name or "table" == child.name or "div" == child.name:
         result = result+child.get_text()+"\n\n"
      if "pre" == child.name and child.text.strip() != "":
         result = result+child.text+"\n\n"
   return result;

#main page

linkBase = 'https://wiki.netxms.org'
html_content= requests.get('%s/wiki/NXSL_Function_Reference' % linkBase).text
soup =  BeautifulSoup(html_content, "html.parser")

#clean old file
if os.path.isfile('nxsl-class-description.rst'):
   os.remove('nxsl-class-description.rst') 

#Write header
rstFile = open('nxsl-class-description.rst', 'w+')
rstFile.write('.. _nxsl-class-description:\n\n')
rstFile.write('############## \n\
NXSL Functions\n\
##############\n\n')
rstFile.write('This chapter descrbes available NXSL functions.\n\n')
rstFile.write('Function tables\n\
===============\n\n')


#Generate table
numOfCol = 0;
numOfRow = 0;
for table in soup.find_all('table'):
   rstFile.write(".. list-table:: \n\
   :header-rows: 1\n\
   :widths: ")
   rows = table.find_all('tr')
   rows.remove(rows[len(rows)-1]) # remove last empty row
   for x in range(0, len(rows[0].find_all('td'))):
      rstFile.write("60 ")
   rstFile.write("\n\n")
   numOfRow = 0
   for tr in rows:
      numOfRow += 1
      columns = tr.find_all('td')   
      numOfCol = 0
      for td in columns:
         numOfCol += 1
         if numOfRow == 1 or td.text.rstrip() == "": #do not create links for empty rows and for header row
            if numOfCol == 1:
               rstFile.write("   * - %s\n" % td.text.strip())  
            else:
               rstFile.write("     - %s\n" % td.text.strip())
         else:
            if numOfCol == 1:
               rstFile.write("   * - :ref:`%s <nxsl-%s>`\n" % (td.text.strip(),td.text.strip()))  
            else:
               rstFile.write("     - :ref:`%s <nxsl-%s>`\n" % (td.text.strip(),td.text.strip()))
   rstFile.write("\n\n")

#generate description for table items
for table in soup.find_all('table'):
   rows = table.find_all('tr')
   rows.remove(rows[len(rows)-1]) # remove last empty row 
   #should go in reverse orger - first take all rows fo eash column   
   numOfRow = len(rows)
   numOfCol = len(rows[0].find_all('td'))
   for x in range(0, numOfCol):
      #first is always header
         header = rows[0].find_all('td')[x].text.strip()
         rstFile.write("%s\n" % header) 
         for i in header:
            rstFile.write("=")
         rstFile.write("\n\n");
         for y in range(1, numOfRow):
            header = rows[y].find_all('td')[x].text.strip()
            if header == "":
               break; # If row empty go to next column
            rstFile.write(".. _nxsl-%s:\n\n" % header)
            rstFile.write("%s\n" % header) 
            for i in header:
               rstFile.write("-")
            rstFile.write("\n\n");
            #get page with this function info if exist and add to page
            href = rows[y].find_all('td')[x].find_all('a')[0].get('href')
            if "wiki" in href:
               rstFile.write(getSubPage(href).encode('utf-8'))
            else:
               rstFile.write("Under construction")
            rstFile.write("\n\n");


#clean old file
if os.path.isfile('nxsl-class-description.rst'):
   if os.path.isfile("admin/nxsl-class-description.rst"):
      os.remove("admin/nxsl-class-description.rst")
   os.rename("nxsl-class-description.rst", "admin/nxsl-class-description.rst")



