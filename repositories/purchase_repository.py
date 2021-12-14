from db.run_sql import run_sql

from models.place import Place
from models.purchase import Purchase
from models.tag import Tag
import repositories.place_repository as place_repository
import repositories.tag_repository as tag_repository

def save(purchase):
    sql = "INSERT INTO purchases (price, place_id, tag_id) VALUES (%s, %s, %s) RETURNING *"
    values = [purchase.price, purchase.place.id, purchase.tag.id]
    results = run_sql(sql, values)
    id = results[0]['id']
    purchase.id = id
    return purchase
    #I think there's an issue here

def select_all():
    purchases = []

    sql = "SELECT * FROM books"
    results = run_sql(sql)

    for row in results:
        place = place_repository.select(row['place_id'])
        tag = tag_repository.select(row['tag_id']) #I think there's an issue here
        purchase = Purchase(row['price'], place, tag, row['id'])
        purchases.append(purchase)
    return purchases

def select(id):
    purchase = None
    sql = "SELECT * FROM purchases WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        place = place_repository.select(result['place_id'])
        tag = tag_repository.select(result['tag_id']) #I think there's an issue here
        purchase = Purchase(result['price'], place, tag, result['id'] )
    return purchase

def delete_all():
    sql = "DELETE  FROM purchases"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM purchases WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(purchase):
    sql = "UPDATE purchases SET (price, place_id, tag_id) = (%s, %s, %s) WHERE id = %s"
    values = [purchase.price, purchase.place.id, purchase.tag.id, purchase.id]
    print(values)
    run_sql(sql, values)

#ADD GET TOTAL HERE 