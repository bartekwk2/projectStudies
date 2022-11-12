class User:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User(id={self.id},email={self.email})"


