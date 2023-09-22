from fastapi import APIRouter


router = APIRouter()

@router.get('/')
def start():
    return "Hello, World"