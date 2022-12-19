import psycopg2

# establishing the connection
# Replace the database name, username, password, host and port with names related to your database.
conn = psycopg2.connect(
    database="newDB",
    user='postgres', password='abc123',
    host='127.0.0.1', port='5432'
)
# Creating a cursor object using the cursor() method
cursor = conn.cursor()  

# Executing an MYSQL function using the execute() method
cursor.execute("select version()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Connection established to: ", data)

# Enter the CSV File Location here ---
with open("D:\\VetLongAndLang.csv") as f:
  
    next(f) #  To Skip the header row.
    # Replace VetLongAndLang with the TABLE NAME in the POSTGRESQL Database
    cursor.copy_from(f, 'VetLongAndLang', sep=',')

conn.commit()

# Closing the connection
conn.close()