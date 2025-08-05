Welcome!

Example website that is generated for a quick overview of the project can be found at folium_from_db_v9.html

Unfortunately, due to the 25mb file size constraints, work is need on your part to make this project functional if you would like to see a wider date range. 

This project contains accident data acquired from the public Chattanooga Open Data website. Accidents shown occurred between 2018 and 2025. This list may not be all inclusive and I have no way to verify data authenticity as I am not a Chattanooga City Employee nor did I collect this data.  

The CSV provided must be converted to a sqlite database file using csv2db.py, with the generated file named "VEHICLE_INCIDENTS_CORRECTED" when prompted, THEN run with folium_from_db_v8_optimizing.py to generate the folium map showing accidents by type. 

This will generate a map containing all accidents within the provided data between 2018 and 2025. Accidents have been categorized by data provided within and grouped by criteria I created to better visualize the accidents. 

folium_from_db_v8_optimizing.py uses all database entries to create the map. Modification of SQL command code can isolate date ranges, such as:

command = ("SELECT Incident_Number, Incident_Date, Hit_and_Run, Involved_Fatal_Injury,"
           "Involved_Medical_Transport, Involved_Placarded_Truck, Pedestrian_Involved, Bicycle_Involved,"
           "Drug_Involved, Alcohol_Involved, Latitude, Longitude FROM VEHICLE_INCIDENTS_CORRECTED" WHERE "
           "Incident_Date BETWEEN '2018-01-01 00:00:00' AND '2018-06-31 23:59:59' LIMIT 50")

I have provided folium_from_db_v9.py and folium_from_db_v9.html as proof of concept of these changes.  

Map size generated with all entries is showing as 153mb. 

Map size generated with above sql changes in file folium_from_db_v9.html is showing as 102kb.

To show or hide accident categories, please go to the top right corner, and click the "stack" icon. 

Thank you for checking out this python project!
