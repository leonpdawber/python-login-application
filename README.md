**Python LoginA Application**

This Python program provides basic user authentication functionalities including sign up and login. It utilizes SQLite for database storage and bcrypt for password hashing.

**Features:**

- **Sign up:** Allows users to create an account by providing a username and password. The password is securely hashed before being stored in the database.
- **Login:** Enables existing users to log in with their username and password. Passwords are compared securely using bcrypt hashing.
- **User Interface:** Provides a simple command-line interface with clear prompts and messages for user interaction.
- **Error Handling:** Incorporates error handling mechanisms to manage database-related errors and user input validation.

**Functionality Overview:**

1. **connect_to_database():** Establishes a connection to the SQLite database and returns the connection and cursor objects.
2. **close_database_connection(conn):** Closes the database connection.
3. **display_welcome_message():** Displays a welcome message at the beginning of the program execution.
4. **display_menu():** Shows the main menu options for the user.
5. **display_login_prompt():** Displays prompts related to the login process.
6. **display_signup_prompt():** Displays prompts related to the signup process.
7. **get_username_password():** Prompts the user to enter a username and password securely using getpass.
8. **display_error_message(message):** Displays error messages during program execution.
9. **login_successful():** Indicates successful login to the user.
10. **signup_successful():** Notifies the user upon successful signup.
11. **user_already_exists():** Informs the user if the chosen username already exists during signup.
12. **incorrect_password():** Notifies the user if the provided password is incorrect during login.
13. **user_not_found():** Informs the user if the username is not found during login.
14. **startProgram():** Main function to initiate the program. Displays the welcome message, handles database initialization, presents the main menu, and directs user actions based on menu options.
15. **signup():** Handles the signup process, including username availability checks and password hashing.
16. **login():** Manages the login process, verifying user credentials against stored hashed passwords in the database.

**Usage:**

- Run the program to initiate the user authentication system.
- Follow the prompts to sign up for a new account or log in with an existing one.
- The system provides appropriate feedback and error messages based on user actions.

**Dependencies:**

- sqlite3
- bcrypt
- getpass
