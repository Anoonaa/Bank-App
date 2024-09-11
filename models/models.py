from flask_login import UserMixin

# In-memory user store for testing (to be replaced with sql database)
users = {
    "testuser": {"password": "testpass"},  # Replace with hashed passwords in production
}

class User(UserMixin):
    def __init__(self, username):
        self.id = username  # Flask-Login expects a field named 'id' for the user identifier

    @classmethod
    def verify_password(cls, username, password):
        """
        Verify if the provided username and password are correct.
        """
        user = users.get(username)
        if user and user["password"] == password:
            return True
        return False

    @classmethod
    def get_user(cls, username):
        """
        Fetch the user object. If the user exists, return a User object, else None.
        """
        if username in users:
            return cls(username)
        return None

