# violations go individually into a table - doug 8/22
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

def make_obs():
    visitid = url.split("VisitID=")[1].split("&")[0]
    html = urlopen(url)
    soup = BeautifulSoup(html, "lxml")
    tables = soup.find_all( "table" )
    rows = tables[16].find_all( "tr" )
    # get cells we want from each row - note, middle cell is empty
    for row in rows:
        cells = row.find_all( "td" )
        violation = cells[0].get_text().strip()
        if violation != "Violation":
            obs = cells[2].get_text().strip()
            # from link, get numeric code to open description page for this violation
            popup = cells[0].find( "a" )
            p = re.compile("(\(')((.)*)('\))")
            m = p.search( str(popup) )
            details_id = m.group(2)
            vals = (visitid, violation, details_id, obs)
            # db table named violations already exists
            c.execute('''INSERT OR IGNORE INTO violations (visitid, violation, details_id, obs) VALUES (?,?,?,?)''', vals)
            conn.commit()

for url in urlList:
    make_obs()

# close after all violations have been written into table
conn.close()
