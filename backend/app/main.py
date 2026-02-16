from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .database.connection import get_db
from .database.models import TestResponse
import uvicorn

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this for production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/status")
async def status(db: AsyncSession = Depends(get_db)):
    try:
        result = await db.execute(select(TestResponse))
        db_response = result.scalars().first()
        
        if not db_response:
            return {
                "status": "online",
                "message": "Database is connected but the test table is empty.",
                "source": "database"
            }
            
        return {
            "status": "online",
            "message": db_response.message,
            "version": db_response.version,
            "source": "database"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": f"Database instance is not available or connection failed: {str(e)}",
            "source": "none"
        }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5001)
