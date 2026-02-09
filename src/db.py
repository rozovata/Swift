from typing import List

import mariadb

from src.models import User

conn = mariadb.connect(
    host="84.38.180.130",
    port=3306,
    user="MrProper1",
    password="qwerty",
    database="MrProper1_db",
    autocommit=False
)


def get_tasks() -> List[User]:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    raw_tasks = cursor.fetchall()
    # (0, 'task1', 'desc', False)
    tasks = []
    for task in raw_tasks:
        tasks.append(User(
            id=task[0],
            name=task[1],
            description=task[2],
            done=task[3],
        ))

    return tasks


def add_user(user: User) -> User:
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO SwiftUsers (UserName, UserPass) VALUES (?, ?)",
        (user.userName, user.userPass)
    )
    conn.commit()
    new_id = cursor.lastrowid
    return User(
        **{
            **user.model_dump(),
            'id': new_id,
        },
    )
