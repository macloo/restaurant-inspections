# restaurant-inspections
Some code to gather, sort and clean up restaurant inspection data from the state of Florida
Goal: To publish info on serious health problems identified in inspections at local restaurants.
Approach:
1. Gather data: 
Available as a csv file at http://www.myfloridalicense.com/DBPR/hotels-restaurants/public-records/#1506344763000-101d4ee5-7a59
2. Reduce unneeded data:
Data set for Alachua County + with “High Priority” violations + within time frame (1 week). Time frame may be user input range,
or within a week prior to running the script.
- Read in csv
- Remove unnecessary columns: keep 'CountyName', 'LicenseID', 'VisitID', 'VisitDate', 'HighPriority' 
- Filter for Alachua County records
- Filter for serious violations
- Filter for date range
- Place 'LicenseID' and 'VisitID' into url that accesses detailed reports
3. Use url list to scape data for high priority violators
- scrape individual reports
- filter for the tags we want
- format in readable text
- output into text file
- email text file to recipients
Final result might look like this:
Bubba's BBQ, 123 NW 4th Ave., Gainesville, had a routine inspection on May 1.
A total of four violations were noted, two of are considered "high priority."
High priority: chicken salad kept above 40 degrees. High priority: cleaning
solutions kept in unmarked bottles. Warning issued.
