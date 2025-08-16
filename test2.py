from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

userdb={
    1: {"name": "John", "age": 30},
    2: {"name": "Jani", "age": 75}, 
    3: {"name": "JJanardan", "age": 45}
}

class User(BaseModel): 
    name: str
    age: int 

@app.put("/userdb/update/{user_id}")
def user_update(user_id: int, user: User):
    if user_id in userdb:
        userdb[user_id] = user.dict()
        return {"message": "User updated successfully", "user": userdb[user_id]}
    else:
        return {"message": "User not found"}


