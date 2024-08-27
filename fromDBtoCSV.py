import sqlite3
import csv

def convert_db_to_csv(db_file, csv_file):
    # Connect to SQLite database
    conn = sqlite3.connect(db_file)
    cursor = conn.cursor()

    # Get all tables in the SQLite database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    # Loop through each table and write contents to CSV
    for table_name in tables:
        table_name = table_name[0]
        cursor.execute(f"SELECT * FROM {table_name}")
        
        # Fetch all data from table
        rows = cursor.fetchall()

        # Fetch the column names for the CSV header
        column_names = [description[0] for description in cursor.description]

        # Open a CSV file to write (each table will have own CSV file)
        with open(f'{csv_file}_{table_name}.csv', 'w', newline='') as csvfile:
            csvwriter = csv.writer(csvfile)

            # Write column names
            csvwriter.writerow(column_names)

            # Write data rows
            csvwriter.writerows(rows)

        print(f"Table {table_name}  exported to {csv_file}_{table_name}.csv")

    # Close the database connection
    conn.close()

# Usage
db_file = 'wpndatabase.db'  # Path to SQLite database file
csv_file = 'wpndatabase'    # Base name for output CSV file(s)

convert_db_to_csv(db_file, csv_file)
