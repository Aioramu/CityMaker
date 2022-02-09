from fastapi import Request,FastAPI,Body,HTTPException,status
from pydantic import BaseModel
from actions import *
from fastapi.responses import JSONResponse

app = FastAPI()

class CityAdd(BaseModel):
    name :str
class CityDelete(BaseModel):
    id :int
class FindBy(BaseModel):
    lat : float
    lon : float

@app.get("/list/")
async def city_list():
    resp=await get_cities()
    return resp
@app.post("/add/")
async def city_list(city:CityAdd):
    resp=await insert_city(city.name)
    return JSONResponse(status_code=resp)
@app.post("/find/")
async def city_list(coords:FindBy):
    resp=await get_city_by_params(coords.lat,coords.lon)
    return resp

@app.delete("/delete/")
async def city_list(id:CityDelete):
    resp=await delete_city(id.id)
    return resp
