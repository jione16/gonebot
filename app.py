import uvicorn
from fastapi import FastAPI,Depends,HTTPException
from router.bot import router as bot_router

app = FastAPI()


app.include_router(router=bot_router)

if __name__ == "__main__":
    uvicorn.run('app:app', host='localhost', port=1616,
                log_level='info', reload=True)
