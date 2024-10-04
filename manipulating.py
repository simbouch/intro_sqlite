import sqlite3

# Connect to SQLite database
connection = sqlite3.connect('my_database.db')

# Create a cursor object
cursor = connection.cursor()

# Select all clients
cursor.execute("SELECT * FROM Clients")
clients = cursor.fetchall()
print("All Clients:")
for client in clients:
    print(client)

# Retrieve orders of a specific client (client_id = 1)
client_id = 1
cursor.execute("SELECT * FROM Commandes WHERE client_id = ?", (client_id,))
commandes = cursor.fetchall()
print(f"\nOrders for client_id {client_id}:")
for commande in commandes:
    print(commande)

# Update the email address of a specific client (client_id = 1)
new_email = 'new.email@example.com'
cursor.execute("UPDATE Clients SET email = ? WHERE id = ?", (new_email, client_id))
print(f"\nUpdated email for client_id {client_id} to {new_email}")

# Delete a specific order (order id = 1)
order_id = 1
cursor.execute("DELETE FROM Commandes WHERE id = ?", (order_id,))
print(f"\nDeleted order with id {order_id}")

# Commit changes and close the connection
connection.commit()
connection.close()

print("\nQuery and update operations completed successfully!")
