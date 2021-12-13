from db.run_sql import run_sql

from models.place import Place
from models.purchase import Purchase
import repositories.place_repository as place_repository

def save(purchase):
    sql = "INSERT INTO purchases (item_name, price, place_id) VALUES (%s, %s, %s) RETURNING *"
    values = [purchase.item_name, purchase.price, purchase.place.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    purchase.id = id
    return purchase

def select_all():
    purchases = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        place = place_repository.select(row['place_id'])
        purchase = Purchase(row['item_name'], row['price'], place, row['id'])
        purchases.append(purchase)
    return purchases

