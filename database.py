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