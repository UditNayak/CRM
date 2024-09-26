import mysql.connector
from mysql.connector import errorcode

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='udit-mysql'  # Make sure this is the correct password
    )

    cursor = connection.cursor()

    # Create a database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS crm")

    # Close the cursor and connection
    cursor.close()
    connection.close()

    print("Database created successfully")

    # Now, connect to the newly created database
    database = mysql.connector.connect(
        host='localhost',
        user='root',
        password='udit-mysql',
        database='crm'
    )

    print("Connected to the 'crm' database")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        print(f"Error: {err}")

