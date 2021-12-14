from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.purchase import Purchase
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository
import repositories.tag_repository as tag_repository

tags_blueprint = Blueprint("tags", __name__)

@tags_blueprint.route("/tags")
def tags():
    tags = tag_repository.select_all()
    return render_template("tags/index.html", tags = tags)

@tags_blueprint.route("/tags/new")
def new_tag():
    return render_template("/tags/new.html")

@tags_blueprint.route("/tags", methods=["POST"])
def create_tag():
    tag_name = request.form["name"]
    new_tag = Tag(tag_name)
    tag_repository.save(new_tag)
    return redirect("/tags")