# restaurant-inspections
Some code to gather, sort and clean up restaurant inspection data from the state of Florida

Goal: To publish info on serious health problems identified in inspections at local restaurants.

High level approach:

Build database of restaurant inspection information
1. Get data from state summary reporton restaurant inspections in our district, filtered for fields we need.
2. Use that for two purposes:
A. Filter for new reports added since script last run, and place new data into database table.
B. Create a list of URLs for the detailed reports in what inspectors observed.
3. Iterate through the URLs to scrape the data of observations, clean that up, and save into a separate table in the database.
4. All of the above may be set as a chon job to run daily so the load on state servers isn't so heavy.

Generate report for publication // this might be a separate script4.
1. Set a time period for what we'll publisher, either from user input or from pre-determined time frame like proir week.
2. Pull data from database and format for publication, saved as txt file.
3. Email the file or make available for download.
4. This step may be implemented as a web page that user can access, or as a chron job.

Final result might look like this:
Bubba's BBQ, 123 NW 4th Ave., Gainesville, had a routine inspection on May 1.
A total of four violations were noted, two of are considered "high priority."
High priority: chicken salad kept above 40 degrees. High priority: cleaning
solutions kept in unmarked bottles. Warning issued.
