from unittest import result
from db.run_sql import run_sql

from models.place import Place
from models.purchase import Purchase

def save(place):
    sql = "INSERT INTO places (place_name) VALUES (%s) RETURNING id"
    values = [place.place_name]
    results = run_sql(sql, values)
    id = results [0] ['id']
    place.id = id

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

def delete_all():
    sql = "DELETE FROM places"
    run_sql(sql)

def delete(place):
    sql = "DELETE FROM places WHERE id = %s"
    values = [place.id]
    run_sql(sql, values)

def update(place):
    sql = "UPDATE places SET place_name = %s WHERE id = %s"
    values = [place.place_name, place.id]
    run_sql(sql, values)



#delete - pass something in