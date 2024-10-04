import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = connection.cursor()

# List of commandes
commandes = [
    (4, 'Monitor', '2024-10-10'),
    (5, 'Keyboard', '2024-10-10'),
    (6, 'Mouse', '2024-10-11')
]

# Insert each commande one by one
for commande in commandes:
    try:
        cursor.execute('''
            INSERT INTO Commandes (client_id, produit, date_commande)
            VALUES (?, ?, ?)
        ''', commande)
        print(f"Inserted commande for client_id: {commande[0]}, product: {commande[1]}")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting commande for client_id {commande[0]}: {e}")

# Commit changes and close the connection
connection.commit()
connection.close()

print("Data insertion attempt completed!")
