import aiomysql
from aiomysql import DictCursor


class Database:
    def __init__(self, host, port, user, password, db):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.db = db
        self.pool = None
        self._result = None

    async def _connect(self):
        if self.pool is None:
            self.pool = await aiomysql.create_pool(host=self.host, port=self.port, user=self.user,
                                                   password=self.password, db=self.db, maxsize=10)

    async def _disconnect(self):
        if self.pool:
            self.pool.close()
            await self.pool.wait_closed()
            self.pool = None

    async def execute(self, query, *args, **kwargs):
        await self._connect()
        async with self.pool.acquire() as conn:
            async with conn.cursor(DictCursor) as cur:
                await cur.execute(query, *args, **kwargs)
                self._result = cur

    async def fetchone(self):
        if self._result is not None:
            return await self._result.fetchone()
        else:
            raise ValueError("No query has been executed yet.")

    async def fetchall(self):
        if self._result is not None:
            return await self._result.fetchall()
        else:
            raise ValueError("No query has been executed yet.")

    async def __aenter__(self):
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self._disconnect()

    async def get_all_users(self):
        await self.execute("SELECT * FROM users")
        users = await self.fetchall()
        return users
