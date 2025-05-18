import uvicorn
from contextlib import asynccontextmanager
from fastapi import FastAPI

from config import logger, settings, SessionManager

from routing import data_phone



@asynccontextmanager
async def lifespan(_apps: FastAPI):
    try:
        yield
    finally:
        await SessionManager.close_session()

app = FastAPI(lifespan=lifespan)

app.include_router(data_phone.router)


if __name__ == "__main__":
    try:
        uvicorn.run(
            app,
            host="0.0.0.0",
            port=settings.app_port,
            log_config="src/logs/log_config.json",
            use_colors=True,
            log_level="info",
            loop="asyncio"
        )
    except Exception as e:
        logger.error(f"Error launch app: {e}")
