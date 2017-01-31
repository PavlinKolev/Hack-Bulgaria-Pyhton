CREATE_CLIENTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS CLIENTS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        balance REAL DEFAULT 0,
        message TEXT
        )
'''


UPDATE_MESSAGE_OF_CLIENT = '''
    UPDATE CLIENTS
    SET message = ?
    WHERE id == ?
'''


UPDATE_PASSWORD_OF_CLIENT = '''
    UPDATE CLIENTS
    SET password = ?
    WHERE id == ?
'''


ADD_CLIENT = '''
    INSERT INTO CLIENTS(username, password)
    VALUES (?, ?)
'''


GET_CLIENT_DATA = '''
    SELECT id, balance, message
    FROM CLIENTS
    WHERE username == ? AND password == ?
'''


GET_USERNAME_BY_ID = '''
    SELECT username
    FROM CLIENTS
    WHERE id == ?
'''
