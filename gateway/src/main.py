from functools import lru_cache

from fastapi import FastAPI
import uvicorn

from core.config import Settings


@lru_cache
def get_settings():
    return Settings()


app = FastAPI()


@app.get("/", include_in_schema=False)
async def root():
    return f"{get_settings().app_name} server started."


if __name__ == "__main__":
    settings = get_settings()
    # https://github.com/encode/uvicorn/blob/48edc940522a3d0d7529922a23ac019eeb53f629/uvicorn/config.py#L186
    uvicorn.run(
        app="main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
