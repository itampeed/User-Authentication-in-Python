# User Authentication in Python

This repository provides a simple example of user authentication in Python using MySQL, bcrypt for password hashing, and JWT (JSON Web Tokens) for secure token-based authentication.

## Features

- User login with username and password
- Hashed password storage in the database
- Generation of authentication tokens
- Token validation and expiration checks

## Prerequisites

- Python 3.x
- MySQL database (you can modify the database configuration in the code)
- Required Python packages: `mysql-connector-python`, `bcrypt`, `PyJWT`

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/itampeed/User-Authentication-in-Python
   cd user-authentication-python
   ```

2. Install the required packages:

   ```bash
   pip install mysql-connector-python bcrypt pyjwt
   ```

3. Set up your MySQL database and configure the database connection in the code (`DB_USER`, `DB_PASSWORD`, `DB_DATABASE`, `DB_HOST`).

4. Generate your secrect key using the prgram below, run it in seperate terminal:

   ```bash
   node -e "console.log(require('crypto').randomBytes(32).toString('hex'))"
   ```
    and then replace your secrect key with the generated one

5. Run the `index.py` script:

   ```bash
   python index.py
   ```

## Usage

1. Simulate user login by entering a valid username and password.
2. If authentication is successful, an authentication token will be generated.
3. You can validate the token using the provided example function.

## Security Considerations

- **Secret Key**: Replace the placeholder secret key (`SECRET_KEY`) with your own secure secret key.
- **Environment Variables**: Avoid hardcoding sensitive information (e.g., database credentials, secret keys) in your code. Use environment variables or configuration files instead.

## License

This project is licensed under the itampeed License and everyone is free to use.

---