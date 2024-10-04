import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
connection = sqlite3.connect('my_database.db')

# Create a cursor object to execute SQL commands
cursor = connection.cursor()

# Create the Clients table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Clients (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nom TEXT NOT NULL,
        prenom TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        date_inscription TEXT NOT NULL
    )
''')

# Create the Commandes table with a foreign key referencing Clients
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Commandes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        client_id INTEGER,
        produit TEXT NOT NULL,
        date_commande TEXT NOT NULL,
        FOREIGN KEY (client_id) REFERENCES Clients(id)
    )
''')

# Commit changes and close the connection
connection.commit()
connection.close()

print("Tables created successfully!")
