import sqlite3
import os

def execute_query(q):

    conn = sqlite3.connect("mfgdb")
    cursor = conn.cursor()

    try:
        cursor.execute()
        conn.commit()
    
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
        conn.rollback()

    finally:
        conn.close()
