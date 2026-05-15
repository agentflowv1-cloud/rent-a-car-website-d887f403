from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class CarModel(BaseModel):
    id: int
    name: str
    year: int
    horsepower: int

# Sample in-memory data store for demonstration purposes
CAR_MODELS = [
    CarModel(id=1, name='Toyota Camry', year=2022, horsepower=203),
    CarModel(id=2, name='Honda Civic', year=2021, horsepower=180),
    CarModel(id=3, name='Ford Mustang', year=2020, horsepower=460)
]

@app.get('/car-models/')
async def get_car_models():
    return CAR_MODELS

@app.get('/car-models/{car_model_id}')
async def get_car_model(car_model_id: int):
    for car_model in CAR_MODELS:
        if car_model.id == car_model_id:
            return car_model
    raise HTTPException(status_code=404, detail='Car model not found')