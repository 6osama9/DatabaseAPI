import sqlite3

class Database:
    def __init__(self, db_name, debug: bool = True):
        self.db_name = db_name
        self.debug = debug
        self.connected = False

    # Connects user to the database
    def connect(self):
        try:
            self.conn = sqlite3.connect(self.db_name)
            self.cursor = self.conn.cursor()
            if self.debug:
                print(f"Connected to {self.db_name}")
            self.connected = True
        except Exception as e:
            print(f"Failed to connect to {self.db_name} | \n {e}")

    # Disconnects user from the database
    def disconnect(self):
        if self.connected and self.conn:
            self.conn.close()
            self.connected = False
        if self.debug:
            print(f"Disconnected from {self.db_name}")

    # Creates a table
    def create_table(self, table_name: str, columns: str):
        if self.debug:
            print(f"Creating table {table_name}")
        try:
            self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})")
            self.conn.commit()
        except Exception as e:
            print(f"Failed to create table {table_name} | \n {e}")

    # Inserts data into a table
    def insert_data(self, table_name: str, columns: str, values: tuple):
        if self.debug:
            print(f"Inserting data into {table_name}")
        try:
            placeholders = ", ".join(["?" for _ in values])  # Placeholder for values
            sql = f"INSERT INTO {table_name} ({columns}) VALUES ({placeholders})"
            self.cursor.execute(sql, values)
            self.conn.commit()
        except Exception as e:
            print(f"Failed to insert data into {table_name} | \n {e}")

    # Selects data from a table
    def select_data(self, table_name: str, columns: str = "*", where: str = ""):
        if self.debug:
            print(f"Selecting data from {table_name}")
        try:
            sql = f"SELECT {columns} FROM {table_name} {where}"
            self.cursor.execute(sql)
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Failed to select data from {table_name} | \n {e}")

    # Deletes data from a table
    def delete_data(self, table_name: str, where: str):
        if self.debug:
            print(f"Deleting data from {table_name}")
        try:
            sql = f"DELETE FROM {table_name} WHERE {where}"
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(f"Failed to delete data from {table_name} | \n {e}")

    # Updates data in a table
    def update_data(self, table_name: str, set_values: str, where: str):
        if self.debug:
            print(f"Updating data in {table_name}")
        try:
            sql = f"UPDATE {table_name} SET {set_values} WHERE {where}"
            self.cursor.execute(sql)
            self.conn.commit()
        except Exception as e:
            print(f"Failed to update data in {table_name} | \n {e}")

    # Drops a table
    def drop_table(self, table_name: str):
        if self.debug:
            print(f"Dropping table {table_name}")
        try:
            self.cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
            self.conn.commit()
        except Exception as e:
            print(f"Failed to drop table {table_name} | \n {e}")

    # Adds a column to a table
    def add_column(self, table_name: str, column_name: str, column_type: str):
        if self.debug:
            print(f"Adding column {column_name} to table {table_name}")
        try:
            self.cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {column_type}")
            self.conn.commit()
        except Exception as e:
            print(f"Failed to add column {column_name} to {table_name} | \n {e}")

    # Shows the schema of a table
    def show_table_schema(self, table_name: str):
        if self.debug:
            print(f"Showing schema for table {table_name}")
        try:
            self.cursor.execute(f"PRAGMA table_info({table_name})")
            return self.cursor.fetchall()
        except Exception as e:
            print(f"Failed to show schema for {table_name} | \n {e}")

    # Counts the number of records in a table
    def count_records(self, table_name: str):
        if self.debug:
            print(f"Counting records in {table_name}")
        try:
            self.cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
            return self.cursor.fetchone()[0]
        except Exception as e:
            print(f"Failed to count records in {table_name} | \n {e}")

    # Executes any custom SQL code
    def execute_sql(self, code: str):
        if self.debug:
            print(f"Executing SQL code in {self.db_name}")
        try:
            self.cursor.execute(code)
            self.conn.commit()
        except Exception as e:
            print(f"Failed to execute SQL code | \n {e}")
