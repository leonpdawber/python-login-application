import sqlite3
import bcrypt 
import getpass

# Functions for database handling
def connect_to_database():
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    return conn, cur

def close_database_connection(conn):
    conn.close()

# Functions for user interface
def display_welcome_message():
    print("Welcome to the User Authentication System!")
    print("==========================================")

def display_menu():
    print("\nMenu:")
    print("1. Log in")
    print("2. Sign up")
    print("3. Exit")

def display_login_prompt():
    print("\nLog In")
    print("------")

def display_signup_prompt():
    print("\nSign Up")
    print("-------")

def get_username_password():
    username = input("Please enter your username: ")
    password = getpass.getpass("Please enter your password: ")
    return username, password

def display_error_message(message):
    print("Error:", message)

def login_successful():
    print("Login successful.")

def signup_successful():
    print("User signed up successfully.")

def user_already_exists():
    print("Username already exists. Please choose a different one.")

def incorrect_password():
    print("Incorrect password.")

def user_not_found():
    print("User not found.")

# Functions for program logic
def startProgram():
    while True:
        try:
            display_welcome_message()
            conn, cur = connect_to_database()
            cur.execute("""CREATE TABLE IF NOT EXISTS logins (username TEXT, password TEXT)""")
            close_database_connection(conn)
        except sqlite3.Error as errormessage:
            display_error_message("Error reading data from SQLite database: " + str(errormessage))

        display_menu()
        option = input("Please select an option: ")

        if option == "1":
            login()
        elif option == "2":
            signup()
        elif option == "3":
            print("Goodbye!")
            break
        else:
            print("Please enter a valid option.")

def signup():
    try:
        display_signup_prompt()
        conn, cur = connect_to_database()

        username, password = get_username_password()

        while True:
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            cur.execute("SELECT * FROM logins WHERE username=?", (username,))
            existing_user = cur.fetchone()
            if existing_user:
                user_already_exists()
                username, password = get_username_password()
            else:
                credentials = (username, hashed_password)
                cur.execute("""INSERT INTO logins (username, password) VALUES (?, ?)""", credentials)
                conn.commit()
                signup_successful()
                break

        close_database_connection(conn)
    except sqlite3.Error as errormessage:
        display_error_message("Error signing up: " + str(errormessage))

def login():
    try:
        display_login_prompt()
        conn, cur = connect_to_database()

        cur.execute("SELECT COUNT(*) FROM logins")
        count = cur.fetchone()[0]
        if count == 0:
            print("No users found in the database. Please sign up first.")
            return

        while True:
            username, password = get_username_password()

            cur.execute("SELECT password FROM logins WHERE username=?", (username,))
            row = cur.fetchone()
            if row:
                hashed_password_from_db = row[0]
                hashed_password_input = bcrypt.hashpw(password.encode(), hashed_password_from_db)
                if hashed_password_input == hashed_password_from_db:
                    login_successful()
                    break
                else:
                    incorrect_password()
            else:
                user_not_found()

        close_database_connection(conn)
    except sqlite3.Error as errormessage:
        display_error_message("Error logging in: " + str(errormessage))

# Start the program
startProgram()