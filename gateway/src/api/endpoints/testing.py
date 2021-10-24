from fastapi import APIRouter
import requests


router = APIRouter()


@router.get("/", include_in_schema=False)
def index():
    return "You've reached the testing API service"


@router.get("/gorest")
def get_gorest_users():
    res = requests.get("https://gorest.co.in/public/v1/users")
    return res.json()


@router.get("")
def a():
    pass
