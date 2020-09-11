from fastapi import APIRouter, Query
from bot.baymax import get_response as baymax_response

router = APIRouter()


@router.get('/baymax')
def index(words: str = Query(None, min_length=2, max_length=100)):
    try:
        response = baymax_response(words)
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
