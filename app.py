import uvicorn
from fastapi import FastAPI, Depends, HTTPException
from router.bot import router as bot_router
from dependencies.security_wall import is_ip_allow
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(CORSMiddleware,
                   allow_origins=origins,
                   allow_credentials=True,
                   allow_methods=["*"],
                   allow_headers=["*"],
                   )

app.include_router(router=bot_router, dependencies=[Depends(is_ip_allow)])

if __name__ == "__main__":
    uvicorn.run('app:app', host='localhost', port=1616,
                log_level='info', reload=True)
