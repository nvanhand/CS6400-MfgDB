import psycopg2 as pg
import os

connection_dict = {"host": "ampfdb.postgres.database.azure.com",
                   "dbname": "machine_data", 
                   "user": "georgeburdell",
                   "password": "Buzz1972",
                   "sslmode": "require",
                   "connect_timeout": 10
                   }

# Construct connection string
conn = pg.connect(**connection_dict)

print("Connection established")

cursor = conn.cursor()


## Print all the tables in the schema 
cursor.execute("""SELECT table_name FROM information_schema.tables
                     WHERE table_schema = 'public'""")
print('executed' )
for table in cursor.fetchall():
       print(table[0])
       try:
              ## Unsuppress to drop all the tables
              #cursor.execute(f"DROP TABLE IF EXISTS {table[0]}")
              conn.commit()
       except:
              conn.rollback()

## Execute table creation from table_string queries
for i in ['cinncinati', 'eos_m280', 'fronius', 'powder_lots']:
    print(i)
    with open(os.path.join('table_strings',i), 'r') as f:
        query = f.read()
        try:
            cursor.execute(query)
            print("successful transaction")
            conn.commit()
        except:
            print('error')
            conn.rollback()


cursor.close()
conn.close()