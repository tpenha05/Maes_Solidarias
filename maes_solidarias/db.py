import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('maes_solidarias/db.sqlite3')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Define the SQL statement to create a table
# query = '''
# CREATE TABLE IF NOT EXISTS accounts_customuser (
#     id INTEGER PRIMARY KEY AUTOINCREMENT,
#     email TEXT NOT NULL UNIQUE,
#     nome_completo TEXT NOT NULL,
#     telefone_celular TEXT NOT NULL,
#     last_login TEXT,
#     is_superuser BOOLEAN NOT NULL,
#     password TEXT NOT NULL
# )
#  '''
query = '''
DROP TABLE IF EXISTS accounts_customuser;
'''

# Execute the SQL statement to create the table
cursor.execute(query)

# Commit the transaction (if necessary)
conn.commit()

# Close the cursor and the connection
cursor.close()
conn.close()