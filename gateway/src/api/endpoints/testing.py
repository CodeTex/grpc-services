import json

from fastapi import APIRouter
import requests

from api.utils import data_dir


router = APIRouter()


@router.get("/", include_in_schema=False)
def index():
    return "You've reached the testing API service"


@router.get("/gorest")
def get_gorest_users():
    res = requests.get("https://gorest.co.in/public/v1/users")
    return res.json()


@router.get("/local")
def get_local_json():
    with open(data_dir / "test_data.json", "r") as f:
        data = json.load(f)
    return data
