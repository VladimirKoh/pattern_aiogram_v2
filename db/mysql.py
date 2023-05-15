import aiomysql
from data import config
import logging


async def create_conn():
    conn = await aiomysql.connect(
        host=config.HOST_DB,
        user=config.USER_DB,
        password=config.PASSWORD_DB,
        db=config.DATABASE_DB,
        charset='utf8mb4',
        cursorclass=aiomysql.cursors.DictCursor
    )
    return conn

async def close_conn(conn):
    conn.close()


async def add_user(user_id, user_name, lang, referal):
    conn = await create_conn()
    async with conn.cursor() as cursor:
        query = "INSERT INTO `users` (`user_id`, `user_name`, `lang`, `referal`) VALUES(%s, %s, %s, %s)"
        await cursor.execute(query, (user_id, user_name, lang, referal))
        await conn.commit()
    await close_conn(conn)


async def exist_user(user_id: str):
    conn = await create_conn()
    async with conn.cursor() as cursor:
        query = f"SELECT * FROM `users` WHERE `user_id` = {user_id}"
        await cursor.execute(query)
        data = await cursor.fetchone()
    await close_conn(conn)
    return data