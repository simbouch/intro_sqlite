import sqlite3
import csv

# Connect to the SQLite database
connection = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = connection.cursor()

# Export Clients table to CSV
cursor.execute("SELECT * FROM Clients")
clients = cursor.fetchall()

with open('clients_export.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row with column names
    csvwriter.writerow([description[0] for description in cursor.description])
    # Write all rows of data
    csvwriter.writerows(clients)
print("Clients data exported to 'clients_export.csv'")

# Export Commandes table to CSV
cursor.execute("SELECT * FROM Commandes")
commandes = cursor.fetchall()

with open('commandes_export.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write the header row with column names
    csvwriter.writerow([description[0] for description in cursor.description])
    # Write all rows of data
    csvwriter.writerows(commandes)
print("Commandes data exported to 'commandes_export.csv'")

# Close the connection
connection.close()
