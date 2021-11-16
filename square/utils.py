import os
import random
import sqlite3
import string
from faker import Faker


def generate_password(length):
    result = ''
    for i in range(length):
        result += random.choice(string.ascii_letters)
    return result


def execute_query(query, args=()):
    db_path = os.path.join(os.getcwd(), 'chinook.db')
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(query, args)
    conn.commit()
    records = cur.fetchall()
    return records


def format_list(lst):
    resp = ''
    for entry in lst:
        resp += '<br>' + str(entry)
    return resp


def format_name(lst):
    resp = ''
    for entry in lst:
        for st in entry:
            resp += str(st) + '<br>'
    return resp


def generate_users(count):
    fake = Faker()
    result = ''
    for i in range(count):
        result += fake.name() + ': ' + fake.email() + '<br>'
    return result
