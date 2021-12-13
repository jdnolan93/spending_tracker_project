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