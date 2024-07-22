import mysql.connector
from mysql.connector import errorcode

def create_database(cursor):
    try:
        cursor.execute(
            "CREATE DATABASE IF NOT EXISTS alx_book_store DEFAULT CHARACTER SET 'utf8'")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)

def connect_to_mysql():
    try:
        cnx = mysql.connector.connect(
            user='root',
            password='your_password',
            host='localhost'
        )
        cursor = cnx.cursor()
        return cnx, cursor
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
        return None, None

def close_connection(cnx, cursor):
    cursor.close()
    cnx.close()

def main():
    cnx, cursor = connect_to_mysql()
    if cnx is not None and cursor is not None:
        create_database(cursor)
        close_connection(cnx, cursor)

if __name__ == "__main__":
    main()
