from fastapi import Request,HTTPException

valid_ip_list = ['120.136.26.229','127.0.0.1']

def is_ip_allow(request:Request):
    if request.client.host not in valid_ip_list:
        raise HTTPException(status_code=403,detail="Acesss denied")

