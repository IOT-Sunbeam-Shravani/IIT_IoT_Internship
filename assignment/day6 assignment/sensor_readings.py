import mysql.connector
from datetime import datetime

# ---------------- DATABASE CONNECTION ----------------
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="root",
    database="sensor_readings"
)

cursor = db.cursor()

# ---------------- CREATE ----------------
def insert_data(temp, hum):
    query = """
    INSERT INTO sensor_readings (temperature, humidity, timestamp)
    VALUES (%s, %s, %s)
    """
    cursor.execute(query, (temp, hum, datetime.now()))
    db.commit()
    print("Data inserted successfully")

# ---------------- READ ----------------
def read_all():
    cursor.execute("SELECT * FROM sensor_readings")
    rows = cursor.fetchall()
    print("\nAll Sensor Readings:")
    for row in rows:
        print(row)

# ---------------- UPDATE ----------------
def update_data(record_id, temp, hum):
    query = """
    UPDATE sensor_readings
    SET temperature=%s, humidity=%s
    WHERE id=%s
    """
    cursor.execute(query, (temp, hum, record_id))
    db.commit()
    print("Data updated successfully")

# ---------------- DELETE ----------------
def delete_data(record_id):
    cursor.execute("DELETE FROM sensor_readings WHERE id=%s", (record_id,))
    db.commit()
    print("Data deleted successfully")

# -------- READ BELOW THRESHOLD --------
def below_threshold(temp_limit, hum_limit):
    query = """
    SELECT * FROM sensor_readings
    WHERE temperature < %s OR humidity < %s
    """
    cursor.execute(query, (temp_limit, hum_limit))
    rows = cursor.fetchall()

    print(f"\nReadings below threshold (Temp < {temp_limit} OR Humidity < {hum_limit}):")
    for row in rows:
        print(row)

# ---------------- MAIN ----------------
if __name__ == "__main__":
    insert_data(29.5, 70)
    insert_data(22.3, 45)

    read_all()

    update_data(1, 30.0, 75)

    below_threshold(25, 50)

    delete_data(2)

    read_all()

    cursor.close()
    db.close()
