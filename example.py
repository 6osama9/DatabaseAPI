from datenbank.API import database
db = database(db_name="example.db",debug=True)

# Create a new database instance
db = Database("my_database.db")

# Connect to the database
db.connect()

# Create a table
db.create_table("users", "id INTEGER PRIMARY KEY, name TEXT, age INTEGER")

# Insert data into the table
db.insert_data("users", "name, age", ("John Doe", 30))

# Select data from the table
users = db.select_data("users")
print(users)

# Update data
db.update_data("users", "age = 31", "name = 'John Doe'")

# Delete data
db.delete_data("users", "name = 'John Doe'")

# Count the number of records
record_count = db.count_records("users")
print(f"Number of records: {record_count}")

# Disconnect from the database
db.disconnect()
