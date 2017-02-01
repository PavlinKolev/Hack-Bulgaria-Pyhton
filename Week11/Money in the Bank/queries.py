CREATE_CLIENTS_TABLE = '''
    CREATE TABLE IF NOT EXISTS CLIENTS(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        password TEXT,
        balance REAL DEFAULT 0,
        message TEXT,
        count_tries INTEGER DEFAULT 0,
        time_for_wrong_tries TIMESTAMP DEFAULT (datetime('now', 'localtime')),
        time_banned TIMESTAMP DEFAULT (datetime('now', 'localtime'))
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
GET_ALL_USERAMES = '''
    SELECT username
    FROM CLIENTS
'''
GET_USERNAME_BY_ID = '''
    SELECT username
    FROM CLIENTS
    WHERE id == ?
'''

GET_COUNT_TRIES = '''
    SELECT count_tries
    FROM CLIENTS
    WHERE username == ?
'''

SET_COUNT_TRIES = '''
    UPDATE CLIENTS
    SET count_tries = ?
    WHERE username == ?
'''

GET_TIME_FOR_WRONG_TRIES = '''
    SELECT time_for_wrong_tries
    FROM CLIENTS
    WHERE username == ?
'''

SET_TIME_FOR_WRONG_TRIES = '''
    UPDATE CLIENTS
    SET time_for_wrong_tries = ?
    WHERE username == ?
'''

GET_TIME_BANNED = '''
    SELECT time_banned
    FROM CLIENTS
    WHERE username == ?
'''

SET_TIME_BANNED = '''
    UPDATE CLIENTS
    SET time_banned = ?
    WHERE username == ?
'''
