from datenbank.API import database
db = database(db_name="example.db",debug=True)
db.connect()
db.disconnect()