import mysql.connector
from mysql.connector import Error


def create_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="YOUR_MYSQL_PASSWORD",
            database="orphanage_db"
        )

        if connection.is_connected():
            print("✓ Successfully connected to MySQL!")
            return connection

    except Error as e:
        print("✗ Error while connecting to MySQL:", e)

    return None


def main():
    print("=" * 55)
    print("        ORPHANAGE HOME MANAGEMENT SYSTEM")
    print("=" * 55)

    connection = create_connection()

    if connection:
        print("\nDatabase connection established.")
        connection.close()
        print("Database connection closed.")


if __name__ == "__main__":
    main()
