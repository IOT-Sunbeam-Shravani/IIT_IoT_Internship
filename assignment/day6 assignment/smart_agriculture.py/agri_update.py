import mysql.connector

connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri",
    use_pure = True
)

sensor_id = int(input("Enter sensor id to update: "))
moisture_level = int(input("Enter new moisture_level: "))

query = """
UPDATE soil_moisture
SET moisture_level =%s
WHERE sensor_id = %s
"""


cursor = connection.cursor()

cursor.execute(query, (moisture_level, sensor_id))

connection.commit()

print(cursor.rowcount,"row(s) updated")

cursor.close()

connection.close()

