# Python Login Application

This is a simple user authentication system implemented in Python using SQLite for database storage and bcrypt for password hashing. It provides functionality for user sign-up, login, and error handling.

## Features

- User sign-up: Users can create new accounts by providing a username and password. Passwords are securely hashed before being stored in the database.
- User login: Registered users can log in using their username and password.
- Error handling: The system handles various error conditions, such as empty username/password fields, existing usernames during sign-up, incorrect passwords during login, and database errors.
- SQL injection mitigation: Where applicable, the application uses prepared statements to mitigate the risk of SQL injection attacks.

## Requirements

- Python 3.x
- SQLite3
- bcrypt

## How to Use

1. Clone the repository to your local machine.
2. Ensure you have Python installed along with the required dependencies.
3. Run the `main.py` file using Python: `python main.py`.
4. Follow the on-screen prompts to sign up or log in.

## Files

- `main.py`: Contains the main logic of the user authentication system.
- `database.db`: SQLite database file where user information is stored. If this file doesn't already exist, it will be created upon script execution.
- `README.md`: This file providing information about the project.

## Usage

- Upon running the program, you'll be presented with a menu offering options to log in, sign up, or exit.
- Choose the appropriate option and follow the prompts to complete the desired action.
- After signing up or logging in successfully, you'll receive a confirmation message.
- If any errors occur during the process, appropriate error messages will be displayed.
