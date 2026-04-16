import aiosqlite 
import asyncio

async def init_db():
    async with aiosqlite.connect("vape_shop.db") as db:
        await db.execute("""
                         CREATE TABLE IF NOT EXISTS users (
                tg_id INTEGER PRIMARY KEY,   -- ID из Телеграма (уникальный)
                username TEXT,               -- Юзернейм (@name)
                full_name TEXT,              -- Имя из профиля
                balance INTEGER DEFAULT 0,   -- Бонусы (по умолчанию 0)
                total_spent INTEGER DEFAULT 0 -- Всего потрачено (для уровней кешбэка)
            )
        """)
        await db.commit()

if __name__ == "__main__":
    asyncio.run(init_db)


async def check_or_add_user(tg_id: int,username: str, full_name: str):
    async with aiosqlite.connect("vape_shop.db") as db:
        cursor = await db.execute("SELECT tg_id FROM users WHERE user_id = ?", (tg_id,))
        user = await cursor.fetchone()
        if user: #проверку пользовалетля в БД
            return False #пользователь есть
        else:
            await db.execute(
                "INSERT INTO users (tg_id, username,full_name,balance) VALUES (?,?,?,?)", #Пользователя нет
                (tg_id,username,full_name,100)
            )
            await db.commit() #это как обычный коммит - сохранение изменений в БД
            return True #пользователь новый