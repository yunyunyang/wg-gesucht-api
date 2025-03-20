from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from src.api.city import query_city
from src.api.room import query_room

app = FastAPI()


@app.get("/wg_gesucht/api/v1/room/{city_id}/{city_name}/{page_id}", tags=["Room"])
def query_rooms(city_id: str, city_name: str, page_id: int):

    result = query_room(city_name, city_id, page_id)
    return result


@app.get("/wg_gesucht/api/v1/city/{keyword}", tags=["City"])
def query_city_info(keyword: str):

    result = query_city(keyword)
    return result
