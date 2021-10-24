from fastapi import APIRouter


router = APIRouter()


@router.get("/", include_in_schema=False)
def index():
    return "You've reached the testing API service"
