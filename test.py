from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

@app.get("/add")

def add(a:int,b:int):
    return a+b

print(add(3,4 ))

def subtract(a:int, b:int):
    return a-b

class subtractmodel (BaseModel):
    a: int
    b: int



@app.post("/sub")
def subtract_number(model: subtractmodel):
    return {"result": subtract(model.a, model.b)}
#return {"result": subtract(model.a, model.b)} returns a dictionary with the result under the key "result", which FastAPI automatically serializes as JSON in the API response. This is useful for structured responses.*/
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
    

@app.delete("/userdb/delete/{user_id}")
def user_delete(user_id: int):
    if user_id in userdb:
        del userdb[user_id]
        return {"message": "User deleted successfully"}
    else:
        return {"message": "User not found"}
    
print(userdb )  # This will print the current state of userdb after deletion