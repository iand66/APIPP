# Fast API example from Pretty Printed

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class City(BaseModel):
    name: str
    timezone: str

db = {
    0: City(name='London', timezone='United Kingdom'), 
    1: City(name='Paris', timezone='France'), 
    2: City(name='Rome',timezone='Italy')
}

@app.get('/')
def index():
    return db

@app.get('/cities')
def get_cities():
    return db

@app.get('/cities/{id}')
def get_cities(id: int):
    return db[id]

@app.post('/cities')
def create_city(city: City):
    db.append(city.dict())
    return db[-1]

@app.put('/cities/{id}', response_model=City)
def update_city(id: int, city:City):
    db[id] = city
    return city

@app.delete('/cities')
def delete_city(id: int):
    db.pop(id)
    return {}