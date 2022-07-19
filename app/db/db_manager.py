import asyncio
import aiosqlite


class Database:
	def __init__(self, db_path: str = 'database.db') -> None:
		self._db_path = db_path

	def connection(self) -> aiosqlite.Connection:
		return aiosqlite.connect(database=self._db_path)

	async def create_user(self, date: str, nick: str, balance: int, info: str, username: str) -> None:
		async with self.connection() as db:
			await db.execute('INSERT INTO users (date, nick, balance, info, username) VALUES (?, ?, ?, ?, ?)', (date, nick, balance, info, username))
			await db.commit()

	async def get_users(self) -> list:
		async with self.connection() as db:
			cursor = await db.execute('SELECT * FROM users')
			result = await cursor.fetchall()
			return result

	async def get_user(self, nick: str) -> list:
		async with self.connection() as db:
			cursor = await db.execute('SELECT * FROM users WHERE nick = ?', (nick,))
			result = await cursor.fetchall()
			return result


async def main():
	db = Database()

	# tasks = []
	# for i in range(1000):
	# 	tasks.append(db.get_users())

	# await asyncio.gather(*tasks)
	result = await db.get_users()
	print(result)
	result = await db.set_active(123, 1)
	print(result)


if __name__ == '__main__':
	asyncio.run(main())
