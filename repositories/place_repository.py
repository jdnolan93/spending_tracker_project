from unittest import result
from db.run_sql import run_sql

from models.place import Place
from models.purchase import Purchase

def save(place):
    sql = "INSERT INTO places (place_name) VALUES (%s) RETURNING *"
    values = [place.place_name]
    results = run_sql(sql, values)
    id = results [0] ['id']
    place.id = id
    return place

def select_all():
    places = []

    sql = "SELECT * FROM places"
    results = run_sql(sql)

    for row in results:
        place = Place(row['place_name'], row['id'])
        places.append(place)
    return places

def select(id):
    place = None
    sql = "SELECT * FROM places WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        place = Place(result['place_name'], result['id'])
    return place