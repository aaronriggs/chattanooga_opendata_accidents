#includes feature groups, marker clusters, and different icons based on conditions
import folium
from folium.plugins import MarkerCluster
import sqlite3
import pandas as pd

#for processing elapsed time
from timeit import default_timer as timer

def csv2db():
    try:
        # modified https://stackoverflow.com/questions/41900593/csv-into-sqlite-table-python
        # load data
        csv_name = "VEHICLE_INCIDENTS_CORRECTED"
        df = pd.read_csv(csv_name + '.csv')
        # strip whitespace from headers
        df.columns = df.columns.str.strip()
        # open database connection
        con = sqlite3.connect(csv_name + ".db")
        # drop data into database
        df.to_sql(csv_name, con, if_exists='replace')
        # close database connection
        con.close()
    except Exception as er:
        print('Error occurred while creating the database:', er)

#create the database used below
csv2db()

#zoom sets height above city
m = folium.Map([35.1002, -85.2374], zoom_start=12)

#allows marker clusters to be created and selected from the folium layer control in top right of map
mCluster_fatal = MarkerCluster(name="Fatal Accident").add_to(m)
mCluster_Medical = MarkerCluster(name="Accident with Medical Transport Involved").add_to(m)
mCluster_accident = MarkerCluster(name="Accident without Medical Transport").add_to(m)
mCluster_dui = MarkerCluster(name="Alcohol Involved in Accident").add_to(m)
mCluster_drugs = MarkerCluster(name="Drugs Involved in Accident").add_to(m)
mCluster_HR = MarkerCluster(name="Hit and Run").add_to(m)
mCluster_HR_Fatal = MarkerCluster(name="Hit and Run with Fatality").add_to(m)
mCluster_Placard = MarkerCluster(name="Involved Placarded Truck").add_to(m)
mCluster_Pedestrian = MarkerCluster(name="Accident Involved a Pedestrian").add_to(m)
mCluster_Ped_HR = MarkerCluster(name="Pedestrian Involved Accident with Hit and Run").add_to(m)
mCluster_Ped_F_HR = MarkerCluster(name="Pedestrian Involved in Fatal Hit and Run").add_to(m)
mCluster_Bicycle = MarkerCluster(name="Bicycle Involved").add_to(m)
mCluster_Bicycle_Fatal = MarkerCluster(name="Bicycle Involved Fatality").add_to(m)
mCluster_Bicycle_F_HR = MarkerCluster(name="Bicycle Involved Fatal Hit and Run").add_to(m)

#minimum viable sql and prepared sql statement
conn = sqlite3.connect('VEHICLE_INCIDENTS_CORRECTED.db')
cursor = conn.cursor()

print("Time range for accident data is: 2018-01-01 - 2025-01-14")
print("Using the format 2018-01-01...")
start_date = input("Enter the start date you would like to use: ")
print("Thank you.")
end_date = input("Enter the end date you would like to use: ")
print("Thank you.")

# command cannot be changed without refactoring all conditions below
# later version allow user selectable criteria
command = ("SELECT Incident_Number, Incident_Date, Hit_and_Run, Involved_Fatal_Injury,"
           "Involved_Medical_Transport, Involved_Placarded_Truck, Pedestrian_Involved, Bicycle_Involved,"
           "Drug_Involved, Alcohol_Involved, Latitude, Longitude FROM VEHICLE_INCIDENTS_CORRECTED WHERE "
           "Incident_Date BETWEEN ? AND ?")

cursor.execute(command, (start_date, end_date))
results = cursor.fetchall()
conn.close()

save_file = input("What should I save this map as? -> ")
print("Processing....")
start = timer()

for row in results:
    try:
        # https://getbootstrap.com/docs/3.3/components/
        if row[2] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Hit and Run",
                popup=additional_info,
                icon=folium.Icon(icon="flag", color="red"),
            )
            mCluster_HR.add_child(marker)

        if row[2] == 'Yes' and row[3] == 'Yes' and row[7] == 'Yes': #reorder this statement to at top of loop
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Fatal Hit and Run Involving a Bicycle",
                popup=additional_info,
                icon=folium.Icon(icon="certificate", color="red"),
            )
            mCluster_Bicycle_F_HR.add_child(marker)

        if row[2] == 'Yes' and row[3] == 'Yes' and row[6] == 'Yes': #reorder this statement to at top of loop
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Fatal Hit and Run involving a Pedestrian",
                popup=additional_info,
                icon=folium.Icon(icon="certificate", color="red"),
            )
            mCluster_Ped_F_HR.add_child(marker)

        if row[3] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Fatal Accident",
                popup=additional_info,
                icon=folium.Icon(icon="warning-sign", color="black"),
            )
            mCluster_fatal.add_child(marker)

        if row[2] and row[6] == 'Yes' and row[3] == 'No':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Hit and Run Involving a Pedestrian",
                popup=additional_info,
                icon=folium.Icon(icon="certificate", color="red"),
            )
            mCluster_Ped_HR.add_child(marker)

        elif row[2] and row[3] == "Yes":
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Hit and Run with Fatality",
                popup=additional_info,
                icon=folium.Icon(icon="flash", color="darkred"),
            )
            mCluster_HR_Fatal.add_child(marker)

        elif row[4] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Medical Transport Involved",
                popup=additional_info,
                icon=folium.Icon(icon="asterisk", color="darkpurple"),
            )
            mCluster_Medical.add_child(marker)

        elif row[5] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Accident Involving Placarded Truck",
                popup=additional_info,
                icon=folium.Icon(icon="flag", color="gray"),
            )
            mCluster_Placard.add_child(marker)

        elif row[6] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Pedestrian Involved Accident",
                popup=additional_info,
                icon=folium.Icon(icon="certificate", color="red"),
            )
            mCluster_Pedestrian.add_child(marker)

        elif row[3] and row[7] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Bicycle Involved Accident with Fatality",
                popup=additional_info,
                icon=folium.Icon(icon="certificate", color="red"),
            )
            mCluster_Bicycle_Fatal.add_child(marker)

        elif row[7] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Bicycle Involved Accident",
                popup=additional_info,
                icon=folium.Icon(icon="flag", color="pink"),
            )
            mCluster_Bicycle.add_child(marker)

        elif row[8] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Drugs Involved in Accident",
                popup=additional_info,
                icon=folium.Icon(icon="flag", color="orange"),
            )
            mCluster_drugs.add_child(marker)

        elif row[9] == 'Yes':
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Alcohol Involved in Accident",
                popup=additional_info,
                icon=folium.Icon(icon="flag", color="purple"),
            )
            mCluster_dui.add_child(marker)

        else:
            additional_info = str("Incident #:\n" + row[0] + "\n" + "Date:\n" + row[1])
            marker = folium.Marker(
                location=[row[10], row[11]],
                tooltip="Accident Without Medical Transport",
                popup=additional_info,
                icon=folium.Icon(icon="ok-sign", color="lightgray"),
            )
            mCluster_accident.add_child(marker)

    except:
        print("Exception occurred, error occurred in row or nulls present in requested data...")
        print("Skipping row containing error and continuing...")
        continue

# add folium map layer control
folium.LayerControl().add_to(m)
m.save(save_file + ".html")

end = timer()

print(f"Time in seconds to complete request: {end - start}")
print("Map generation is now complete.")
print(f"Now saving {save_file}.html")
print("Program completed successfully!")