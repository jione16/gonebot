from fastapi import APIRouter, Query
from bot.bot import get_response

router = APIRouter()


@router.get('/get_response')
def index(words: str = Query(None, min_length=2, max_length=100)):
    try:
        response = get_response(words)
        print(response)
        return {
            "error": False,
            "response": str(response)
        }
    except Exception as identifier:
        print(identifier)
        return {
            "error": True,
            "message": str(identifier)
        }
