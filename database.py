import hashlib
import random
import sqlite3
from _md5 import md5

from Crypto import Random
from Crypto.Cipher import AES
import base64, os


class Database:
    def __init__(self, dbname):
        self.dbname = dbname
        self.conn = sqlite3.connect(self.dbname)

    def connect(self):
        try:
            self.conn.execute(
                'CREATE TABLE PERSON (id INT PRIMARY KEY NOT NULL , name TEXT  NOT NULL, last_name TEXT  NOT NULL, age INT NOT NULL);')
        except Exception as e:
            print(e)
        return self.conn

    def disconnect(self):
        self.conn.close()

    def get_records(self):
        cursor = self.conn.cursor()
        sqlite_select_query = "SELECT * FROM PERSON"
        cursor.execute(sqlite_select_query)
        records = cursor.fetchall()
        return records

    def insert_test_data(self):
        for i in range(1, 10):
            fname = 'name' + str(i)
            lname = 'name' + str(i)
            age = 20 + i
            params = (i, fname, lname, age)
            self.conn.execute("INSERT INTO PERSON VALUES (?,?, ?, ?)", params)
            self.conn.commit()

    @staticmethod
    def insert_cipher_data(items):
        connection = sqlite3.connect('cipher.sqlite3')
        try:
            connection.execute(
                'CREATE TABLE CIPHER (data TEXT  NOT NULL, age_index TEXT  NOT NULL);')
        except Exception as e:
            print(e)
            print("baby")
        for i in items:
            data = i[0]
            index = i[1]
            params = (data, index)
            connection.execute("INSERT INTO CIPHER VALUES (?,?)", params)
            connection.commit()