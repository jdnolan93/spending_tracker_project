from db.run_sql import run_sql

from models.place import Place
from models.purchase import Purchase
from models.tag import Tag
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository
import repositories.tag_repository as tag_repository

def save(tag):
    sql = "INSERT INTO tags (tag_name) VALUES (%s) RETURNING id"
    values = [tag.tag_name]
    results = run_sql(sql, values)
    id = results [0]['id']
    tag.id = id

def select_all():
    tags = []

    sql = "SELECT * FROM tags"
    results = run_sql(sql)

    for row in results:
        tag = Tag(row['tag_name'], row ['id'])
        tags.append(tag)
    return tags

def select(id):
    tag = None
    sql = "SELECT * FROM tags WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        tag = Tag(result['tag_name'], result['id'])
    return tag

def delete_all():
    sql = "DELETE FROM tags"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM tags WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def update(tag):
    sql = "UPDATE tags SET tag_name = %s WHERE id = %s"
    values = [tag.tag_name, tag.id]
    run_sql(sql, values)