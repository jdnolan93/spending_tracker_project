from db.run_sql import run_sql

from models.place import Place
from models.purchase import Purchase
from models.tag import Tag
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository
import repositories.tag_repository as tag_repository

def save(tag):
    sql = "INSERT INTO tags (tag_name, active) VALUES (%s, %s,) RETURNING *"
    values = [tag.tag_name, tag.active]
    results = run_sql(sql, values)
    id = results [0]['id']
    tag.id = id
    return tag

