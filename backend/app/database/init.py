import asyncio
from .connection import engine, Base
from .models import TestResponse
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import sessionmaker

async def init_db():
    async with engine.begin() as conn:
        # Create tables
        await conn.run_sync(Base.metadata.create_all)
    
    # Seed initial data
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )
    
    async with async_session() as session:
        from sqlalchemy import select
        result = await session.execute(select(TestResponse))
        if not result.scalars().first():
            db_response = TestResponse(
                message="Hello from the PostgreSQL database!",
                version="1.0.0"
            )
            session.add(db_response)
            await session.commit()
            print("Database initialized and seeded!")
        else:
            print("Database already contains data.")

if __name__ == "__main__":
    asyncio.run(init_db())
