import sqlite3

# Connect to SQLite database (it will create the database file if it doesn't exist)
conn = sqlite3.connect('maintenance.db')
cursor = conn.cursor()

# Create Service Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Service (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    description TEXT,
    price REAL NOT NULL
)
''')

# Create Category Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Category (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL
)
''')

# Create Technician Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Technician (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    specialty TEXT
)
''')

# Create ServiceTechnician Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ServiceTechnician (
    service_id INTEGER,
    technician_id INTEGER,
    date_assigned DATE,
    PRIMARY KEY (service_id, technician_id),
    FOREIGN KEY (service_id) REFERENCES Service(id),
    FOREIGN KEY (technician_id) REFERENCES Technician(id)
)
''')


# Connect to the SQLite database
conn = sqlite3.connect('maintenance.db')
cursor = conn.cursor()

# List of categories to be added
categories = [
    "Electronics Repair",
    "Plumbing",
    "Electricity",
    "Internet",
    "Woodwork"
]

# Insert categories into the Category table
for category in categories:
    cursor.execute('''
    INSERT INTO Category (name)
    VALUES (?)
    ''', (category,))

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Categories added successfully.")
