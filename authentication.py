from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()


def encrypt_password(password):
    '''
    this function will encrypt a new users password \n
    password -- the chosen password to encrypt 
    '''
    hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
    return hashed_password


def check_password(hashed_password, entered_password):
    '''
    this will check if the entered password matches the hashed password \n
    hashed_password -- a hashed password from the database \n
    entered_password -- passowrd to compare the hashed password to
    '''
    return bcrypt.check_password_hash(hashed_password, entered_password)
