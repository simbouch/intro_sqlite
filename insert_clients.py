import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = connection.cursor()

# List of clients
clients = [
    ('Arthur', 'Royer', 'arthur.royer92@orange.fr', '2024-10-03'),
    ('Khadydi', 'Diagne', 'khadydiagne18@gmail.com', '2024-10-03'),
    ('Axel', 'Munerol', 'axel.munerol@gmail.com', '2024-10-03')
]

# Insert each client one by one
for client in clients:
    try:
        cursor.execute('''
            INSERT INTO Clients (nom, prenom, email, date_inscription)
            VALUES (?, ?, ?, ?)
        ''', client)
        print(f"Inserted client: {client[1]}, {client[0]}")
    except sqlite3.IntegrityError as e:
        print(f"Error inserting {client[1]}: {e}")

# Commit changes and close the connection
connection.commit()
connection.close()

print("Data insertion attempt completed!")
