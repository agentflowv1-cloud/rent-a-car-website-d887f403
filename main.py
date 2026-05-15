from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPBasic
from pydantic import BaseModel
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
import uvicorn

# Define the database connection
SQLALCHEMY_DATABASE_URL = "postgresql://user:password@localhost/db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Define the CarModel table
class CarModel(Base):
    __tablename__ = "car_models"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)

# Create the database tables
Base.metadata.create_all(bind=engine)

# Define the CarModel schema
class CarModelSchema(BaseModel):
    name: str

# Define the admin interface
app = FastAPI()

# Define the authentication scheme
security = HTTPBasic()

# Define the add car model endpoint
@app.post("/car-models")
async def add_car_model(car_model: CarModelSchema, credentials: HTTPBasicAuth = Depends(security)):
    # Authenticate the admin
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid admin credentials")

    # Add the car model to the database
    db = SessionLocal()
    existing_car_model = db.query(CarModel).filter(CarModel.name == car_model.name).first()
    if existing_car_model:
        raise HTTPException(status_code=400, detail="Car model already exists")
    new_car_model = CarModel(name=car_model.name)
    db.add(new_car_model)
    db.commit()
    return {"message": "Car model added successfully"}

# Define the remove car model endpoint
@app.delete("/car-models/{car_model_name}")
async def remove_car_model(car_model_name: str, credentials: HTTPBasicAuth = Depends(security)):
    # Authenticate the admin
    if credentials.username != "admin" or credentials.password != "password":
        raise HTTPException(status_code=401, detail="Invalid admin credentials")

    # Remove the car model from the database
    db = SessionLocal()
    car_model = db.query(CarModel).filter(CarModel.name == car_model_name).first()
    if not car_model:
        raise HTTPException(status_code=404, detail="Car model not found")
    db.delete(car_model)
    db.commit()
    return {"message": "Car model removed successfully"}

# Run the application
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)