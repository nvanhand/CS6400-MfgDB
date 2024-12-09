import os
import csv
import sqlite3

print(os.getcwd())
conn = sqlite3.connect("mfgdb")
cursor = conn.cursor()
f = os.path.join("0_preprocessing", "clean_data", "daq.csv")
with open(f, 'r') as file:
    csv_reader = csv.reader(file)
    
    for row in csv_reader:
        
        try:
            q = f'INSERT INTO SensorData (BuildID, SensorSerial, Value, Date, Time) VALUES (?,?,?,?,?)'
            cursor.execute(q, row)  
            conn.commit()      
        except sqlite3.Error as e:
            conn.rollback()

conn.close()