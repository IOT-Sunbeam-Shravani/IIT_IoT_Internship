import mysql.connector
connection = mysql.connector.connect(
    host = "127.0.0.1",
    port = 3306,
    user = "root",
    password = "root",
    database = "smart_agri",
    use_pure = True
)

sensor_id = int(input("Enter id to be deleted : "))

query = "DELETE FROM  soil_moisture WHERE sensor_id= %s;"

cursor = connection.cursor()

cursor.execute(query , (sensor_id,))

connection.commit()

print("Record deleted successfully")

cursor.close()

connection.close()

