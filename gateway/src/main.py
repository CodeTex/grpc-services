from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from uvicorn import run

from api.api import api_router
from core.config import get_settings


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", include_in_schema=False)
async def root():
    return f"{get_settings().app_name} server started."


# Endpoint routing
app.include_router(api_router, prefix=get_settings().api_v1_str)


if __name__ == "__main__":
    settings = get_settings()
    # https://github.com/encode/uvicorn/blob/48edc940522a3d0d7529922a23ac019eeb53f629/uvicorn/config.py#L186
    run(
        app="main:app",
        host=settings.server_host,
        port=settings.server_port,
        reload=True,
    )
