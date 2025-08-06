# Welcome!

An example of the folium webpage that is generated from this project can be found at folium_python_example.html

This page contains the first 50 accidents contained in the data. 

### folium_for_github.py is the main project file.  

Originally, I asked that YOU run csv2db.py and folium_from_db_v8_optimizing.py to generate the necessary database and your desired map. That is no longer required. YOU should not have to do anything to make my project functional. 

All you need to do is follow the requirements.txt, copy VEHICLE_INCIDENTS_CORRECTED.csv and folium_for_github.py into the same VENV, run folium_for_github.py, input the dates as requested, and you will have your own custom map! 


# Extra Info

This project contains accident data acquired from the public Chattanooga Open Data website. Accidents shown occurred between 2018 and 2025. This list may not be all inclusive and I have no way to verify data authenticity as I am not a Chattanooga City Employee nor did I collect this data.  

While using this program, you will be prompted to input a start and end date to allow map data to be generated. Date data starts at "2018-01-01 00:00:00" and ends at "2025-01-14 12:54:00". Using date format "2025-01-14" is sufficient to search. 

If using the above dates, this will generate a map containing all accidents within the provided data between 2018 and 2025. 

Accidents have been categorized by data provided within and grouped by criteria I created to better visualize the accidents. 

Map file size generated with all entries is showing as 153mb. Using Folium Marker Clusters drastically reduces file size and loading times. 

To show or hide accident categories, please go to the top right corner, and click the "stack" icon. 

Thank you for checking out this python project!
