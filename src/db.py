from typing import List

import mariadb

from models import User

conn = mariadb.connect(
    host="84.38.180.130",
    port=3306,
    user="tanya",
    password="123abc",
    database="tanya_db",
    autocommit=False
)


def add_userr(user: User) -> User:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO user (name, PASSWORD) VALUES (%s, %s);",
        (user.name, user.passw)
    )
    conn.commit()
    new_id = cursor.lastrowid
    return User(
        **{
            **user.model_dump(),
            'id': new_id,
        },
    )

# def get_users (user: User):
#     cursor = conn.cursor()
#     cursor.execute(
#         "INSERT * FROM user"
#     )
#     conn.commit()
