from flask import Flask, render_template, request, redirect
from flask import Blueprint
from models.purchase import Purchase
import repositories.place_repository as place_repository
import repositories.purchase_repository as purchase_repository
import repositories.tag_repository as tag_repository

purchases_blueprint = Blueprint("purchases", __name__)

@purchases_blueprint.route("/purchases")
def purchases():
    purchases = purchase_repository.select_all()
    return render_template("purchases/index.html", purchases = purchases)

@purchases_blueprint.route("/purchases/new")
def new_purchase():
    places = place_repository.select_all()
    tags = tag_repository.select_all()
    return render_template ("/purchases/new.html", places = places, tags = tags)