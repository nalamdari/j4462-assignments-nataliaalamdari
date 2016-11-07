import urllib2
import unicodecsv as csv
import mechanize
from bs4 import BeautifulSoup

br = mechanize.Browser()
br.open('http://enrarchives.sos.mo.gov/enrnet/PickaRace.aspx')

# Fill out the top form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboElectionNames'] = ['750003566']
br.submit('ctl00$MainContent$btnElectionType')

# Fill out the bottom form
br.select_form(nr=0)
br.form['ctl00$MainContent$cboRaces'] = ['750003269']
br.submit('ctl00$MainContent$btnCountyChange')

# Get HTML
html = br.response().read()

########## YOUR CODE HERE ##########

soup = BeautifulSoup(html, "html.parser")
table = soup.find('table', {'id': 'MainContent_dgrdCountyRaceResults'})

list_of_rows = []
for row in table.find_all('tr'):
    list_of_cells = []
    for cell in row.find_all('th'):
        text = cell.text
        list_of_cells.append(text)
        
    for cell in row.find_all('td'):
        text = cell.text
        list_of_cells.append(text)
    list_of_rows.append(list_of_cells)

outfile = open("./election-results.csv", "wb")
writer = csv.writer(outfile)
writer.writerows(list_of_rows)  

