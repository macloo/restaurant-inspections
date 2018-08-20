from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

# use only one URL for testing code
# all violations for one date, one location
my_url = 'https://www.myfloridalicense.com/inspectionDetail.asp?InspVisitID=6602877&id=4070634'
html = urlopen(my_url)
soup = BeautifulSoup(html, "lxml")
# create a new file for writing
newfile = open('anewfile.txt', 'w')

# get all tables
tables = soup.find_all( "table" )
# get all rows from the one table we want
rows = tables[16].find_all("tr")
# get cells we want from each row - note, middle cell is empty
for row in rows:
    cells = row.find_all("td")
    violation = cells[0].get_text().strip()
    if violation != "Violation":
        obs = cells[2].get_text().strip()
        # from link, get numeric code to open description page for this violation
        popup = cells[0].find("a")
        p = re.compile("(\(')((.)*)('\))")
        m = p.search( str(popup) )
        details_id = m.group(2)
        # write out to file
        newfile.write( "Violation: {}\nDetails: {}\nObservation: {}\n\n".format(violation, details_id, obs) )

# close and save the new file
newfile.close()
