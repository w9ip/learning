def is_password_good(password):
    if len(password) >= 8 and [e for e in password if e.isupper()] and [
        e for e in password if e.islower()
    ] and [e for e in password if e.isdigit()]:
        return True
    return False
