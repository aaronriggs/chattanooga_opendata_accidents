import sqlite3
import pandas as pd

class CreateDB:
    def __init__(self):
        try:
            # modified https://stackoverflow.com/questions/41900593/csv-into-sqlite-table-python
            # load data
            csv_name = input("Enter CSV file name for Database creation: " )
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

#CreateDB()
if __name__ == "__main__":
    CreateDB()
