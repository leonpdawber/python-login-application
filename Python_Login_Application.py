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
    print("\nWelcome to the User Authentication System!")
    print("\n==========================================")

def display_menu():
    print("\nMenu:")
    print("-----")
    print("\n1. Log in")
    print("2. Sign up")
    print("3. Exit")

def display_login_prompt():
    print("\nLog In:")
    print("------")

def display_signup_prompt():
    print("\nSign Up:")
    print("-------")

def get_username_password():
    while True:
        username = input("\nPlease enter your username: ").strip()
        password = getpass.getpass("Please enter your password: ").strip()
        
        if username and password:  # Check if both username and password are non-empty
            return username, password
        else:
            print("\nUsername and password cannot be empty. Please try again.")

def display_error_message(message):
    print("\nError:", message)

def login_successful(username):
    print(f"\nLogin to User: {username} successful.")

def signup_successful(username):
    print(f"\nUser: {username} signed up successfully.")

def user_already_exists():
    print("\nUsername already exists. Please choose a different one.")

def incorrect_password():
    print("\nIncorrect password.")

def user_not_found():
    print("\nUser not found.")

# Functions for program logic

display_welcome_message()
    
def start_program():
    while True:
        try:
            conn, cur = connect_to_database()
            cur.execute("""CREATE TABLE IF NOT EXISTS logins (username TEXT, password TEXT)""")
            close_database_connection(conn)
        except sqlite3.Error as error_message:
            display_error_message("\nError reading data from SQLite database: " + str(error_message))

        display_menu()
        option = input("\nPlease select an option: ").strip()

        if option == "1":
            login()
        elif option == "2":
            sign_up()
        elif option == "3":
            print("\nGoodbye!")
            break
        else:
            print("\nPlease enter a valid option.")

def sign_up():
    try:
        display_signup_prompt()
        conn, cur = connect_to_database()

        username = input("\nPlease enter your desired username: ").strip()

        # Check if the username already exists in the database
        cur.execute("SELECT * FROM logins WHERE username=?", (username,))
        existing_user = cur.fetchone()
        if existing_user:
            user_already_exists()
            close_database_connection(conn)
            return  # Exit the function if the user already exists

        # If the username does not exist, proceed with signing up
        password = getpass.getpass("Please enter your password: ").strip()
        
        # Increase the number of hashing rounds for better security
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt(rounds=14))
        
        credentials = (username, hashed_password)
        cur.execute("""INSERT INTO logins (username, password) VALUES (?, ?)""", credentials)
        conn.commit()
        signup_successful(username)

        close_database_connection(conn)
    except sqlite3.Error as error_message:
        display_error_message("\nError signing up: " + str(error_message))

def login():
    try:
        display_login_prompt()
        conn, cur = connect_to_database()

        cur.execute("SELECT COUNT(*) FROM logins")
        count = cur.fetchone()[0]
        if count == 0:
            print("\nNo users found in the database. Please sign up first.")
            return

        while True:
            username, password = get_username_password()

            cur.execute("SELECT password FROM logins WHERE username=?", (username,))
            row = cur.fetchone()
            if row:
                hashed_password_from_db = row[0]
                if bcrypt.checkpw(password.encode(), hashed_password_from_db):
                    login_successful(username)
                    break
                else:
                    incorrect_password()
            else:
                user_not_found()
        close_database_connection(conn)
    except sqlite3.Error as error_message:
        display_error_message("\nError logging in: " + str(error_message))

# Start the program
start_program()
