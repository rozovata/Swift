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


def re_userr(user: User) -> User:
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE user SET name = %s , PASSWORD = %s WHERE id =  %s ;",
        (user.name, user.passw, user.id)
    )
    conn.commit()
    return User(
        **{
            **user.model_dump(),
        },
    )


def get_user_by_user_password(user: User) -> User:
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM user WHERE name = %s and password = %s ;",
        (user.name, user.passw)
    )
    user = cursor.fetchall()  # [(2, 'danya', '111')]
    if len(user) == 1:
        return User(id=user[0][0], name=user[0][1], passw=user[0][2])
    else:
        return User(id = -1, name="-1", passw="-1")