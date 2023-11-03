import mysql.connector

# Connect to the database
def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='madram',
            password='developer#1$',
            database='test_gpt'
        )
        return connection
    except:
        print("Error connecting to the database")
        return None

# Create table if not exists
def create_table(connection):
    try:
        cursor = connection.cursor()
        query = """
            CREATE TABLE IF NOT EXISTS names (
                id INT AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(255),
                last_name VARCHAR(255)
            )
        """
        cursor.execute(query)
        cursor.close()
        connection.commit()
    except:
        print("Error creating table")

# Insert names into the table
def insert_names(connection, first_names, last_names):
    try:
        cursor = connection.cursor()
        query = """
            INSERT INTO names (first_name, last_name) VALUES (%s, %s)
        """
        for first_name, last_name in zip(first_names, last_names):
            cursor.execute(query, (first_name, last_name))
        cursor.close()
        connection.commit()
        print("Names inserted successfully")
    except:
        print("Error inserting names")

# Get names from user
def get_names():
    first_names = []
    last_names = []
    while True:
        first_name = input("Enter first name (blank to stop): ")
        if first_name == '':
            break
        last_name = input("Enter last name: ")
        first_names.append(first_name)
        last_names.append(last_name)
    return first_names, last_names

# Main function
def main():
    # Connect to the database
    connection = connect_to_database()
    if connection is None:
        return

    # Create table if not exists
    create_table(connection)

    # Get names from user
    first_names, last_names = get_names()

    # Insert names into the table
    insert_names(connection, first_names, last_names)

    # Close the database connection
    connection.close()

# Call the main function
if __name__ == '__main__':
    main()
