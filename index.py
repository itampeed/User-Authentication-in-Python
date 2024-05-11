import mysql.connector
import bcrypt
import jwt
from datetime import datetime, timedelta, timezone


# Database configuration
DB_USER = "Your_database_username"
DB_PASSWORD = "Your_database_password"
DB_DATABASE = "authentication_db"
DB_HOST = "Your_database_host(mostly localhost)"

# Connect to the database
def get_database_connection():
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_DATABASE
    )

# Authenticate user and issue authentication token
def authenticate_user(username, password):
    conn = get_database_connection()
    cursor = conn.cursor()

    # Retrieve user record from database
    cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
    user = cursor.fetchone()

    if user:
        # Verify hashed password
        hashed_password = user[2].encode('utf-8')
        if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
            # Extract permissions (assuming permissions are in the third column)
            permissions = user[3]  # Adjust this index based on your database schema

            # Generate authentication token
            token = generate_authentication_token(username, permissions)
            return {'username': username, 'permissions': permissions, 'token': token}

    return None

# Generate authentication token
def generate_authentication_token(username, permissions):
    SECRET_KEY = "Your secret token"  # Replace with your own secure secret key
    payload = {
        'username': username,
        'permissions': permissions,
        'system_name': 'YourSystemName',
        'issued_at': datetime.now(timezone.utc).isoformat(),
        'expires_at': (datetime.now(timezone.utc) + timedelta(hours=1)).isoformat()
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token

# Validate authentication token
def validate_authentication_token(token):
    SECRET_KEY = "Your secrect token"  # Replace with your own secure secret key
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        # Additional validation logic (e.g., check expiration time)
        return payload
    except jwt.ExpiredSignatureError:
        return None  # Token has expired
    except jwt.InvalidTokenError:
        return None  # Invalid token

def main():
    # Simulate user login
    print("User Login")
    username = input("Enter username: ")
    password = input("Enter password: ")

    user_info = authenticate_user(username, password)
    if user_info:
        print("\nAuthentication successful.")
        print(f"Welcome, {username}!")
        print("Your permissions:", user_info['permissions'])

        # Issue authentication token
        token = user_info['token']
        print("Your authentication token:", token)

        # Example: Validate authentication token
        validated_payload = validate_authentication_token(token)
        if validated_payload:
            print("\nAuthentication token is valid.")
            print("Token payload:", validated_payload)
        else:
            print("\nAuthentication token is invalid or expired.")

    else:
        print("\nAuthentication failed. Invalid username or password.")

if __name__ == "__main__":
    main()
