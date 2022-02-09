from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import delete,select
from models import Cities
import os
import json
import requests
from fastapi import status,HTTPException
engine = create_async_engine('postgresql+asyncpg://postgres:postgres@db/postgres')

session = Session(bind=engine,future=True)
async_session = sessionmaker(
    engine, expire_on_commit=False, class_=AsyncSession)

def get_params(name):
    params={
    'q':name,
    "appid":os.environ['API_KEY']
    }
    resp= requests.get("http://api.openweathermap.org/geo/1.0/direct",params=params).json()[0]
    return resp
async def insert_city(name):
    try:
        params=get_params(name)
    except:
        raise HTTPException(status_code=404, detail="Not Found coordinates for this city")
    async with async_session() as session:
        async with session.begin():
            try:
                city=Cities(name=name,lat=params['lat'],lon=params['lon'])
            except:
                raise HTTPException(status_code=400, detail="Something goes wrong on creation")
            session.add(city)
            session.commit()
    return status.HTTP_201_CREATED
async def get_cities():
    list=[]
    async with async_session() as session:
        all_city_list=select(Cities)
        all_city_list= await session.execute(all_city_list)
        for row in all_city_list:
            list.append(row._asdict())
    return list
async def get_city_by_params(lat,lon):
    all_city_list=await get_cities()

    city_diff=[]
    city_name=[]
    for i in all_city_list:
        i=i['Cities']
        db_lat=i.lat
        db_lon=i.lon
        distance_diff=((lat-db_lat)**2)+((lon-db_lon)**2)**0.5
        if len(city_diff)>=2:
            if distance_diff<max(city_diff):
                index=city_diff.index(max(city_diff))
                city_diff[index]=distance_diff
                city_name[index]=i.name
        else:
            city_diff.append(distance_diff)
            city_name.append(i.name)
    print(city_diff,city_name)
    resp_list=[]
    for j in range(len(city_diff)):
        resp_list.append({"name":city_name[j],"difference":city_diff[j]})
    return resp_list
async def delete_city(id):
    async with async_session() as session:
        async with session.begin():
            city=delete(Cities).filter(Cities.id==id)
            await session.execute(city)
            await session.commit()
    resp=await get_cities()
    return resp
